from product_of_array import productExceptSelf
import pytest

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert productExceptSelf([0, 0]) == [0, 0]

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer4():
    assert productExceptSelf([0, 4, 0]) == [0, 0, 0]

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer5():
    assert productExceptSelf([1, 0]) == [0, 1]