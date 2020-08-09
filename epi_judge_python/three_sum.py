from typing import List, Set

from test_framework import generic_test

def has_two_sum(A: List[int], t: int) -> bool:
    S = set(A)
    for a in A:
        if t-a in S:
            return True

    return False

def has_three_sum(A: List[int], t: int) -> bool:
    for a in A:
        if has_two_sum(A, t-a):
            return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
