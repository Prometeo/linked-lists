import pytest
from main import LinkedList


# ~> Fixtures
@pytest.fixture
def base_linked_list() -> LinkedList:
    return LinkedList(1)


# ~> Tests
def test_create_linked_list():
    value = 1
    linked_list = LinkedList(value)
    assert linked_list.length == 1
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1


def test_append_item(base_linked_list: LinkedList):
    value_1 = 2
    value_2 = 3
    base_linked_list.append(value_1)
    base_linked_list.append(value_2)
    assert base_linked_list.length == 3
    assert base_linked_list.head.next.value == value_1
    assert base_linked_list.tail.value == value_2
    assert base_linked_list.tail.next is None


def test_pop_one_item_list(base_linked_list: LinkedList):
    result = base_linked_list.pop()
    assert result == 1
    assert base_linked_list.length == 0


def test_pop_items(base_linked_list: LinkedList):
    base_linked_list = base_linked_list
    value_1 = 2
    value_2 = 3
    base_linked_list.append(value_1)
    base_linked_list.append(value_2)
    result_1 = base_linked_list.pop()
    result_2 = base_linked_list.pop()

    assert result_1 == value_2
    assert result_2 == value_1
    assert base_linked_list.length == 1


def test_pop_first_one_item_list(base_linked_list: LinkedList):
    result = base_linked_list.pop_first()
    assert base_linked_list.length == 0
    assert result == 1
    assert base_linked_list.head is None


def test_pop_first_item(base_linked_list: LinkedList):
    base_linked_list.append(2)
    base_linked_list.append(3)
    length = base_linked_list.length
    result = base_linked_list.pop_first()
    assert result == 1
    assert base_linked_list.length == length - 1
    assert base_linked_list.head.value == 2


def test_prepend_empty_list(base_linked_list: LinkedList):
    base_linked_list.pop()
    value = 2
    result = base_linked_list.prepend(value)
    assert result is True
    assert base_linked_list.head.value == 2
    assert base_linked_list.tail.value == 2


def test_preped_value(base_linked_list: LinkedList):
    value = 2
    result = base_linked_list.prepend(value)
    assert result is True
    assert base_linked_list.head.value == 2
    assert base_linked_list.head.next.value == 1


def test_get_item(base_linked_list: LinkedList):
    base_linked_list.append(2)
    base_linked_list.append(3)
    base_linked_list.append(4)
    node = base_linked_list.get_item(2)
    assert node.value == 3


def test_get_item_out_of_range(base_linked_list: LinkedList):
    node = base_linked_list.get_item(1)
    assert node is None


def test_insert_item(base_linked_list: LinkedList):
    base_linked_list.append(2)
    base_linked_list.append(3)
    base_linked_list.append(4)
    index = 2
    value = 5
    result = base_linked_list.insert_item(index, value)
    node = base_linked_list.get_item(index)
    assert result is True
    assert node.value == value
    assert node.next.value == 3
    assert base_linked_list.length == 5


def assert_insert_into_head(base_linked_list: LinkedList):
    base_linked_list.append(2)

    result = base_linked_list.insert_item(0, 3)
    assert result is True
    assert base_linked_list.head.value == 3
    assert base_linked_list.head.next.value == 1
    assert base_linked_list.length == 3
