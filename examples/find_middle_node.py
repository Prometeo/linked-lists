# Find the middle node, there is no length and you can loop over the list only once
class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node

    def append(self, value: int) -> None:
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node


def find_middle_node_1(linked_list: LinkedList) -> int:
    temp = linked_list.head
    values: list = []
    while temp:
        values.append(temp.value)
        temp = temp.next
    return values[len(values) // 2]


def find_middle_node_2(linked_list: LinkedList) -> int:
    slow: Node = linked_list.head
    fast: Node = linked_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value


def main():
    new_list: LinkedList = LinkedList(1)
    for i in range(2, 8):
        new_list.append(i)
    result_1: int = find_middle_node_1(new_list)
    print(result_1)
    result_2: int = find_middle_node_2(new_list)
    print(result_2)


if __name__ == "__main__":
    main()
