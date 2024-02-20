import pytest
from leetcode.missing_number_268.missing_number import missingNumber

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert missingNumber([3,0,1]) == 2

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert missingNumber([0,1]) == 2

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8