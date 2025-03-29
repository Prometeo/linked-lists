import pytest
from linked_list import LinkedList


# ~> Fixtures
@pytest.fixture
def base_linked_list() -> LinkedList:
    linked_list = LinkedList(1)
    return linked_list


# ~>  Tests
def test_create_linked_list():
    value = 1
    linked_list = LinkedList(value)
    assert linked_list.length == 1
    assert linked_list.head.value == value
    assert linked_list.tail.value == value


def test_append_item(base_linked_list: LinkedList):
    value_1 = 2
    value_2 = 3
    base_linked_list.append(value_1)
    base_linked_list.append(value_2)
    assert base_linked_list.length == 3
    assert base_linked_list.head.next.value == value_1  # type: ignore
    assert base_linked_list.tail.value == value_2
    assert base_linked_list.head.next.next.value == value_2  # type: ignore
    assert base_linked_list.tail.next is None


def test_pop_item(base_linked_list: LinkedList):
    base_linked_list.append(2)
    base_linked_list.append(3)
    assert base_linked_list.pop() == 3
    assert base_linked_list.tail.value == 2
    assert base_linked_list.length == 2


def test_pop_only_item():
    linked_list = LinkedList(1)
    assert linked_list.pop() == 1
    assert linked_list.length == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_first(base_linked_list):
    base_linked_list.append(2)
    base_linked_list.append(3)
    item = base_linked_list.pop_first()
    assert item == 1
    assert base_linked_list.head.value == 2
    assert base_linked_list.tail.value == 3
    assert base_linked_list.length == 2


def test_single_first(base_linked_list):
    item = base_linked_list.pop_first()
    assert item == 1
    assert base_linked_list.head is None
    assert base_linked_list.tail is None
    assert base_linked_list.length == 0


def test_get_item(base_linked_list):
    base_linked_list.append(2)
    base_linked_list.append(3)
    base_linked_list.append(4)
    item_1 = base_linked_list.get_item(2)
    item_2 = base_linked_list.get_item(3)
    item_3 = base_linked_list.get_item(30)

    assert item_1.value == 3
    assert item_2.value == 4
    assert item_3 is None


def test_insert(base_linked_list):
    base_linked_list.append(2)
    base_linked_list.append(3)
    base_linked_list.append(4)
    base_linked_list.insert_item(9, 2)
    assert base_linked_list.get_item(2).value == 9
    assert base_linked_list.get_item(3).value == 3
    assert base_linked_list.length == 5


def test_prepend(base_linked_list):
    base_linked_list.prepend(5)
    assert base_linked_list.head.value == 5
    assert base_linked_list.head.next.value == 1
    assert base_linked_list.length == 2


def test_prepend_empty_linked_list(base_linked_list):
    base_linked_list.pop()
    base_linked_list.prepend(9)
    assert base_linked_list.length == 1
    assert base_linked_list.head.value == 9
    assert base_linked_list.tail.value == 9


def test_remove(base_linked_list):
    base_linked_list.append(2)
    base_linked_list.append(3)
    base_linked_list.append(4)
    assert base_linked_list.remove_item(2)
    assert base_linked_list.length == 3
    assert base_linked_list.get_item(2).value == 4
