"""Задача 3. Чи містить зв'язаний список цикл.

Алгоритм Флойда ("черепаха і заєць"): повільний вказівник робить 1 крок,
швидкий - 2. Якщо цикл є, швидкий колись наздожене повільного.
Пам'ять O(1).
"""


def has_cycle(head):
    """Повертає True, якщо у списку є цикл."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False   # швидкий вказівник дійшов до кінця - циклу немає
