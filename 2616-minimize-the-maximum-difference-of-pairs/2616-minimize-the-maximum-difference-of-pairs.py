class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        question:
        minimize the maximum difference between p pairs
        
        thought:
        first thing is sorting them because after we sort them the best matching is consecutive ones
        
        create consecutive difference pairs
        
        amongst the difference pairs select the bottom p pairs using dp
        
        
        0 2
        1 3
        
        as opposed to 0 1, 2 3
        """
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        answer = 0
        
        
        def counter(target, nums):
            count = 0
            idx = 0
            
            while idx < len(nums) - 1:
                if nums[idx + 1] - nums[idx] <= target:
                    idx += 1
                    count += 1
                    
                idx += 1
                
            return count
                
                
                
            
        # counter(1, nums)
        while left <= right:
            mid = (left + right) // 2
            
            count = counter(mid, nums)
            if count < p:
                left = mid + 1
                
            else:
                answer = mid
                right = mid - 1
                
        return answer