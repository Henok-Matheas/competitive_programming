class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # [3, 2]6
        ## if first < second pop first
        ## if current < previous
        """
        while the current is less than the previous and it has can remove elements it will
        """
        stack = []
        
        for idx, num in enumerate(nums):
            while stack and len(stack) - 1 + (len(nums) - idx) >= k and num < stack[-1]:
                stack.pop()
            stack.append(num)
        
        return stack[:k]