class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0]

        sum_ = 0
        prefix_dict = defaultdict(int)
        prefix_dict[0] += 1
        for num in nums:
            currSum = prefixSum[-1] + num
            sum_ += prefix_dict[currSum - k]
            prefixSum.append(currSum)
            prefix_dict[currSum] += 1
        return sum_