class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        stack = [source]
        visited = set([source])
                    
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
                    
        return False