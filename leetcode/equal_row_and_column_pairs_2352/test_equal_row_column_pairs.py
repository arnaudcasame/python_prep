from equal_row_column_pairs import equalPairs
import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert equalPairs([3,2,1],[1,7,6],[2,7,7]) == 1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3