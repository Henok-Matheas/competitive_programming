class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        normal dp, but can we make it bottom up?
        """
        
        @lru_cache(None)
        def dp(start):
            if start == len(arr):
                return 0
            
            maxim = 0
            curr_max = 0
            for idx in range(start, min(len(arr), start + k)):
                curr_max = max(curr_max, arr[idx])
                to_add = (idx - start + 1) * curr_max
                maxim = max(maxim, to_add + dp(idx + 1))
                
            return maxim
        
        return dp(0)