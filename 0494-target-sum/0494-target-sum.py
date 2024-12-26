class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        simple backtrack
        
        count = 0
        """
        @lru_cache(None)
        def dp(total, idx):
            if idx == len(nums):
                return total == target
            
            return dp(total + nums[idx], idx + 1) + dp(total - nums[idx], idx + 1)
        
        return dp(0, 0)
            