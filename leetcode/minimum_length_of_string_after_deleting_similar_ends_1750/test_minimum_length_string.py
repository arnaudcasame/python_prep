import pytest
from minimum_length_string import minimumLength

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert minimumLength('ca') == 2

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert minimumLength('cabaabac') == 0

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert minimumLength('aabccabba') == 3

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer4():
    assert minimumLength('abbbbbbbbbbbbbbbbbbba') == 0

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer5():
    assert minimumLength('bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb') == 1