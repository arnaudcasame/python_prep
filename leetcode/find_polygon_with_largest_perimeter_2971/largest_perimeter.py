from typing import List


def largestPerimeter(nums: List[int]) -> int:
    nums = sorted(nums)
    sum, longestSide, maxNum = 0, 0, -1
    for num in nums:
        sum += num
    for i in range(len(nums)-1, -1, -1):
        longestSide = nums[i]
        sum = sum - longestSide
        if sum > longestSide:
            maxNum = max(maxNum, sum + longestSide)
    return maxNum