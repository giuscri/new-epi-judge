from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    n = 1
    candidate = next(stream)
    for x in stream:
        if n == 0:
            candidate = x
            n += 1
        elif n > 0 and x != candidate:
            n -= 1
        elif n > 0 and x == candidate:
            n += 1
        else: # n < 0
            assert False
    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
