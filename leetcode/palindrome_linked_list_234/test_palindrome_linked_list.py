from data_structures.list_node import ListNode
from palindrome_linked_list import isPalindrome

import pytest


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    node = ListNode.fromList([1,2,2,1])
    assert isPalindrome(node) == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    node = ListNode.fromList([1,2])
    assert isPalindrome(node) == False