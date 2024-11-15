class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        this is a placeholder and seeker question
        
        seeker is the for loop
        
        when I find a zero I swap it with the placeholder and then have placeholder += 1
        """
        place = 0
        
        for seek in range(len(nums)):
            if nums[seek] != 0:
                nums[place], nums[seek] = nums[seek], nums[place]
                place += 1
        