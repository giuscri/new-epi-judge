from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    n, m = len(A)+1, len(B)+1

    previous = list(range(m))
    current = [0 for _ in range(m)]

    for i in range(1, n):
        current[0] = i
        for j in range(1, m):
            if A[i-1] == B[j-1]:
                current[j] = previous[j-1]
            else:
                current[j] = 1 + min(current[j-1], previous[j], previous[j-1])

        previous = current
        current = [0 for _ in range(m)]

    return previous[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
