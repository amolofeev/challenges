"""
https://en.wikipedia.org/wiki/Binary_tree

Binary tree is a tree-like data structure with 1 and only 1 rule:
- each node mustn't have more than 2 children.

I have no idea how to use it and where would it be needed=)
"""
from typing import Any, Union


class BinaryTreeNone:
    """
    This class implements just base requirements for binary tree without any functions to work with
    """

    def __init__(self, data: Any):
        self.data = data
        self.left: Union[BinaryTreeNone, None] = None
        self.right: Union[BinaryTreeNone, None] = None
