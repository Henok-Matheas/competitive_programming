class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        right = -float("inf")
        points.sort()
        
        for start, end in points:
            if start > right:
                count += 1
                right = end
            right = min(right, end)
        
        return count
                