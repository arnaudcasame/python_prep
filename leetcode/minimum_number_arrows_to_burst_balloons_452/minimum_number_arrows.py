from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    result = len(points)
    points.sort()
    previous = points[0]

    for i in range(1, len(points)):
        current = points[i]

        if current[0] <= previous[1]:
            result -= 1
            previous = [current[0], min(current[1], previous[1])]
        else:
            previous = current

    return result