# Determine if the linked list has a loop
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length: int = 1

    def append(self, value: int) -> None:
        new_node: Node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def has_loop(self) -> bool:
        slow: Node = self.head
        fast: Node = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False


def main():
    linked_list: LinkedList = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.tail.next = linked_list.head
    print(linked_list.has_loop())


if __name__ == "__main__":
    main()
