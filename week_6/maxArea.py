class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        
        max_area = 0
        while p2 > p1:
            minim = min(height[p1],height[p2])
            max_area = max(max_area, minim *(p2 - p1))
            
            if height[p1] == minim :
                p1 += 1
            else:
                p2 -= 1
        return max_area
        