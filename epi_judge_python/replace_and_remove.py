import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    if not s:
        return 0

    j = len(s)-1
    i = j
    while i > 0 and (s[i] == "" or s[i] == "b"):
        i -= 1

    assert s[i+1] == "" or s[i+1] == "b"

    while i >= 0:
        if s[i] != "b":
            s[j] = s[i]
            j -= 1
        i -= 1

    j += 1
    i = 0
    while j < len(s):
        if s[j] == "a":
            s[i] = "d"
            s[i+1] = "d"
            i += 1
        else:
            s[i] = s[j]
        i += 1
        j += 1

    return i


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
