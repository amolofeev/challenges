"""
https://en.wikipedia.org/wiki/Linked_list#Singly_linked_list

TODO: add reverse
TODO: add sorting
TODO: add inserting into specified position
"""
from typing import Any, Union


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Union[Node, None] = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value: Any) -> None:
        """Add item in the end of list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_head(self) -> Any:
        """Pop head item == Queue"""
        if self.head is not None:
            head = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return head.value

    def generator(self):
        """Iterate over list from head to tail"""
        if self.head is None:
            yield from ()
        else:
            current = self.head
            yield current.value
            while current.next:
                current = current.next
                yield current.value

    def delete(self, index: int):
        if not isinstance(index, int):
            raise TypeError(f'index must be int, {type(index)} found')
        if index < 0:
            raise ValueError('index must be >= 0')

        if self.head is None:
            raise IndexError('Head is none')

        if index == 0:
            self.pop_head()
        else:
            n = 0
            prev = None
            curr = self.head
            while curr.next and n < index:
                prev = curr
                curr = curr.next
                n += 1

            if n == index:
                prev.next = curr.next
            else:
                raise IndexError

    def __getitem__(self, index: int) -> Any:
        if self.head is None:
            raise IndexError

        n = 0
        curr = self.head
        while curr.next and n < index:
            curr = curr.next
            n += 1
        if n == index:
            return curr.value
        raise IndexError

    def __bool__(self):
        return self.head is not None


if __name__ == '__main__':
    from python.std.context_manager import ExceptionRaised


    def make_sll(n=5):
        sll = SinglyLinkedList()
        for i in range(n):
            sll.push_back(i)
        return sll


    sll = make_sll()

    with ExceptionRaised(IndexError) as e:
        index_error = sll[15]

    assert list(sll.generator()) == list(range(5))

    for i in range(5):
        assert sll[i] == i

    for default, actual in map(lambda x: (x, sll.pop_head()), range(5)):
        assert default == actual
    assert sll.pop_head() is None

    # test deletions
    sll = make_sll()
    sll.delete(0)
    sll.delete(1)
    assert list(sll.generator()) == [1, 3, 4]

    with ExceptionRaised(IndexError):
        sll.delete(5)
    with ExceptionRaised(ValueError):
        sll.delete(-1)
    with ExceptionRaised(TypeError):
        sll.delete('1')
    with ExceptionRaised(IndexError):
        SinglyLinkedList().delete(1)
