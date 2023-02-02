class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        sub = 0
        nums.sort()
        
        for num  in nums:
            new_num = num - sub
            count += min(new_num, 1)
            sub += new_num
        
        return count