from is_subsequence import isSubsequence

import pytest

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert isSubsequence('abc', 'ahbgdc') == True

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert isSubsequence('axc', 'ahbgdc') == False