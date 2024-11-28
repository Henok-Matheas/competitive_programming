class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r_sum = []
        tot = 0
        
        for num in nums:
            tot += num
            r_sum.append(tot)
        
        return r_sum