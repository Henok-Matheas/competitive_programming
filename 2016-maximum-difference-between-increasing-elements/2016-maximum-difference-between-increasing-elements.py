class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        stack = []
        maxim = -1
        for num in nums:
            ## pop all that are larger or equal
            while stack and stack[-1] >= num:
                stack.pop()
                
            if stack:
                maxim = max(maxim , num - stack[0])
                
            stack.append(num)
            
        return maxim