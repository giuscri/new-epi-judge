from functools import lru_cache
from test_framework import generic_test

def levenshtein_distance(A: str, B: str) -> int:
    n, m = len(A) + 1, len(B) + 1
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j

    for i in range(1, n):
        for j in range(1, m):
            # it's easier to understand why the definition of dp[i][j] is true
            # moving from the bottom-right to the upper-left corner. For example:
            # from dp[i][j] to dp[i][j - 1] is insert/append as we inserted/appended
            # the last character of the second string to the first one and moved both forward
            dp[i][j] = min(
                1 + dp[i - 1][j], # delete
                1 + dp[i][j - 1], # insert (append)
                dp[i - 1][j - 1] + (1 if A[i - 1] != B[j - 1] else 0) # substitute or already same character
            )

    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
