"""Задача 2. Видалити дублікати з відсортованого зв'язаного списку."""


def delete_duplicates(head):
    """Залишає кожне значення лише один раз і повертає голову списку."""
    node = head
    while node and node.next:
        if node.next.val == node.val:
            node.next = node.next.next   # пропускаємо вузол-дублікат
        else:
            node = node.next
    return head
