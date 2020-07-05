import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    n, m = len(items), capacity+1
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        if j < items[0].weight:
            dp[0][j] = 0
        else:
            dp[0][j] = items[0].value

    for i in range(1, n):
        for j in range(m):
            if j >= items[i].weight:
                dp[i][j] = max(dp[i-1][j], items[i].value + dp[i-1][j - items[i].weight])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
