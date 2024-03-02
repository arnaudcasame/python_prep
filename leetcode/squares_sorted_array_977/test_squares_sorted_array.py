import pytest
from squares_sorted_array import sortedSquares


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]