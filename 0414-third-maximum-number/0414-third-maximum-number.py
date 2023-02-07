class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        k = len(nums) - 3

        if k < 0:
            return max(nums)

        def quickselect(left, right, k):
            pivot, pointer = nums[right], left
            for idx in range(left, right):
                if nums[idx] <= pivot:
                    nums[idx], nums[pointer] = nums[pointer], nums[idx]
                    pointer += 1

            nums[right], nums[pointer] = nums[pointer], nums[right]

            if pointer < k:
                return quickselect(pointer + 1, right, k)
            if pointer > k:
                return quickselect(left, pointer - 1, k)

            return nums[pointer]

        return quickselect(0, len(nums) - 1, k)
            