

class Solution:
    def numIdenticalPairs(nums):
        if len(nums) < 2:
            return 0
        g_pairs = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    g_pairs += 1
        return g_pairs