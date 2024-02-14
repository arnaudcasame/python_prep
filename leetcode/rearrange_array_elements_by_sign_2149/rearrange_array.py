from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
    bucket = []
    p, n = 0, 1
    for i in range(0, len(nums)):
        num = nums[i]
        if num < 0:
            bucket.insert(n, num)
            n += 2
        else:
            bucket.insert(p, num)
            p += 2
    return bucket