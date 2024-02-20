from typing import List

def missingNumber(nums: List[int]) -> int:
    bucket = {}
    for num in nums:
        bucket[num] = 1
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
    return nums[-1]+1

def missingNumberO(nums: List[int]) -> int:
        missing = 0
        for num in nums:
            missing ^= num
        for i in range(len(nums) + 1):
            missing ^= i
        return missing