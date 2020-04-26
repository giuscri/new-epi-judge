from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from math import inf


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L

    # set `p` to where the sublist to reverse starts
    # prev_p is the last node of the original list head
    prev_p = None
    p = L
    i = 1
    while p is not None and i < start:
        prev_p = p
        p = p.next
        i += 1

    # reverse the sublist starting at p
    previous = None
    current = p
    while current is not None and i <= finish:
        current_next = current.next
        current.next = previous
        previous = current
        current = current_next
        i += 1

    # attach sublist to the original list tail
    p.next = current

    # attach original list head to sublist
    if prev_p is not None:
        prev_p.next = previous
        return L # the head hasn't changed
    else:
        return previous


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
