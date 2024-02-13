import pytest
from leetcode.find_first_palindrome_2108.first_palindrome import firstPalindrome

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert firstPalindrome(["abc","car","ada","racecar","cool"]) == "ada"

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert firstPalindrome(["notapalindrome","racecar"]) == "racecar"

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert firstPalindrome(["def","ghi"]) == ""