class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        for every length we want the farthest greater or equal length. then we can just move the index of the smaller one, 
        
        """
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            left_val, right_val = height[left], height[right]
            area = min(left_val, right_val) * (right - left)
            max_area = max(area, max_area)
            
            if left_val < right_val:
                left += 1
            else:
                right -=1 
        return max_area