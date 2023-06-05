class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """
        n ** 2 to build the graph
        
        for every node call dfs(node) which returns maxim detonated
        """
        
        graph = defaultdict(list)
        detonated = 0
        
        for current_bomb, (x1, y1, r1) in enumerate(bombs):
            for next_bomb, (x2, y2, r2) in enumerate(bombs):
                distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if current_bomb != next_bomb and distance <= r1:
                    graph[current_bomb].append(next_bomb)
        
        def dfs(root):
            visited = set([root])
            stack = [root]
            count = 0
            
            while stack:
                node = stack.pop()
                count += 1
                
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)
                        
            return count
        
        for bomb in range(len(bombs)):
            detonated = max(dfs(bomb), detonated)
            
        return detonated