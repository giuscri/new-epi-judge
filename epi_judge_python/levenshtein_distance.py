from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    n, m = len(A)+1, len(B)+1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        dp[0][j] = j
    for i in range(n):
        dp[i][0] = i

    for i in range(1, n):
        for j in range(1, m):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
