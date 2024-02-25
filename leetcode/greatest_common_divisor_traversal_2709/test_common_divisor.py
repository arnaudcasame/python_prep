import pytest
from leetcode.greatest_common_divisor_traversal_2709.common_divisor import canTraverseAllPairs


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_1():
    assert canTraverseAllPairs([2,3,6]) == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_2():
    assert canTraverseAllPairs([3,9,5]) == False

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_3():
    assert canTraverseAllPairs([4,3,12,8]) == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_4():
    assert canTraverseAllPairs([28,39]) == False

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_5():
    assert canTraverseAllPairs([21,88,75]) == False

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_6():
    assert canTraverseAllPairs([10]) == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_7():
    assert canTraverseAllPairs([1,1]) == False