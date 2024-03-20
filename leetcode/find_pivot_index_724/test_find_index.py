from find_index import pivotIndex
import pytest


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert pivotIndex([1,7,3,6,5,6]) == 3

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert pivotIndex([1,2,3]) == -1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert pivotIndex([2,1,-1]) == 0