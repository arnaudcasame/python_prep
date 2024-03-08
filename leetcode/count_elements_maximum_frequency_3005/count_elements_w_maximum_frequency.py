from typing import List

def maxFrequencyElements(nums: List[int]) -> int:
    bucket = {}
    for num in nums:
        bucket[num] = 1 if num not in bucket else bucket[num] + 1
    # print(bucket)
    lastFreq = 0
    count = 0
    for key in bucket:
        if lastFreq < bucket[key]:
            lastFreq = bucket[key]
            count = 0
            count += bucket[key]
        elif lastFreq == bucket[key]:
            count += bucket[key]
    return count