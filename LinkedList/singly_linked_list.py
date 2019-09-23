"""
https://en.wikipedia.org/wiki/Linked_list#Singly_linked_list

TODO: add reverse
TODO: add deletion
TODO: add sorting
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

    ll = SinglyLinkedList()
    for i in range(5):
        ll.push_back(i)

    with ExceptionRaised(IndexError) as e:
        index_error = ll[15]

    assert list(ll.generator()) == list(range(5))

    for i in range(5):
        assert ll[i] == i

    for default, actual in map(lambda x: (x, ll.pop_head()), range(5)):
        assert default == actual
    assert ll.pop_head() is None
