class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(left, right, k):
            pivot, pointer = nums[right], left

            for idx in range(left, right):
                if nums[idx] <= pivot:
                    nums[pointer], nums[idx] = nums[idx], nums[pointer]
                    pointer += 1

            nums[pointer], nums[right] = nums[right], nums[pointer]

            if pointer < k:
                return quickselect(pointer + 1, right, k)
            elif pointer > k:
                return quickselect(left, pointer - 1, k)
            return nums[pointer]

        return quickselect(0, len(nums) - 1, len(nums) - k)