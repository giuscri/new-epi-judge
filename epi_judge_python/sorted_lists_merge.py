from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:

    if not L1:
        return L2
    elif not L2:
        return L1

    if L1.data > L2.data:
        L1, L2 = L2, L1

    p, q = L1, L2

    while p is not None and q is not None:
        if p.data <= q.data and (p.next is None or q.data <= p.next.data):
            nextp = p.next
            nextq = q.next
            p.next = q
            q.next = nextp
            q = nextq

        p = p.next

    return L1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
