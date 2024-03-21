from two_strings_are_close import closeStrings

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert closeStrings('abc', 'bca') == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert closeStrings('a', 'aa') == False

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert closeStrings('cabbba', 'abbccc') == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer4():
    assert closeStrings('asdefgfw', 'deaffgws') == True