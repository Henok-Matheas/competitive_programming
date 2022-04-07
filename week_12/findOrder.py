class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        comesfrom = defaultdict(int)
        graph = defaultdict(list)

        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            comesfrom[courses[0]] += 1
        queue = collections.deque({})
        for idx in range(numCourses):
            if idx not in comesfrom:
                queue.append(idx)
        answer = []
        while queue:
            node = queue.popleft()
            answer.append(node)
            for child in graph[node]:
                comesfrom[child] -= 1
                if comesfrom[child] == 0:
                    queue.append(child)
        return answer if len(answer) == numCourses else []
