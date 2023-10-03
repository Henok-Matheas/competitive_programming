class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        
        there will be no visited.
        will have path
        
        it's actually a backtrack solution.
        """
        
        answer, path = [], [0]
        
        def backtrack(path):
            if path and path[-1] == len(graph) - 1:
                answer.append(path[:])
                return
            
            for child in graph[path[-1]]:
                path.append(child)
                backtrack(path)
                path.pop()
                
                
        backtrack(path)
        return answer
                
            
        