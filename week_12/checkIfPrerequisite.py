class Solution:

    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ancestors = {index: set() for index in range(numCourses)}
        parents_count = [0] * numCourses

        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            parents_count[edge[1]] += 1
            ancestors[edge[1]].add(edge[0])

        queue = collections.deque()

        for element in range(numCourses):
            if parents_count[element] == 0:
                queue.append(element)

        while queue:
            node = queue.popleft()
            parents = set()
            for parent in ancestors[node]:
                parents.update(set(ancestors[parent]))
            ancestors[node].update(parents)
            for child in graph[node]:
                parents_count[child] -= 1
                if parents_count[child] == 0:
                    queue.append(child)

        answer = []
        for query in queries:
            answer.append(True if query[0] in ancestors[query[1]] else False)
        return answer
