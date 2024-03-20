from data_structures.list_node import ListNode
from merge_between_linked_list import mergeInBetween

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    node1 = ListNode.fromList([10,1,13,6,9,5])
    node2 = ListNode.fromList([1000000,1000001,1000002])
    assert ListNode.toList(mergeInBetween(node1, 3, 4, node2)) == [10,1,13,1000000,1000001,1000002,5]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    node1 = ListNode.fromList([0,1,2,3,4,5,6])
    node2 = ListNode.fromList([1000000,1000001,1000002,1000003,1000004])
    assert ListNode.toList(mergeInBetween(node1, 2, 5, node2)) == [0,1,1000000,1000001,1000002,1000003,1000004,6]