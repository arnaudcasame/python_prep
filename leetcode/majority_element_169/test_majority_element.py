import pytest
from leetcode.majority_element_169.majority_element import majority_element

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert majority_element([3,2,3]) == 3

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert majority_element([2,2,1,1,1,2,2]) == 2