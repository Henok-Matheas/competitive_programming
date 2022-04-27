class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = {index: [] for index in range(n)}
        graph = defaultdict(list)
        parent_count = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            parent_count[edge[1]] += 1
            ancestor_list = ancestors[edge[1]]
            ancestor_list.append(edge[0])
        queue = collections.deque({})
        for node in range(n):
            if parent_count[node] == 0:
                queue.append(node)
        while queue:
            node = queue.popleft()
            parents = set()
            while ancestors[node]:
                parent = ancestors[node].pop()
                parents.add(parent)
                parents.update(set(ancestors[parent]))
            parents_list = list(parents)
            parents_list.sort()
            ancestors[node] = parents_list

            for child in graph[node]:
                parent_count[child] -= 1
                if parent_count[child] == 0:
                    queue.append(child)
        answer = [0] * n
        for index in range(n):
            ancestors[index].sort()
            answer[index] = ancestors[index]
        return answer
