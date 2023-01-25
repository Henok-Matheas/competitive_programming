class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def bfs(root):
            path = [float("inf")] * n
            visited = set([root])
            
            queue = deque([[0,root]])
            while queue:
                dist, node = queue.popleft()
                path[node] = dist
                neigh = edges[node]
                
                if neigh != -1 and neigh not in visited:
                    visited.add(neigh)
                    queue.append((dist + 1, neigh))
                    
            return path
        
        
        path1 = bfs(node1)
        path2 = bfs(node2)
        minim = [float("inf"), -1]
        
        for node in range(n):
            minim = min(minim, [max(path1[node], path2[node]), node])
        
        return minim[1]