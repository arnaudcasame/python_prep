import pytest

from diameter_binary_tree import diameterOfBinaryTree

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert diameterOfBinaryTree([1,2,3,4,5]) == 3

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert diameterOfBinaryTree([1,2]) == 1