"""
Given a binary tree A, invert the binary tree and return it.

Inverting refers to making the left child the right child and vice versa.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(node):

    if node is None:
        return
    else:
        temp = node.left
        node.left = node.right
        node.right = temp
        preorder(node.left)
        preorder(node.right)
        return