class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float("inf")] * len(nums)
        jumps[0] = 0
        
        end = 0
        
        for start, num in enumerate(nums):
            while end < len(nums) and end <= start + num:
                jumps[end] = min(jumps[end], 1 + jumps[start])
                end += 1
        
        if jumps[-1] == float("inf"):
            return -1
        return jumps[-1]