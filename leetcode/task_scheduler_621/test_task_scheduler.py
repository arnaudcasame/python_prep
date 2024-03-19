from task_scheduler import leastInterval

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert leastInterval(["A","A","A","B","B","B"], 2) == 8

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert leastInterval(["A","C","A","B","D","B"], 1) == 6

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert leastInterval(["A","A","A", "B","B","B"], 3) == 10