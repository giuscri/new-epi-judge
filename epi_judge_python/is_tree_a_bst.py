from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple

def f(tree: BinaryTreeNode) -> Tuple[bool, int, int]:
    if tree.left is None:
        left_valid, mL, ML = True, tree.data, tree.data
    else:
        left_valid, mL, ML = f(tree.left)

    if tree.right is None:
        right_valid, mR, MR = True, tree.data, tree.data
    else:
        right_valid, mR, MR = f(tree.right)

    valid = left_valid and right_valid and ML <= tree.data <= mR
    return (valid, mL, MR)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True

    valid, _, _ = f(tree)
    return valid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
