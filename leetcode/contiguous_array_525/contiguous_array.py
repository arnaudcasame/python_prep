from typing import List


def findMaxLength(nums: List[int]) -> int:
    o, z = 0, 0
    bucket = {}
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            z += 1
        else:
            o += 1
        
        if (o-z) not in bucket:
            bucket[o-z] = i
        
        if o == z:
            count = o + z
        else:
            index = bucket[o-z]
            count = max(count, i - index)
    return count