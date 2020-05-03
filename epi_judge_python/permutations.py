from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    if not A:
        return [[]]

    n = len(A)
    r = []
    for i in range(n):
        ps = permutations(A[:i] + A[i+1:])
        for p in ps:
            r.append(p + [A[i]])
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
