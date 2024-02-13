from leetcode.find_first_palindrome_2108.first_palindrome import firstPalindrome

def test_answer1():
    assert firstPalindrome(["abc","car","ada","racecar","cool"]) == "ada"

def test_answer2():
    assert firstPalindrome(["notapalindrome","racecar"]) == "racecar"

def test_answer3():
    assert firstPalindrome(["def","ghi"]) == ""