class Solution:
    def binary(self, target, nums, best):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= target:
                left = mid + 1
            else:
                best = nums[mid]
                right = mid - 1
        
        return best
    
    
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        @lru_cache(None)
        def dp(pointer1, prev):
            
            ## if pointer1 runs out return 0
            ## if the current value is invalid and if pointer2 won't satisfy us, retur
            if pointer1 == len(arr1):
                return 0
            
            current = arr1[pointer1]
            replace = self.binary(prev, arr2, current)
            
            unreplaced = replaced = float("inf")
            ### try to decide on the replacement
            ### if we can't find any replacement then return float
            if current > prev:
                unreplaced = dp(pointer1 + 1, current)
                
            if replace > prev:
                replaced = 1 + dp(pointer1 + 1, replace)
            
            """
            for replaced use a binary search method to find what to replace it with
            """
            return min(unreplaced, replaced)
        
        
        
        operations = dp(0, -1)
        if operations == float("inf"):
            return -1
        
        return operations