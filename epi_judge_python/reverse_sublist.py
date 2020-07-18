from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from typing import List

def reverse_list(L: Optional[ListNode], n: int) -> Optional[ListNode]:
    if L is None:
        return None

    if n < 0:
        raise RuntimeError("n is < 0")

    stack: List[ListNode] = []

    prev: Optional[ListNode] = None
    p = L
    while p is not None and n > 0:
        stack.append(p)
        prev = p
        p = p.next
        n -= 1

    L = prev
    prev = None
    while len(stack) > 0:
        p = stack.pop()
        p.next = None
        if prev:
            prev.next = p
        prev = p

    return L

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if start < 1:
        return L

    if finish-start < 0:
        raise RuntimeError(f"{finish} is less than start={start}")

    if L is None:
        return None

    prev: Optional[ListNode] = None
    p: Optional[ListNode] = L
    for _ in range(start-1):
        if p is None:
            raise RuntimeError(f"list is shorter than {start} nodes")

        prev = p
        p = p.next

    q = p
    for _ in range(finish-start+1):
        if q is None:
            raise RuntimeError(f"list is shorter than {finish-start} nodes")

        q = q.next

    rev = reverse_list(p, finish-start+1)
    if prev is not None:
        prev.next = rev
    else:
        L = rev

    assert p is not None
    p.next = q
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
