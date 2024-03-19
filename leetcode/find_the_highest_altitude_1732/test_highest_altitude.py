from highest_altitude import largestAltitude

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert largestAltitude([-5,1,5,0,-7]) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert largestAltitude([-4,-3,-2,-1,4,3,2]) == 0