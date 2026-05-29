"""配置加载：密钥一律从环境变量读取，禁止硬编码。"""

import os


def load_api_secret() -> str:
    """从环境变量读取支付网关密钥。

    缺失时直接抛错，避免用空串静默走到下游扣款逻辑。
    """
    secret = os.environ.get("PAYMENT_API_SECRET")
    if not secret:
        raise RuntimeError("PAYMENT_API_SECRET 未配置，拒绝启动")
    return secret


def gateway_base_url() -> str:
    """支付网关地址，可被环境变量覆盖，默认走生产。"""
    return os.environ.get("PAYMENT_GATEWAY_URL", "https://api.gateway.example.com/v1")
