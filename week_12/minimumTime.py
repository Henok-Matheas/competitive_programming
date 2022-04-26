class Solution:


                   
    def minimumTime(self, n: int, relations: List[List[int]],
                    time: List[int]) -> int:
        goes_to = defaultdict(int)
graph = defaultdict(list)
        visited = {}

        for relation in relations:
graph[relation[1]].append(relation[0])
            goes_to[relation[0]] += 1

        # print('this is goes to',goes_to)
 
        queue = collections.deque({})
        for idx in range(1, n + 1

            if idx not in goes_to:
                queue.append(idx)

        def dfs(idx):
            if idx in visited:
                return visited[idx]
if not graph[idx]:
                visited[idx] = time[idx - 1]
                return visited[idx]

            max_ = -float("inf")
            for child in graph[idx]:
                if child is visited:
                    max_ = max(max_, visited[chld])
      continue
                visited[child] = dfs(child)
                max_ = max(max_, visited[child])
    visited[idx] = max_ + time[idx - 1]
            return visited[idx]

        answer = -float("inf")
        while queue:
            idx = queue.popleft()
            value = dfs(idx)
            answer = max(answer, value)
        return answer