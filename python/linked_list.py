from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self, value: int):
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length = 1

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> int | None:
        if self.head and self.tail is None:
            return None
        pre = self.head
        temp = self.head
        result: int | None = None
        if self.length == 1 and self.head:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            result = temp.value
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return result

    def pop_first(self) -> int | None:
        if self.head and self.tail is None:
            return None
        result: int | None = None
        if self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            result = self.head.value
            self.head = self.head.next
        self.length -= 1
        return result

    def get_item(self, index: int) -> Node | None:
        if index < 0 or index > self.length:
            return None
        temp: Node = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert_item(self, value: int, index: int) -> bool:
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        temp: Node = self.get_item(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
