from test_framework import generic_test


def parity(x: int) -> int:
    p = 0
    while x > 0:
        p ^= (x & 1)
        x >>= 1
    return p


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
