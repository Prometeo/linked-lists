# Remove dublicated nodes from the linked list


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length = 1

    def append(self, value: int) -> None:
        new_node: Node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def remove_duplicates(self) -> None:
        values: set = set()
        current: Node = self.head
        prev: Node | None = None
        while current:
            if current.value in values:
                prev.next = current.next
                current = current.next
            else:
                values.add(current.value)
                prev = current
                current = current.next
        self.print_linked_list()

    def print_linked_list(self) -> None:
        cur: Node = self.head
        while cur:
            print(cur.value)
            cur = cur.next


def main():
    linked_list: LinkedList = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(4)
    linked_list.append(2)
    linked_list.append(1)
    print("Initial Linked list:")
    linked_list.print_linked_list()
    print("Final Linked list:")
    linked_list.remove_duplicates()


if __name__ == "__main__":
    main()
