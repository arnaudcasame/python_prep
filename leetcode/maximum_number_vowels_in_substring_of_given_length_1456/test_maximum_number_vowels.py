from maximum_number_vowels import maxVowels

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert maxVowels('abciiidef', 3) == 3

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert maxVowels('aeiou', 2) == 2

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert maxVowels('leetcode', 3) == 2