class Solution:

    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        visited = defaultdict(int)

        def recur(index):
            if index >= len(nums):
                return 0

            if index + 2 not in visited: visited[index + 2] = recur(index + 2)
            if index + 3 not in visited: visited[index + 3] = recur(index + 3)

            return max(visited[index + 2], visited[index + 3]) + nums[index]

        return max(recur(0), recur(1))


class Solution:

    def rob(self, nums: List[int]) -> int:

        maxim = 0
        bound = lambda row: row >= 0 and row < len(nums)
        for i in range(len(nums)):
            jump2 = nums[i - 2] if bound(i - 2) else 0
            jump3 = nums[i - 3] if bound(i - 3) else 0

            nums[i] += max(jump2, jump3)

            maxim = max(maxim, nums[i])
        return maxim