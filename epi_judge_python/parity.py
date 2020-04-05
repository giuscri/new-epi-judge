from test_framework import generic_test
from typing import Dict

def precompute() -> Dict[int, int]:
    cache: Dict[int, int] = dict()
    for x in range(2 ** 16):
        cache[x] = _parity(x)
    return cache

def _parity(x: int) -> int:
    p = 0
    while x > 0:
        p ^= (x & 1)
        x >>= 1
    return p

CACHE = precompute()

def parity(x: int) -> int:
    p1 = CACHE[x & (2 ** 16 - 1)]
    p2 = CACHE[(x >> 16) & (2 ** 16 - 1)]
    p3 = CACHE[(x >> 32) & (2 ** 16 - 1)]
    p4 = CACHE[(x >> 48) & (2 ** 16 - 1)]
    return p1 ^ p2 ^ p3 ^ p4

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
