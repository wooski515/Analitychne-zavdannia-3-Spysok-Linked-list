"""Задача 1. Об'єднати два відсортовані зв'язані списки."""

from list_node import ListNode


def merge_two_lists(list1, list2):
    """Зшиває вузли list1 і list2 в один відсортований список і повертає його голову."""
    dummy = ListNode()   # фіктивна голова, щоб не обробляти перший вузол окремо
    tail = dummy
    while list1 and list2:
        # Приєднуємо менший з двох поточних вузлів
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    # Залишок одного зі списків уже відсортований - просто приєднуємо його
    tail.next = list1 if list1 else list2
    return dummy.next
