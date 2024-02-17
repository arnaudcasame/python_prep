from leetcode.least_number_unique_integers_after_k_removals_1481.least_num_of_unique_ints import findLeastNumOfUniqueInts
import pytest


@pytest.mark.skip('Unskip only to test solution')
def test_answer_1():
    assert findLeastNumOfUniqueInts([5, 5, 4], 1) == 1
@pytest.mark.skip('Unskip only to test solution')
def test_answer_2():
    assert findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 2) == 2
@pytest.mark.skip('Unskip only to test solution')
def test_answer_3():
    assert findLeastNumOfUniqueInts([1], 1) == 0
@pytest.mark.skip('Unskip only to test solution')
def test_answer_4():
    assert findLeastNumOfUniqueInts([2, 1, 1, 3, 3, 3], 3) == 1
@pytest.mark.skip('Unskip only to test solution')
def test_answer_5():
    assert findLeastNumOfUniqueInts([2, 4, 1, 8, 3, 5, 1, 3], 3) == 3
