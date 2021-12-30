class Solution:
    def recur(self, nums):
        if len(nums) == 1:
            return nums[0]
        return  max(nums[0] - self.recur(nums[1:]), nums[-1] - self.recur(nums[:-1]))
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        value = self.recur(nums)
        print(value)
        if value >= 0:
            return True
        else:
            return False
        