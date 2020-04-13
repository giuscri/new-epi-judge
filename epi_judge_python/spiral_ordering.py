from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not square_matrix:
        return []

    r = []
    n, m = len(square_matrix), len(square_matrix[0])
    i, j, offset = 0, 0, 0
    while offset < (n+1) // 2:
        while j < m-offset:
            r.append(square_matrix[i][j])
            j += 1
        j -= 1
        i += 1

        while i < n-offset:
            r.append(square_matrix[i][j])
            i += 1
        i -= 1
        j -= 1

        while j >= offset:
            r.append(square_matrix[i][j])
            j -= 1
        j += 1
        i -= 1

        while i >= offset+1:
            r.append(square_matrix[i][j])
            i -= 1
        i += 1
        j += 1

        offset += 1

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
