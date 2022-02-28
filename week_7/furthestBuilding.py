# [4,2,7,6,9,14,12]
# 5
# 1
# [1,5,1,2,3,4,10000]
# 4
# 1
import heapq


class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int,
                         ladders: int) -> int:
        count = 0
        brcks = []
        i = 0
        while i < len(heights) - 1:
            climb = heights[i + 1] - heights[i]
            if climb <= 0:
                i += 1

            elif climb - bricks > 0 and ladders > 0:
                ladder_before = (-1 * brcks[0]) if brcks else 0

                if climb <= ladder_before:
                    bricks += -1 * heapq.heappop(brcks) if brcks else 0
                    ladders -= 1
                else:
                    ladders -= 1
                    i += 1

            elif climb - bricks <= 0:
                bricks -= climb
                heapq.heappush(brcks, -1 * climb)
                i += 1

            else:
                return i
        return i
