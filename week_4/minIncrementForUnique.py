class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        nums.sort()
        
        count = 0
        
        stack = [nums[0]]
        
        value = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] > value:
                value = nums[i]
            else:
                count += value - nums[i] + 1
                value = nums[i] + value - nums[i] + 1
            
            # if nums[i] > stack[-1]:
            #     stack.append(nums[i])
            # elif nums[i] <= stack[-1]:
            #     count += stack[-1] - nums[i] + 1
            #     stack.append(nums[i] + stack[-1] - nums[i] + 1)
        return count