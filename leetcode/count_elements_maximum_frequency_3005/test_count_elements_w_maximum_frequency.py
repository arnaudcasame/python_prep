from count_elements_w_maximum_frequency import maxFrequencyElements
import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert maxFrequencyElements([1,2,2,3,1,4]) == 4

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert maxFrequencyElements([1,2,3,4,5]) == 5
