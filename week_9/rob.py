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