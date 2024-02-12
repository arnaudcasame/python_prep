def majority_element(nums: list):
    bucket = dict()
    majority = 0
    for num in nums:
        if num in bucket:
            bucket[num] = bucket[num] + 1
        else:
            bucket[num] = 1
        if bucket.get(num) > len(nums)//2:
            majority = num
    return majority