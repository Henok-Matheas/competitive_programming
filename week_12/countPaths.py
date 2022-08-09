class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        arrival_state = [[float("inf"), 0] for _ in range(n)]
        # arrival_time, arrival_count with arrival time
        road_dict = defaultdict(list)
        for node1, node2, time in roads:
            road_dict[node1].append([node2, time])
            road_dict[node2].append([node1, time])

        # time, node, parent
        heap = [[0, 0, 0]]
        visited = set()
        while heap:
            time, node, parent = heapq.heappop(heap)

            if time > arrival_state[n - 1][0]:
                break

            arrival_state[node][0] = min(arrival_state[node][0], time)
            if arrival_state[node][0] == time:
                arrival_state[node][1] += arrival_state[parent][
                    1] if arrival_state[parent][1] else 1
            if node in visited:
                continue

            visited.add(node)

            for neigh, neigh_time in road_dict[node]:
                if neigh in visited:
                    continue

                heapq.heappush(heap, [time + neigh_time, neigh, node])
        # print(arrival_state)
        return arrival_state[n - 1][1] % (7 + (10**9))
