class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        whenever we are asked for two points or some target and a list of sth we should use two pointers
        
        for this question what we can do is have two pointers at each end and the smaller one moves further till we find the sweet spot?
        
        solution:
        have a left and right
        total = right - left * min(nums[left], right)
        whenever left <= right
        move left
        else move right
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left <= right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
        