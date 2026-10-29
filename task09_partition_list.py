"""Задача 9. Розділити список: вузли < x перед вузлами >= x.

Вихідний порядок вузлів усередині кожної частини зберігається.
"""

from list_node import ListNode


def partition(head, x):
    """Повертає голову розділеного списку."""
    less_dummy = ListNode()   # вузли зі значенням < x
    more_dummy = ListNode()   # вузли зі значенням >= x
    less, more = less_dummy, more_dummy
    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            more.next = head
            more = more.next
        head = head.next
    more.next = None                 # кінець списку, щоб не лишилось старих посилань
    less.next = more_dummy.next      # приєднуємо другу частину до першої
    return less_dummy.next
