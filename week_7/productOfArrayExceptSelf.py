class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # before mult and after mult
        before = [1]
        after = [1]

        prefix = 1
        postfix = 1

        for num in nums:
            prefix *= num
            before.append(prefix)

        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            postfix *= num
            after.append(postfix)
        after = after[::-1]
        answer = []
        for idx in range(len(nums)):
            answer.append(before[idx] * after[idx + 1])

        return answer