class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxim = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                count = 0
                while current in num_set:
                    current += 1
                    count += 1
                maxim = max(maxim, count)
            
        return maxim