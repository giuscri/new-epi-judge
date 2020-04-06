import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    items.sort(key=lambda i: i.weight)

    m = capacity + 1
    n = len(items)
    M = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        M[i][0] = 0

    for j in range(m):
        if j < items[0].weight:
            M[0][j] = 0
        else:
            M[0][j] = items[0].value

    for i in range(1, n):
        for j in range(1, m):
            if j < items[i].weight:
                M[i][j] = M[i - 1][j]
            else:
                M[i][j] = max(items[i].value + M[i - 1][j - items[i].weight], M[i - 1][j])

    return M[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
