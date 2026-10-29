"""Задача 8. Розвернути вузли списку групами по k.

Якщо в кінці залишилось менше k вузлів, вони не змінюються.
Значення у вузлах не змінюються, переставляються самі вузли.
"""

from list_node import ListNode


def reverse_k_group(head, k):
    """Розвертає кожну групу з k вузлів і повертає нову голову списку."""
    dummy = ListNode(0, head)
    group_prev = dummy   # вузол перед поточною групою
    while True:
        # Шукаємо k-й вузол групи; якщо його немає - залишок коротший за k
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        group_next = kth.next   # перший вузол наступної групи
        # Розвертаємо групу: перший вузол групи має вказувати на group_next
        prev, curr = group_next, group_prev.next
        while curr is not group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = group_prev.next   # колишній перший вузол тепер останній у групі
        group_prev.next = kth     # k-й вузол тепер перший у групі
        group_prev = first
