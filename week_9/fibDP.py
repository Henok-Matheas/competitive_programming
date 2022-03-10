class Solution:
    visited = defaultdict(int)

    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        if n - 2 not in self.visited: self.visited[n - 2] = self.fib(n - 2)
        if n - 1 not in self.visited: self.visited[n - 1] = self.fib(n - 1)
        return self.visited[n - 1] + self.visited[n - 2]