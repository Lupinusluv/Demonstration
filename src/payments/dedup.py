"""去重工具：用哈希集合 / 计数器，复杂度 O(n)。"""

from collections import Counter
from typing import Hashable, Iterable, TypeVar

T = TypeVar("T", bound=Hashable)


def find_duplicates(items: Iterable[T]) -> list[T]:
    """返回出现次数 >= 2 的元素。基于 Counter，单次遍历 O(n)。"""
    counts = Counter(items)
    return [value for value, count in counts.items() if count >= 2]


def unique_preserve_order(items: Iterable[T]) -> list[T]:
    """去重并保持首次出现顺序。用集合做 O(1) 成员判断。"""
    seen: set[T] = set()
    result: list[T] = []
    for value in items:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
