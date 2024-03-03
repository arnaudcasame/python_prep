import pytest
from data_structures.list_node import ListNode
from remove_nth_node import removeNthFromEnd

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    node = ListNode.fromList([1,2,3,4,5])
    assert removeNthFromEnd(node, 2) == [1,2,3,5]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    node = ListNode.fromList([1])
    assert removeNthFromEnd(node, 1) == []

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    node = ListNode.fromList([1,2])
    assert removeNthFromEnd(node, 1) == [1]