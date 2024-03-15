from typing import List


def maxArea(height: List[int]) -> int:
    i, j = 0, len(height)-1
    area = 0
    while i < j:
        lesser = height[i] if height[i] < height[j] else height[j]
        area = max(area, lesser * (j-i))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return area