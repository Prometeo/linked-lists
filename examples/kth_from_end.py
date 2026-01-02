# Find the kth node starting from the end, there is no length property


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: None | Node = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node

    def append(self, value: int) -> None:
        new_node: Node = Node(value)
        self.tail.next = new_node
        self.tail = new_node


def kth_element(linked_list: LinkedList, k: int) -> int | None:
    slow: Node = linked_list.head
    fast: Node = linked_list.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    return slow.value


def main() -> None:
    linked_list: LinkedList = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    result = kth_element(linked_list, 3)
    print(result)


if __name__ == "__main__":
    main()
