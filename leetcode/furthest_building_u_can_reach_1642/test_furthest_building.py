import pytest
from leetcode.furthest_building_u_can_reach_1642.furthest_building import furthestBuilding


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_1():
    assert furthestBuilding([4,2,7,6,9,14,12], 5, 1) == 4

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_2():
    assert furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2) == 7

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer_3():
    assert furthestBuilding([14,3,19,3], 17, 0) == 3
