"""Задача 6. Подвоїти число, записане цифрами у зв'язаному списку.

Перенос у розряд виникає лише тоді, коли наступна (молодша) цифра >= 5,
бо 5 * 2 = 10. Тому достатньо одного проходу зліва направо.
"""

from list_node import ListNode


def double_it(head):
    """Подвоює число й повертає голову списку з результатом."""
    # Старша цифра >= 5 дасть перенос - потрібен новий старший розряд
    if head.val >= 5:
        head = ListNode(0, head)
    node = head
    while node:
        node.val = (node.val * 2) % 10
        if node.next and node.next.val >= 5:   # перенос з молодшого розряду
            node.val += 1
        node = node.next
    return head
