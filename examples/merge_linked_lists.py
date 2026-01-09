class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def append(self, value: int) -> None:
        new_node: Node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self) -> None:
        temp: Node = self.head
        while temp:
            print(temp.value)
            temp = temp.next


def merge_lists(list1: LinkedList, list2: LinkedList) -> None:
    temp1: Node = list1.head
    temp2: Node = list2.head

    new_list: LinkedList = LinkedList()

    while temp1 and temp2:
        if temp1.value <= temp2.value:
            new_list.append(temp1.value)
            new_list.append(temp2.value)
        else:
            new_list.append(temp2.value)
            new_list.append(temp1.value)
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1:
        while temp1:
            new_list.append(temp1.value)
    if temp2:
        while temp1:
            new_list.append(temp2.value)
    return new_list


def main() -> None:
    list1: LinkedList = LinkedList()
    list2: LinkedList = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(4)
    list2.append(2)
    list2.append(3)
    list2.append(4)
    merge_lists(list1, list2)


if __name__ == "__main__":
    main()
