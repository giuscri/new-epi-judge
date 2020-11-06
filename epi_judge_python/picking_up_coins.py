from typing import List, Dict, Tuple
from functools import lru_cache

from test_framework import generic_test

def f(C: List[int], i: int, j: int, cache: Dict[Tuple[int, int], int]) -> int:
    if j-i+1 == 1:
        return C[i]
    if j-i+1 == 2:
        return max(C[i], C[i+1])

    if (i, j) in cache:
        return cache[(i, j)]

    to_cache = max(
        C[i] + min(f(C, i+2, j, cache), f(C, i+1, j-1, cache)),
        C[j] + min(f(C, i+1, j-1, cache), f(C, i, j-2, cache)),
    )
    cache[(i, j)] = to_cache
    return to_cache

def maximum_revenue(coins: List[int]) -> int:
    return f(coins, 0, len(coins)-1, {})


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
