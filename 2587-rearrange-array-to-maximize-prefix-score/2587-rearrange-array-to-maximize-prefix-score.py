class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """
        nums = 
        
        """
        nums.sort(reverse = True)
        sum_ = 0
        count = 0
        
        for num in nums:
            sum_ += num
            
            if sum_ > 0:
                count += 1 
        
        return count
            