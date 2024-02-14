import pytest
from rearrange_array import rearrangeArray

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert rearrangeArray([3,1,-2,-5,2,-4]) == [3,-2,1,-5,2,-4]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert rearrangeArray([-1,1]) == [1,-1]