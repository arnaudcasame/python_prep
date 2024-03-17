from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0

    while i < len(intervals):
        if newInterval[1] < intervals[i][0]:
            break
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        i += 1
    
    result.append(newInterval)

    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result
