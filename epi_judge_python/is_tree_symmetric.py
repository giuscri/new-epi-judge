from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import List

def f(left: BinaryTreeNode, right: BinaryTreeNode) -> bool:
    if not left and not right:
        return True

    if left and not right or not left and right:
        return False

    if left.data != right.data:
        return False

    return f(left.left, right.right) and f(left.right, right.left)

def is_symmetric(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True

    return f(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
