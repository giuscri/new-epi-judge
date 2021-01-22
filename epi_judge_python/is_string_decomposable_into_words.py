import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def decompose_into_dictionary_words(s: str,
                                    D: Set[str]) -> List[str]:
    W = 0
    for w in D:
        W = max(len(w), W)

    n = len(s)
    T = [[] for _ in range(n)]
    for i in range(n):
        j = i
        curr = ""
        while j >= 0 and j >= i-W:
            curr = s[j]+curr
            if curr in D and T[j-1]:
                T[i] = T[j-1]+[curr]
                break

            j -= 1

        if j < 0:
            T[i] = [curr] if curr in D else []

    return T[-1]

@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
