import pytest
from leetcode.furthest_building_u_can_reach_1642.furthest_building import furthestBuilding


# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_1():
    assert furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_2():
    assert furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_3():
    assert furthestBuilding([14,3,19,3], 17, 0) == 3

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_4():
    assert furthestBuilding([3,19], 87, 1) == 1

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_5():
    assert furthestBuilding([1, 2], 0, 0) == 0

# @pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_6():
    assert furthestBuilding([1,5,1,2,3,4,10000], 4, 1) == 5