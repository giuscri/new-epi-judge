from typing import List
from math import inf

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    l = inf
    r = -inf
    for i in range(len(prices)):
        l = min(l, prices[i])
        r = max(r, prices[i] - l)

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
