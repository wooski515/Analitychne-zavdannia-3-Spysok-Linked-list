"""Задача 4. Перевпорядкувати список: L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...

Значення у вузлах не змінюються, переставляються самі вузли.
"""


def reorder_list(head):
    """Перевпорядковує список на місці."""
    if head is None or head.next is None:
        return
    # 1. Знаходимо середину: slow зупиниться в кінці першої половини
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 2. Відрізаємо другу половину і розвертаємо її
    second = slow.next
    slow.next = None
    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt
    second = prev   # голова розвернутої другої половини (Ln, Ln-1, ...)
    # 3. По черзі вставляємо вузли другої половини між вузлами першої
    first = head
    while second:
        first_next, second_next = first.next, second.next
        first.next = second
        second.next = first_next
        first, second = first_next, second_next
