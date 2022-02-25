class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        best = [-1, -1]

        while (left <= right):
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left_temp = mid
                right_temp = mid

                right_return = mid
                left_return = mid

                while left_temp <= right:
                    midi = (left_temp + right) // 2

                    if nums[midi] == target:
                        left_temp = midi + 1
                        right_return = midi
                    else:
                        right = midi - 1

                while left <= right_temp:
                    midi = (left + right_temp) // 2

                    if nums[midi] == target:
                        right_temp = midi - 1
                        left_return = midi
                    else:
                        left = midi + 1

                return [left_return, right_return]
        return best
