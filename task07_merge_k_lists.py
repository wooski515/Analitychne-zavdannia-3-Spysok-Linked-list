"""Задача 7. Об'єднати k відсортованих списків.

Зливаємо списки попарно (як у сортуванні злиттям), використовуючи функцію
з задачі 1. За кожен прохід кількість списків зменшується вдвічі,
тому загальна складність O(N * log k), де N - кількість усіх вузлів.
"""

from task01_merge_two_lists import merge_two_lists


def merge_k_lists(lists):
    """Повертає голову одного відсортованого списку з усіх списків lists."""
    if not lists:
        return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            second = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two_lists(lists[i], second))
        lists = merged
    return lists[0]
