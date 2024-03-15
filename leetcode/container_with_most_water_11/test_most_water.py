from most_water import maxArea
import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert maxArea([1,1]) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert maxArea([2,1]) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer4():
    assert maxArea([1,2]) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer5():
    assert maxArea([2, 3, 4, 5, 18, 17, 6]) == 17