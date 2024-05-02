class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        """
        list of pos and neg ints without zero find largest pos num such that -k exists as well.
        """
        left, right, ans = 0, len(nums) - 1, -1
        nums.sort()
        
        while nums[left] < 0 and nums[right] > 0:
            if abs(nums[left]) > nums[right]:
                left += 1
            elif abs(nums[left]) < nums[right]:
                right -= 1
            else:
                return nums[right]
        
        return ans