from typing import List, NamedTuple, Set
from math import sqrt

from test_framework import generic_test

class Y(NamedTuple):
    a: int
    b: int

class HeapNode(NamedTuple):
    y: Y

    @property
    def k(self) -> float:
        return self.y.a + self.y.b * sqrt(2)

    def __eq__(self, other) -> bool:
        return self.k == other.k

    def __lt__(self, other) -> bool:
        return self.k < other.k

def insert(min_heap: List[HeapNode], x: HeapNode) -> None:
    min_heap.append(x)
    i = len(min_heap)-1
    while i > 0:
        parent_idx = (i-1) // 2
        if min_heap[i].k < min_heap[parent_idx].k:
            min_heap[i], min_heap[parent_idx] = min_heap[parent_idx], min_heap[i]
            i = parent_idx
        else:
            break

def extract_min(min_heap: List[HeapNode]) -> HeapNode:
    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    n = min_heap.pop()
    i = 0
    while i < len(min_heap):
        if 2*i+2 < len(min_heap) and min_heap[2*i+2] < min_heap[2*i+1]:
            smallest_child_idx = 2*i+2
        elif 2*i+1 < len(min_heap):
            smallest_child_idx = 2*i+1
        else:
            break

        if min_heap[smallest_child_idx].k < min_heap[i].k:
            min_heap[smallest_child_idx], min_heap[i] = min_heap[i], min_heap[smallest_child_idx]
            i = smallest_child_idx
        else:
            break

    return n


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    heap: List[HeapNode] = [HeapNode(Y(a=0, b=0))]
    into_heap: Set[float] = {0}
    r: List[float] = []
    for _ in range(k):
        n = extract_min(heap)
        r.append(n.k)
        n1 = HeapNode(Y(n.y.a+1, n.y.b))
        n2 = HeapNode(Y(n.y.a, n.y.b+1))
        if n1.k not in into_heap:
            insert(heap, n1)
            into_heap.add(n1.k)
        if n2.k not in into_heap:
            insert(heap, n2)
            into_heap.add(n2.k)

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
