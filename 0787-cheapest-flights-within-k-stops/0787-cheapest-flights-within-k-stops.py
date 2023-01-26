class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## first we consturct the graph in  a dictionary format
        graph = defaultdict(list)
        for source, destination, weight in flights:
            graph[source].append([destination, weight])
        
        ## we use the heap to get the lowest price, and stop value
        heap = [[0,-1, src]]
        ## we visit a node, with stop,
        visited = {}

        while heap:
            weight, stop, node = heapq.heappop(heap)
            visited[node] = stop
            if node == dst:
                return weight

            for neigh, neigh_weight in graph[node]:
                ## if the stops is > k then we don't really need to visit it
                ## if we didn't visit it or if the way we visited it had a worse off stop
                ## then we can visit it again with a better stop
                if stop + 1 <= k and (neigh not in visited or stop + 1 < visited[neigh]):
                    heapq.heappush(heap,[weight + neigh_weight, stop + 1, neigh])

        return -1





