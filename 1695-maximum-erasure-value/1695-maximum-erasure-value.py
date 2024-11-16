class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxim, total = 0, 0
        left = 0
        unique = set()
        
        for num in nums:
            while num in unique:
                popped = nums[left]
                total -= popped
                unique.remove(popped)
                left += 1
                
            total += num
            unique.add(num)
            maxim = max(maxim, total)
            
        return maxim