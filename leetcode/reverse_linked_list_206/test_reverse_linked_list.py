from data_structures.list_node import ListNode
from reverse_linked_list import reverseList

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    node = ListNode.fromList([1,2,3,4,5])
    assert ListNode.toList(reverseList(node)) == [5,4,3,2,1]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    node = ListNode.fromList([1,2])
    assert ListNode.toList(reverseList(node)) == [2,1]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    node = ListNode.fromList([])
    assert ListNode.toList(reverseList(node)) == []