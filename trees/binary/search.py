"""
https://en.wikipedia.org/wiki/Binary_search_tree

TODO: add deletion
"""

from typing import Any, Union


class TreeNode:
    def __init__(self, key: Any, value: Any, level: int = 0):
        self.key = key
        self.value = value
        self.level = level
        self.left: Union[TreeNode, None] = None
        self.right: Union[TreeNode, None] = None

    def insert(self, key: Any, value: Any) -> None:
        """insert value by key into tree"""
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key, value, self.level + 1)
            else:
                self.left.insert(key, value)
        else:
            if self.right is None:
                self.right = TreeNode(key, value, self.level + 1)
            else:
                self.right.insert(key, value)

    def search(self, key: Any) -> Union['TreeNode', None]:
        """
        Search by key and return node or None.
        """
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        else:
            return None

    def height(self):
        lh = 0
        rh = 0
        if self.left:
            lh = self.left.height()
        if self.right:
            rh = self.right.height()
        return 1 + max(lh, rh)

    def is_balanced(self):
        lh = 0
        rh = 0
        if self.left:
            lh = self.left.height()
        if self.right:
            rh = self.right.height()

        return abs(lh - rh) <= 1


class BinarySearchTree:
    def __init__(self):
        self.root: Union[TreeNode, None] = None

    def insert(self, key: Any, value: Any) -> None:
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.root.insert(key, value)

    def search(self, key: Any) -> Union[TreeNode, None]:
        if self.root is None:
            return None
        return self.root.search(key)

    def height(self):
        if self.root is None:
            return 0
        return self.root.height()

    def is_balanced(self):
        if self.root is None:
            return True
        return self.root.is_balanced()
