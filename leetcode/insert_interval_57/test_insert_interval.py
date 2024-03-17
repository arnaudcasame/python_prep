from insert_interval import insert
import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert insert([[1,3],[6,9]], [2, 5]) == [[1, 5], [6, 9]]

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]