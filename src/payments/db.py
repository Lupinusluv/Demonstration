"""订单数据访问：所有查询使用参数化占位符，杜绝 SQL 注入。"""

import sqlite3
from typing import Any


def connect(db_path: str) -> sqlite3.Connection:
    """打开数据库连接并启用行工厂，便于按列名取值。"""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


class OrderRepository:
    """订单仓储，封装参数化查询。"""

    def __init__(self, conn: sqlite3.Connection) -> None:
        self._conn = conn

    def get_user_orders(self, user_id: int) -> list[dict[str, Any]]:
        """按用户 ID 查订单，使用占位符绑定参数，user_id 不拼进 SQL。"""
        cur = self._conn.execute(
            "SELECT * FROM orders WHERE user_id = ?",
            (user_id,),
        )
        return [dict(row) for row in cur.fetchall()]

    def get_order_by_id(self, order_id: int) -> dict[str, Any] | None:
        """按订单 ID 查单条记录。"""
        cur = self._conn.execute(
            "SELECT * FROM orders WHERE id = ?",
            (order_id,),
        )
        row = cur.fetchone()
        return dict(row) if row else None
