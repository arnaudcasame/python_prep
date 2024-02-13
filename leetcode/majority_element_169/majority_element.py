from typing import List

def majority_element(nums: List[int])->int:
    item, majority = 0, 0
    for num in nums:
        if majority == 0:
            item = num
        majority += 1 if num == item else -1
    return item