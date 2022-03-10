class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = defaultdict(int)

        def recur(i):
            if i >= len(cost):
                return 0

            if i + 2 not in visited: visited[i + 2] = recur(i + 2)
            if i + 1 not in visited: visited[i + 1] = recur(i + 1)

            return min(visited[i + 1] + cost[i], visited[i + 2] + cost[i])

        return min(recur(0), recur(1))