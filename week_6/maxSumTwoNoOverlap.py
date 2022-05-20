class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:

        first = [[sum(nums[:firstLen]), 0, firstLen - 1]]
        # for i in range(firstLen):
        #     first[-1] += nums[i]

        second = [[sum(nums[:secondLen]), 0, secondLen - 1]]
        # for i in range(secondLen):
        #     second[-1] += nums[i]
        #         j = secondLen

        for i in range(firstLen, len(nums)):
            first.append([
                first[-1][0] + nums[i] - nums[i - firstLen], i + 1 - firstLen,
                i
            ])

        for i in range(secondLen, len(nums)):
            second.append([
                second[-1][0] + nums[i] - nums[i - secondLen],
                i + 1 - secondLen, i
            ])

        max_ = -float("inf")

        for one, indxl, indxr in first:
            for two, indexl, indexr in second:
                if indxl <= indexl <= indxr or indexl <= indxl <= indexr:
                    continue

                max_ = max(max_, two + one)
        return max_
