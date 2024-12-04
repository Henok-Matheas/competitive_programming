class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        BFS - KAHNS ALGO
        """
        graph = [[] for _ in range(numCourses)]
        incoming = [0] * numCourses
        queue = deque()
        order = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
            
        for course in range(numCourses):
            if not incoming[course]:
                queue.append(course)
                
        while queue:
            course = queue.popleft()
            order.append(course)
            
            for child in graph[course]:
                incoming[child] -= 1
                
                if not incoming[child]:
                    queue.append(child)
                    
        return order if len(order) == numCourses else []