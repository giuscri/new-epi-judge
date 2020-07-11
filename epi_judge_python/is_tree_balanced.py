from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple

def f(tree: BinaryTreeNode) -> Tuple[bool, int]:
    if tree is None:
        return (True, -1)

    left_balanced, left_height = f(tree.left)
    right_balanced, right_height = f(tree.right)
    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    return (balanced, max(left_height, right_height) + 1)

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    balanced, _ = f(tree)
    return balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
