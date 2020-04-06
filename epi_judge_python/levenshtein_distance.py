from functools import lru_cache
from test_framework import generic_test

@lru_cache()
def levenshtein_distance(A: str, B: str) -> int:
    if len(A) == 0 or len(B) == 0:
        return len(A) + len(B)

    if A[0] == B[0]:
        return levenshtein_distance(A[1:], B[1:])
    
    d = levenshtein_distance(A[1:], B)
    s = levenshtein_distance(A[1:], B[1:])
    i = levenshtein_distance(A, B[1:])

    return 1 + min(d, s, i)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
