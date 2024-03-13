from data_structures.list_node import ListNode
from remove_zero_sum_consecutive_nodes_in_linked_list import removeZeroSumSublists

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    head = ListNode.fromList([1,2,-3,3,1])
    result = removeZeroSumSublists(head)
    assert ListNode.toList(result) == [3,1]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    head = ListNode.fromList([1,2,3,-3,4])
    result = removeZeroSumSublists(head)
    assert ListNode.toList(result) == [1,2,4]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    head = ListNode.fromList([1,2,3,-3,-2])
    result = removeZeroSumSublists(head)
    assert ListNode.toList(result) == [1]