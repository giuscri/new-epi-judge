from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    n = len(A)
    dp = [0 for _ in range(n)]
    for i in range(n):
        M = 0
        for j in range(i):
            if A[j] > A[i]:
                continue
            M = max(M, dp[j])

        dp[i] = M+1

    return max(dp)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
