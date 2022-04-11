class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        unsafe = set()
        answer = []

        def dfs(node):
            for child in graph[node]:
                if child in path or child in unsafe:
                    unsafe.add(child)
                    unsafe.add(node)
                    break
                elif child in visited:
                    continue
                visited.add(child)
                path.add(child)
                dfs(child)
                if child in unsafe:
                    unsafe.add(node)
            path.remove(node)
            return 0

        for idx in range(len(graph)):
            if idx not in visited:
                visited.add(idx)
                path.add(idx)
                dfs(idx)
                # if idx not in unsafe:
                #     answer.append(idx)
        for idx in range(len(graph)):
            if idx not in unsafe:
                answer.append(idx)
        return answer