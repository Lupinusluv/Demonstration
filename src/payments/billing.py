"""计费逻辑：密钥从配置读取，异常按类型捕获，不吞错。"""

from typing import Any

from .config import load_api_secret


class PaymentError(RuntimeError):
    """计费失败时抛出，携带可读原因。"""


class PaymentProcessor:
    """封装扣款 / 退款，密钥在构造时从环境注入。"""

    def __init__(self) -> None:
        self._secret = load_api_secret()

    def _validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise PaymentError(f"金额必须为正：{amount}")

    def charge(self, amount: int, token: str) -> dict[str, Any]:
        """对指定 token 扣款。校验失败抛 PaymentError，不返回 None 掩盖错误。"""
        self._validate_amount(amount)
        if not token:
            raise PaymentError("缺少支付 token")
        try:
            # 省略真实网关调用；此处仅演示规范结构。
            return {"ok": True, "amount": amount, "token": token}
        except (ConnectionError, TimeoutError) as exc:
            # 只捕获预期的网络类异常，并向上抛出可读错误。
            raise PaymentError("支付网关不可达") from exc

    def refund(self, charge_id: str, amount: int) -> dict[str, Any]:
        """按扣款 ID 退款。"""
        self._validate_amount(amount)
        return {"ok": True, "charge_id": charge_id, "refunded": amount}
