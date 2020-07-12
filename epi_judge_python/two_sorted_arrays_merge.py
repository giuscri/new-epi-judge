from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    if len(B) != n:
        raise RuntimeError("n should equal len(B)")

    if len(A) < len(B):
        raise RuntimeError("A should be larger than B")

    i = 0
    while i < m:
        A[len(A)-1-i] = A[m-1-i]
        i += 1

    i = len(A)-m
    j = 0
    k = 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            A[k] = A[i]
            i += 1
        else:
            A[k] = B[j]
            j += 1
        k += 1

    while i < len(A):
        A[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        A[k] = B[j]
        j += 1
        k += 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
