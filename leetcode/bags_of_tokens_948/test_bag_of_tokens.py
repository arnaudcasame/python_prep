import pytest
from bag_of_tokens import bagOfTokensScore


@pytest.mark.skip('Unskip only for testing solution')
def test_answer1():
    assert bagOfTokensScore([100], 50) == 0

@pytest.mark.skip('Unskip only for testing solution')
def test_answer2():
    assert bagOfTokensScore([200,100], 150) == 1

@pytest.mark.skip('Unskip only for testing solution')
def test_answer3():
    assert bagOfTokensScore([100,200,300,400], 200) == 2