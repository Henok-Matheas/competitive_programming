class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        mid = k - 1
        half = k

        first = 0
        last = len(nums) - 1

        while first < mid:
            nums[first], nums[mid] = nums[mid], nums[first]
            first += 1
            mid -= 1

        while half < last:
            nums[last], nums[half] = nums[half], nums[last]
            last -= 1
            half += 1