class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        variations = defaultdict(set)
        busses = defaultdict(set)
        
        for bus in range(len(routes)):
            busses[bus] = set(routes[bus])
            
            for node in routes[bus]:
                variations[node].add(bus)
                
                
            
        start_bus, start_step = -1, 0
        queue = deque([(source, start_bus, start_step)])
        
        while queue:
            node, bus, step = queue.popleft()
            
            if node == target:
                return step
            
            while busses[bus]:
                next_node = busses[bus].pop()
                variations[next_node].remove(bus)
                queue.append((next_node, bus, step))
                
            while variations[node]:
                next_bus = variations[node].pop()
                busses[next_bus].remove(node)
                queue.append((node, next_bus, step + 1))
            
        return -1