class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i - 1]:
                diff = heights[i] - heights[i - 1]
                heapq.heappush(heap, diff)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    return i - 1
        return len(heights) - 1

"""
Find every upward climb and store its height difference.
If climbs exceed ladders, use bricks for the smallest climb and save ladders for bigger climbs.
If bricks become negative, stop. The previous building is the furthest you can reach.
"""