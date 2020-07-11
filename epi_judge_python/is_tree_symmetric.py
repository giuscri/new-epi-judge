from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import List


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    if not tree.left and tree.right or tree.left and not tree.right:
        return False

    if not tree.left and not tree.right:
        return True

    p_queue: List[BinaryTreeNode] = [tree.left]
    q_queue: List[BinaryTreeNode] = [tree.right]

    while p_queue and q_queue:
        p = p_queue.pop(0)
        q = q_queue.pop(0)

        if p.data != q.data:
            return False

        if p.right:
            p_queue.append(p.right)
        if p.left:
            p_queue.append(p.left)
        if q.left:
            q_queue.append(q.left)
        if q.right:
            q_queue.append(q.right)

    if not p_queue and q_queue or p_queue and not q_queue:
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
