class Solution:
    def traverse(self, node, counts, distances, graph):
        distance, count = 0, 1
        
        while graph[node]:
            neigh = graph[node].pop()
            ## remove node from neigh
            graph[neigh].discard(node)
            
            neigh_dist, neigh_count = self.traverse(neigh, counts, distances, graph)
            distance += neigh_dist + neigh_count
            count += neigh_count
            
        counts[node] = count
        distances[node] = distance
        return distance, count
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        distance = [0] * n
        count = [0] * n
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        graph_copy = copy.deepcopy(graph)   
        
        down = [[] for _ in range(n)]
        total, nodes = self.traverse(0, count, distance, graph)
        graph = graph_copy
        
        print(count)
        print(distance)
        stack = [[0, total  + n]]
        
        while stack:
            node, parent_dist = stack.pop()  
            distance[node] = parent_dist - count[node] + n - count[node]
            
            while graph[node]:
                neigh = graph[node].pop()
                ## remove node from neigh
                graph[neigh].discard(node)
                
                stack.append((neigh, distance[node]))
        
        return distance