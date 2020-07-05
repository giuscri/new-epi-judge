from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    prev = [1 for _ in range(m)]
    row = [1 for _ in range(m)]

    for _ in range(1, n):
        for j in range(1, m):
            row[j] = prev[j] + row[j-1]
        prev = row

    return row[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
