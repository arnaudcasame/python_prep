from minimum_common_value import getCommon
import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert getCommon([1,2,3], [2,4]) == 2

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert getCommon([1,2,3,6], [2,3,4,5]) == 2