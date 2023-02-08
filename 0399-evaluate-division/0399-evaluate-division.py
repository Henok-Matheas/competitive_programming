class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        graph = defaultdict(list)
        
        
        for index in range(len(equations)):
            root1, root2 = equations[index]
            weight = values[index]
            graph[root1].append([root2,weight])
            graph[root2].append([root1, 1/ weight])
            
            
        def dfs(begin,target,cost):
            if begin == target:
                return cost
    
            for values in graph[begin]:
                neighbour = values[0]
                weight = values[1]
                
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                cst = dfs(neighbour, target, cost * weight)
                if cst != None:
                    return cst
            return None
        
        answer = []
        for query in queries:
            visited = set()
            cost = dfs(query[0],query[1],1) if query[0] in graph and query[1] in graph else None
            answer.append(cost if cost != None else float(-1))
        return answer
        