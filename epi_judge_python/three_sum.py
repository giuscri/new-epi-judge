from typing import List, Set

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    S: Set[int] = set()
    for a in A:
        S.add(t-a)

    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i] + A[j] in S:
                return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
