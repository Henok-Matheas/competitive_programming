class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        pivot = 0
        first = 0
        lft = 0
        rgt = len(nums) - 1

        while lft <= rgt:
            mid = (lft + rgt) // 2

            if nums[mid] >= nums[first]:
                pivot = mid
                lft = mid + 1
            else:
                rgt = mid - 1

        if nums[left] <= target:
            right = pivot
        else:
            left = pivot + 1

        # print("I am here",pivot,"left",left,"right",right)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1