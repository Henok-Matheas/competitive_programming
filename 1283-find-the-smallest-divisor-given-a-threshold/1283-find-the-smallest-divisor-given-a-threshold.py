class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        best = right
        
        def div_sum(div: int):
            tot = 0
            for num in nums:
                tot += math.ceil(num / div)
            return tot
        
        while left <= right:
            mid = (left + right) // 2
            
            if div_sum(mid) > threshold:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
            
            
        return best