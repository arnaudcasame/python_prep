from find_pivot_integer import pivotInteger

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert pivotInteger(8) == 6

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert pivotInteger(1) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert pivotInteger(4) == -1