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
