from minimum_number_arrows import findMinArrowShots

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]) == 2