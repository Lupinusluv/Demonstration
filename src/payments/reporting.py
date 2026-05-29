"""报表生成：用 join 一次性拼接，避免循环内字符串累加。"""

from typing import Any, Sequence


def build_report(rows: Sequence[Any]) -> str:
    """把每行渲染成文本并用换行连接。join 只分配一次，O(n)。"""
    return "\n".join(str(row) for row in rows)


def summarize(rows: Sequence[Any]) -> dict[str, int]:
    """给出行数与去重后行数的简单汇总。"""
    distinct = {str(row) for row in rows}
    return {"total": len(rows), "distinct": len(distinct)}
