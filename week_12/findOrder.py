class Solution:


                 
    def findOrder(self, numCourses: int,
          prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

courses in prerequisites:
            graph[courses[1]].append(courses[0])

        visited = set()
        path = set()

        answer = []
        isCyclic = False

        def dfs(node):
            nonlocal isCyclic
            if isCyclic:
                return
            for child in graph[node]:
                if child in path:
                    isCyclic = True
                    return
                if child in visited:
                    continue
                visited.add(child)
                path.add(child)
    dfs(child)
            answer.append(node)
            path.remove(node)

        for idx in range(numCourses):
            if idx not in visited:
                visited.add(idx)
            
                path.add(idx)
                dfs(idx)
        return answer[::-1] if len(
            answer) == numCourses and not isCyclic else []


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
