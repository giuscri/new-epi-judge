from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    if tree is None:
        return []

    if k == 0:
        return []

    r: List[int] = []

    r += find_k_largest_in_bst(tree.right, k)

    if len(r) < k:
        r += [tree.data]

    if k - len(r) > 0:
        r += find_k_largest_in_bst(tree.left, k - len(r)) # `+=` as a whole is O(k)
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
