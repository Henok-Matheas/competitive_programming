class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        """
        
        for some index we can have two checks.
        
        one with 3 elements
        
        one with 2 elements
            - are the 2 elements the same
            
        one with 3 elements
            - are the 3 elements the same
            - are the 3 elements increasing
            
        if the current idx is 
        """
        
        @lru_cache(None)
        def dp(idx):
            if idx == len(nums):
                return True
            
            valid = False
            
            if idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                valid = valid or dp(idx + 2)
            
            if idx + 2 < len(nums) and nums[idx] == nums[idx + 1] and nums[idx] == nums[idx + 2]:
                valid = valid or dp(idx + 3)
            
            if idx + 2 < len(nums) and nums[idx] + 1 == nums[idx + 1] and nums[idx] + 2 == nums[idx + 2]:
                valid = valid or dp(idx + 3)
            
            return valid
        
        return dp(0)