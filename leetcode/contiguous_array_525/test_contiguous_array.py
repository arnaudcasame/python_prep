from contiguous_array import findMaxLength
import pytest

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert findMaxLength([0, 1]) == 2

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert findMaxLength([0, 1, 0]) == 2
