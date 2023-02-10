class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        
        j = 0
        while j < len(nums) and nums[j] < 0:
            j += 1
        
        j = len(nums) - 1 if j >= len(nums) else j
        i = j - 1
        while i >= 0 or j < len(nums):
            if i >= 0 and (j >= len(nums) or (j < len(nums) and nums[i] ** 2 <= nums[j] ** 2)):
                answer.append(nums[i] ** 2)
                i -= 1
            elif j < len(nums) and (i < 0 or (i >= 0 and nums[i] ** 2 > nums[j] ** 2)):
                answer.append(nums[j] ** 2)
                j += 1
            
        return answer