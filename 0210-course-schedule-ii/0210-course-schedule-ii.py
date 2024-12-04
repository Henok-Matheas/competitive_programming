class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        BFS - KAHNS ALGO
        
        DFS METHOD USING COLORING
        
        WE USE BACKTRACKING AND COLORING
        
        COLORS:
        0 - UNVIS
        1 - IN PATH
        2 - VISISTED
        """
        graph = [[] for _ in range(numCourses)]
        colors = [0] * numCourses
        order = []
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            
        
        def topSort(course):
            if colors[course] == 1:
                return False
            
            colors[course] = 1
            for child in graph[course]:
                if colors[child] == 2:
                    continue
                if not topSort(child):
                    return False
                
            colors[course] = 2
            order.append(course)
            return True
            
        for course in range(numCourses):
            if colors[course]:
                continue
                
            if not topSort(course):
                return []
        
        return list(reversed(order))