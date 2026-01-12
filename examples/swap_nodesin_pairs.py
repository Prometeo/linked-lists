# swap values of each pair elements of a given linked list
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


def print_list(head) -> None:
    temp: Node = head
    while temp:
        print(temp.value)
        temp = temp.next


def swap_pairs(head: Node) -> None:
    temp: Node = head
    while temp and temp.next:
        temp.value, temp.next.value = temp.next.value, temp.value

        temp = temp.next.next


def main():
    head: Node = Node(1)
    head.next: Node = Node(2)
    head.next.next: Node = Node(3)
    head.next.next.next: Node = Node(4)
    head.next.next.next.next: Node = Node(5)
    head.next.next.next.next.next: Node = Node(6)
    head.next.next.next.next.next.next: Node = Node(7)
    head.next.next.next.next.next.next.next: Node = Node(8)
    print("Initial List")
    print_list(head)
    print("List result")
    swap_pairs(head)
    print_list(head)


if __name__ == "__main__":
    main()
