class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        flippable = k
        i = 0
        j = 0
        max_ = 0
        while i < len(nums) and j < len(nums):
            while j < len(nums) and (flippable > 0 or nums[j] == 1):
                if nums[j] == 0 and flippable > 0:
                    flippable -= 1
                j += 1
            if nums[i] == 0:
                flippable += 1 if flippable < k else 0
            max_ = max(max_, j - i)
            i += 1
            j = i if j < i else j
        return max_