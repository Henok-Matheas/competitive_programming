class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        
        """
        left, right = 0, max(nums)
        answer = 0
        
        def counter(target, nums):
            idx, count = 0, 0
            
            while idx < len(nums):
                if nums[idx] <= target:
                    count += 1
                    idx += 1
                    
                idx += 1
                
            return count
        
        
        while left <= right:
            mid = (left + right) // 2
            
            if counter(mid, nums) < k:
                left = mid + 1
                
            else:
                answer = mid
                right = mid - 1
                
        return answer