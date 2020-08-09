from typing import List
import sys

from test_framework import generic_test

INF = sys.maxsize

def get_max_trapped_water(heights: List[int]) -> int:
    i, j = 0, len(heights)-1
    m = -INF
    while i < j:
        if heights[i] < heights[j]:
            m = max(m, abs(i-j) * heights[i])
            i += 1
        elif heights[j] < heights[i]:
            m = max(m, abs(i-j) * heights[j])
            j -= 1
        else: # height[i] == height[j]
            m = max(m, abs(i-j) * heights[j])
            i += 1
            j -= 1
    return m


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
