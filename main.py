from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length = 1

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def pop(self) -> int | None:
        if self.head is None and self.tail is None:
            return None
        if self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            result = temp.value
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return result

    def pop_first(self) -> int | None:
        if self.head is None:
            return None

        if self.head == self.tail:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            result = self.head.value
            self.head = self.head.next

        self.length -= 1

        return result

    def prepend(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def get_item(self, index: int) -> Node | None:
        if index < 0 or index > self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def insert_item(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.get_item(index - 1)
            new_node.next = node.next
            node.next = new_node
        self.length += 1
        return True
