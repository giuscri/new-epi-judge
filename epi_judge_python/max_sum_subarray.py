from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    n = len(A)
    S = 0
    min_sum = 0
    max_sum = 0
    a, b = -1, -1
    min_idx = -1
    for j in range(n):
        S += A[j]
        if S < min_sum:
            min_sum = S
            min_idx = j
        if S - min_sum > max_sum:
            max_sum = S - min_sum
            a, b = min_idx + 1, j
    assert max_sum == sum(A[a:b+1])
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
