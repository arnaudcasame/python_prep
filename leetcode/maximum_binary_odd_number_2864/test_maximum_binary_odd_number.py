import pytest
from maximum_binary_odd_number import maximumOddBinaryNumber

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert maximumOddBinaryNumber('010') == '001'

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert maximumOddBinaryNumber('0101') == '1001'

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert maximumOddBinaryNumber('1') == '1'