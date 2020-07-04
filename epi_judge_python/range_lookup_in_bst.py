import collections
from typing import List

from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))

def inorder(tree: BstNode, r: List[int], interval: Interval) -> None:
    if tree is None:
        return

    if tree.data >= interval.left:
        inorder(tree.left, r, interval)

    if interval.left <= tree.data <= interval.right:
        r.append(tree.data)

    if tree.data < interval.right:
        inorder(tree.right, r, interval)

def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    r = []
    inorder(tree, r, interval)
    return r


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
