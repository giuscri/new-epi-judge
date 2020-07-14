from typing import List, Optional, Tuple
from math import sqrt, isclose
from functools import total_ordering

from test_framework import generic_test

class V:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

class BSTNode:
    def __init__(self, v=V(a=0, b=0)):
        self.v: V = v
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    @property
    def k(self) -> float:
        return self.v.a + self.v.b * sqrt(2)

    @property
    def height(self) -> int:
        lh = self.left.height if self.left is not None else -1
        rh = self.right.height if self.right is not None else -1
        return max(lh, rh) + 1

    @property
    def balanced(self) -> bool:
        lh = self.left.height if self.left is not None else -1
        rh = self.right.height if self.right is not None else -1
        return abs(lh - rh) <= 1

    def __repr__(self) -> str:
        return f"({self.k}, ({self.v.a}, {self.v.b}))"

def right_rotate(x: BSTNode) -> BSTNode:
    y = x.left
    if y is None:
        raise RuntimeError("left subtree must be not None")

    x.left = y.right
    y.right = x
    return y

def left_rotate(y: BSTNode) -> BSTNode:
    x = y.right
    if x is None:
        raise RuntimeError("right subtree must be not None")

    y.right = x.left
    x.left = y
    return x

def insert(tree: Optional[BSTNode], node: BSTNode) -> BSTNode:
    if tree is None:
        return node

    if isclose(node.k, tree.k):
        return tree
    elif node.k < tree.k:
        tree.left = insert(tree.left, node)
        if not tree.balanced and tree.left is not None and node.k < tree.left.k: # left-left case
            tree = right_rotate(tree)
            assert tree.balanced
        elif not tree.balanced and tree.left is not None and node.k > tree.left.k: # left-right case
            tree.left = left_rotate(tree.left)
            assert tree.left.balanced
            tree = right_rotate(tree)
            assert tree.balanced
        return tree
    else: # node.k > tree.k
        tree.right = insert(tree.right, node)
        if not tree.balanced and tree.right is not None and node.k > tree.right.k: # right-right case
            tree = left_rotate(tree)
            assert tree.balanced
        elif not tree.balanced and tree.right is not None and node.k < tree.right.k: # right-left case
            tree.right = right_rotate(tree.right)
            tree = left_rotate(tree)
            assert tree.balanced
        return tree

def delete(tree: Optional[BSTNode], k: float) -> Optional[BSTNode]:
    if tree is None:
        return tree

    if isclose(k, tree.k):
        if tree.left is None and tree.right is None:
            tree = None
        elif tree.left is not None and tree.right is None: # one child
            tree = tree.left
        elif tree.left is None and tree.right is not None: # one child
            tree = tree.right
        else: # two children: return inorder successor
            prev = None
            ptr = tree.right
            while ptr.left is not None:
                prev = ptr
                ptr = ptr.left

            assert ptr is not None
            tree.v = ptr.v
            prev.left = None
    elif k < tree.k:
        tree.left = delete(tree.left, k)
    else: # k > tree.k
        tree.right = delete(tree.right, k)

    if tree is None: # we had only the node we deleted
        return None

    if tree.balanced:
        return tree

    z = tree
    assert z.left is not None or z.right is not None
    if z.left is None or z.right.height > z.left.height:
        y = z.right
        if y.left is None or y.right is not None and y.right.height > y.left.height: # right-right
            z = left_rotate(z)
        else: # right-left
            z.right = right_rotate(z.right)
            z = left_rotate(z)
    elif z.right is None or z.left.height > z.right.height:
        y = z.left
        if y.right is None or y.left is not None and y.left.height > y.right.height: # left-left
            z = right_rotate(z)
        else: # left-right
            z.left = left_rotate(z.left)
            z = right_rotate(z)
    else:
        assert False

    tree = z
    return tree

def pop_minimum(tree: Optional[BSTNode]) -> Tuple[Optional[BSTNode], Optional[BSTNode]]:
    if tree is None:
        return (None, None)

    ptr = tree
    while ptr.left is not None:
        ptr = ptr.left

    tree = delete(tree, ptr.k)
    return (tree, ptr)

def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    tree: BSTNode = BSTNode(v=V(a=0, b=0))
    r: List[float] = []
    for _ in range(k):
        assert tree is not None
        tree, node = pop_minimum(tree)
        r.append(node.k)
        n1 = BSTNode(V(node.v.a+1, node.v.b))
        n2 = BSTNode(V(node.v.a, node.v.b+1))
        tree = insert(tree, n1)
        tree = insert(tree, n2)

    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
