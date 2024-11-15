class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        for this question we just need to jump either 2 or 3 steps
        
        what if we use the heap to only store k values?
        
        
        
        
        """
        def is_valid(diff, k):
            prev = -2
            for idx, num in enumerate(nums):
                if idx > prev + 1 and num <= diff:
                    prev = idx
                    k -= 1  
            return k <= 0
        
        left, right = 0, max(nums)
        best = right
        while left <= right:
            mid = (left + right) // 2
            
            if is_valid(mid, k):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        
        return best