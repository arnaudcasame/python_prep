import pytest
from leetcode.find_polygon_with_largest_perimeter_2971.largest_perimeter import largestPerimeter


@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer1():
    assert largestPerimeter([5,5,5]) == 15

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer2():
    assert largestPerimeter([1,12,1,2,5,50,3]) == 12

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer3():
    assert largestPerimeter([5,5,50]) == -1

@pytest.mark.skip(reason='Unskip only to test solution')
def test_answer4():
    longestInput = [300005055, 352368231, 311935527, 315829776, 327065463, 388851949, 319541150, 397875604, 311309167, 391897750, 366860048, 359976490, 325522439, 390648914, 359891976, 369105322, 350430086, 398592583, 354559219, 372400239, 344759294, 379931363, 308829137, 335032174, 336962933, 380797651, 378305476, 336617902, 393487098, 301391791, 394314232, 387440261, 316040738, 388074503, 396614889, 331609633, 374723367, 380418460, 349845809, 318514711, 308782485, 308291996, 375362898, 397542455, 397628325, 392446446, 368662132, 378781533, 372327607, 378737987]
    assert largestPerimeter(longestInput) == 17876942274