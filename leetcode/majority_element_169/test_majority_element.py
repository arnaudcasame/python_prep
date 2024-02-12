
from leetcode.majority_element_169 import majority_element as leet


def test_answer1():
    assert leet.majority_element([3,2,3]) == 3

def test_answer2():
    assert leet.majority_element([2,2,1,1,1,2,2]) == 2