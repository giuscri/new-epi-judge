from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    ptr = tree
    while ptr is not None and ptr.data != key:
        if key < ptr.data:
            ptr = ptr.left
        else:
            ptr = ptr.right

    return ptr

def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
