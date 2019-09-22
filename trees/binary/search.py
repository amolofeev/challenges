"""
https://en.wikipedia.org/wiki/Binary_search_tree

TODO: add deletion
"""

from typing import Any, Union, Tuple


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


if __name__ == '__main__':
    inputs = {
        '~= balanced': [5, 3, 1, 2, 0, 7, 6, 8, 9],
        'sorted': [0, 1, 2, 3, 4, 5],
        'reversed': [5, 4, 3, 2, 1, 0],
    }

    for label, lst in inputs.items():
        print(label, '-' * 20)
        b = BinarySearchTree()
        for key, value in zip(lst, lst):
            b.insert(key, value)
        for key, value in zip(lst, lst):
            node = b.search(key)
            assert node is not None
            assert node.value == node.key == value
            print(
                f'Key {key} for value {value} found in tree'
                f' and node.value == {node.value} at level {node.level}'
            )

        not_exists = 2.5
        node = b.search(not_exists)
        assert node is None
        print(f'Key {not_exists} doesn\'t found!')
