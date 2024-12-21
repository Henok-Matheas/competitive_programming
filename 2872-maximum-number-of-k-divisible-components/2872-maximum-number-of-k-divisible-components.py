class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        edges = [node1, node2]
        values with values[i] being value of node i
        
        
        do like a topsort thing since we want to start from the lowest ones 
        
        and whenever  we reach a value whose sum is divisible we add 1 to it
        
        
        so we have innodes 
        we count innodes
        
        we create a queue of the nodes who have an innode of one
        EDGE_CASE = when our tree has onlye one value then we check if it's divisible or not
        
        from the queue when removing
        we check if it's divisible if it is
        add 1 to count
        
        for children
        innnode[child] -= 1
        VALUE[child] += curr if it's not divisible
        if innode[child] == 1 or zero
        add to queue with value
        
        queue = [0, 4, 3]
        values [1, 8, 1, 4, 4]
        
        queue = [4, 3]
        values = [1, 8, 2, 4, 4]
        
        queue = [3, 2]
        values = [1, 8, 6, 4, 4]
        
        values[3] = 4 - FALSE
        queue = [2]
        values = [1, 12, 6, 4, 4]
        
        values[2] = 6 - TRUE
        count += 1
        queue = [1]
        values [1, 12, 6, 4, 4]
        
        """
        graph = [set() for _ in range(n)]
        
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
            
        queue = deque([])
        count = 0
        
        for node in range(n):
            if len(graph[node]) <= 1:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            if values[node] % k == 0:
                count += 1
                values[node] = 0
            
            if len(graph[node]):
                child = graph[node].pop()
                graph[child].remove(node)
                values[child] += values[node]

                if len(graph[child]) == 1:
                    queue.append(child)
        
        return count