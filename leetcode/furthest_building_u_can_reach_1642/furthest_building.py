import heapq
from typing import List

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(0, len(heights)-1):
        if heights[i+1] - heights[i] <= 0:
            continue
        bricks -= heights[i+1] - heights[i]
        heapq.heappush(heap, -(heights[i+1] - heights[i]))

        if bricks < 0:
            if ladders == 0:
                return i
            ladders -= 1
            bricks += -heapq.heappop(heap)
    return len(heights) - 1