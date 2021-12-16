

class Solution:
    def numIdenticalPairs(nums):
        counted = [0]* 101
        g_pairs = 0
        for i in nums:
            counted[i] += 1 
        
        for j in counted:
            g_pairs += int((j * (j - 1)/2))
        return g_pairs