from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    rightBucket = [1] * len(nums)
    leftBucket = [1] * len(nums)

    rProd = 1
    for i in range(len(nums)-2, -1, -1):
        rProd *= nums[i+1]
        rightBucket[i] = rProd

    lProd = 1
    for i in range(1, len(nums)):
        lProd *= nums[i-1]
        leftBucket[i] = lProd

    for i in range(0, len(nums)):
        nums[i] = leftBucket[i] * rightBucket[i]

    print(leftBucket, rightBucket, nums)
    return nums