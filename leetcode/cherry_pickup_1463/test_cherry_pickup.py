import pytest
from cherry_pickup import cherryPickup

@pytest.mark.skip('Unskip only for testing solution')
def test_answer1():
    assert cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]) == 24

@pytest.mark.skip('Unskip only for testing solution')
def test_answer2():
    assert cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]) == 28