"""
https://en.wikipedia.org/wiki/Linked_list#Singly_linked_list

TODO: add sorting
TODO: add inserting into specified position
"""
from typing import Any, Union


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: Union[Node, None] = None

    def __str__(self):
        return f'{self.value} - {self.next}'


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

    def reverse(self):
        if self.head is None:
            return
        prev, curr = None, self.head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev

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

