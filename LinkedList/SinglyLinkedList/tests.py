from unittest import TestCase, skip
from .singly_linked_list import SinglyLinkedList


def make_sll(n=5):
    sll = SinglyLinkedList()
    for i in range(n):
        sll.push_back(i)
    return sll


class SLLTestCase(TestCase):
    def setUp(self) -> None:
        self.sll = make_sll()

    def test_get_item_by_index(self):
        for i in range(5):
            self.assertEqual(
                self.sll[i],
                i
            )

    def test_get_item_by_wrong_index(self):
        with self.assertRaises(IndexError):
            index_error = self.sll[15]

    def test_generator(self):
        self.assertEqual(
            list(self.sll.generator()),
            list(range(5))
        )

    def test_queue_interface(self):
        test_data = map(lambda x: (x, self.sll.pop_head()), range(5))
        for default, actual in test_data:
            self.assertEqual(default, actual)

    def test_queue_interface_for_empty_list(self):
        sll = SinglyLinkedList()
        self.assertIsNone(sll.pop_head())

    def test_delete_by_index(self):
        self.sll.delete(0)
        self.sll.delete(1)
        self.assertEqual(
            list(self.sll.generator()),
            [1, 3, 4]
        )

    def test_delete_by_wrong_index(self):
        with self.assertRaises(IndexError):
            self.sll.delete(5)
        with self.assertRaises(ValueError):
            self.sll.delete(-1)
        with self.assertRaises(TypeError):
            self.sll.delete('1')
        with self.assertRaises(IndexError):
            SinglyLinkedList().delete(1)

    def test_reverse(self):
        self.sll.reverse()
        self.assertEqual(
            list(self.sll.generator()),
            list(range(5))[::-1]
        )

    @skip('not implemented')
    def test_sorting_asc(self):
        self.sll.sort()
        self.assertEqual(
            list(self.sll.generator()),
            list(range(5))
        )

    @skip('not implemented')
    def test_sorting_desc(self):
        self.sll.sort(reversed=True)
        self.assertEqual(
            list(self.sll.generator()),
            list(range(5))[::-1]
        )
