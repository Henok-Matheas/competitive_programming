class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        have a while loop to place the numbers at their correct positions
        so we will have for while loop
        the while loop is for placing and the way it works is 
        """
        visited = set()
        for seek in range(len(nums)):
            if seek in visited:
                continue
            curr_idx, curr = seek, nums[seek]
            while (curr_idx + k) % len(nums) not in visited:
                visited.add((curr_idx + k) % len(nums))
                curr, nums[(curr_idx + k) % len(nums)] = nums[(curr_idx + k) % len(nums)], curr
                curr_idx = (curr_idx + k) % len(nums)