from typing import List


def firstPalindrome(words: List[str]) -> str:
    for word in words:
        if isPalindrome(word):
            return word
    return ''


def isPalindrome(word: str) -> bool:
    length = len(word)
    n = (length//2)+1 if length%2 == 0 else round(length/2)+1
    for index in range(0, n):
        left = index
        right = length - 1 - index
        if word[left] != word[right]:
            return False
    return True