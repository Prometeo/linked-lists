# The node to be deleted is in the list and is not a tail node.
# The value of each node in the list is unique.


class Node:
    def __init__(self, x) -> None:
        self.value = x
        self.next = None


def delete_node(head: Node, value: int) -> None:
    slow: Node = head
    fast: Node = head
    if not fast.next:
        head = None
        return None
    if slow.value == value:
        head = None
        return None

    while fast:
        fast = fast.next
        if fast.value == value:
            slow.next = fast.next
            fast = None
            return None
        slow = slow.next


def print_list(head: Node) -> None:
    temp: Node = head
    while temp:
        print(temp.value)
        temp = temp.next


def main():
    head: Node = Node(4)
    head.next = Node(5)
    head.next.next = Node(1)
    head.next.next.next = Node(9)
    delete_node(head, 5)
    print_list(head)


if __name__ == "__main__":
    main()
