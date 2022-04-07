class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        comesfrom = defaultdict(int)
        graph = defaultdict(list)

        for courses in prerequisites:
            if courses[0] not in graph:
                graph[courses[0]] = []
            graph[courses[1]].append(courses[0])
            comesfrom[courses[0]] += 1
            comesfrom[courses[1]] += 0
        queue = collections.deque({})
        for node in comesfrom:
            if comesfrom[node] == 0:
                queue.append(node)
        answer = 0
        while queue:
            node = queue.popleft()
            answer += 1
            for child in graph[node]:
                comesfrom[child] -= 1
                if comesfrom[child] == 0:
                    queue.append(child)
        return True if answer == len(graph) else False