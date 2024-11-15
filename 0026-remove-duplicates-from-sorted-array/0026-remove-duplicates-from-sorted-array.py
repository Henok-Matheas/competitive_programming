class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        have a placer and seeker
        
        the seeker will find nums which are different from their previous and then place them at the placer
        then the placer will move
        """
        place  = 0
        for seek, num in enumerate(nums):
            if not seek or nums[seek - 1] != num:
                nums[place] = num 
                place += 1
                
        return place