from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i, j = 0, 0
    r: List[int] = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            x = A[i]
            r.append(x)
            while i < len(A) and A[i] == x:
                i += 1
            while j < len(B) and B[j] == x:
                j += 1
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
