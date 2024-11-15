class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        have a while loop to place the numbers at their correct positions
        so we will have for while loop
        the while loop is for placing and the way it works is 
        reverse the nums and then again revese
        """
        nums.reverse()
        k %= len(nums)
        
        
        def reverse(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        