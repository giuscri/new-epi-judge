from list_node import ListNode, list_size
from test_framework import generic_test
from typing import List

def reverse(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    prev, curr = None, head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def is_linked_list_a_palindrome(L: ListNode) -> bool:
    if not L:
        return True

    length = list_size(L)
    if length%2 == 0:
        mid = (length // 2) - 1
    else:
        mid = length // 2


    p = L
    i = 0
    while p is not None and i < mid:
        p = p.next
        i += 1

    p.next = reverse(p.next)

    p = L
    i = 0
    while p is not None and i <= mid:
        p = p.next
        i += 1

    q = L
    i = 0
    while p is not None and i < mid:
        if q.data != p.data:
            return False

        p = p.next
        q = q.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
