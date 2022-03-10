class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(2, len(cost)):
            cost[idx] = min(cost[idx - 1], cost[idx - 2]) + cost[idx]
        return min(cost[-1], cost[-2])


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = defaultdict(int)
        value = 0
        n = 2

        visited[0] = 0
        visited[1] = 0
        while n <= len(cost):
            visited[n] = min(visited[n - 1] + cost[n - 1],
                             visited[n - 2] + cost[n - 2])
            n += 1

        return visited[len(cost)]


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