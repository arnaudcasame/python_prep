import pytest
from bitwise_and_numbers import rangeBitwiseAnd


# @pytest.mark.skip('Unskip only for testing solution')
def test_answer1():
    assert rangeBitwiseAnd(5, 7) == 4

# @pytest.mark.skip('Unskip only for testing solution')
def test_answer2():
    assert rangeBitwiseAnd(0, 0) == 0

# @pytest.mark.skip('Unskip only for testing solution')
def test_answer3():
    assert rangeBitwiseAnd(1, 2147483647) == 0