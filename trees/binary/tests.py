from unittest import TestCase
from trees.binary.search import BinarySearchTree

BALANCED = [5, 3, 1, 2, 0, 7, 6, 8, 9]
SORTED = [0, 1, 2, 3, 4, 5]
REVERSED = [5, 4, 3, 2, 1, 0]


class BinarySearchTreeTestCase(TestCase):
    def setUp(self) -> None:
        self.balanced = BinarySearchTree()
        for k, v in zip(BALANCED, BALANCED):
            self.balanced.insert(k, v)

        self.sorted = BinarySearchTree()
        for k, v in zip(SORTED, SORTED):
            self.sorted.insert(k, v)

        self.reversed = BinarySearchTree()
        for k, v in zip(REVERSED, REVERSED):
            self.reversed.insert(k, v)

    def test_balanced(self):
        self.assertTrue(self.balanced.is_balanced())
        self.assertLess(
            self.balanced.height(),
            len(BALANCED)
        )

    def test_sorted(self):
        self.assertFalse(self.sorted.is_balanced())
        self.assertEqual(
            self.sorted.height(),
            len(SORTED)
        )

    def test_reversed(self):
        self.assertFalse(self.reversed.is_balanced())
        self.assertEqual(
            self.reversed.height(),
            len(REVERSED)
        )

    def test_search_balanced(self):
        for i in BALANCED:
            node = self.balanced.search(i)
            self.assertEqual(node.key, node.value, i)

    def test_search_sorted(self):
        for i in SORTED:
            node = self.sorted.search(i)
            self.assertEqual(node.key, node.value, i)

    def test_search_reversed(self):
        for i in REVERSED:
            node = self.reversed.search(i)
            self.assertEqual(node.key, node.value, i)

    def test_search_does_not_exists(self):
        self.assertIsNone(
            self.balanced.search(-12)
        )
        self.assertIsNone(
            self.balanced.search(50)
        )
        self.assertIsNone(
            self.balanced.search(3.5)
        )
