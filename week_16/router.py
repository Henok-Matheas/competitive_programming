from collections import defaultdict

n, m = list(map(int, input().split()))


class Node:

    def __init__(self, capacity, bandwidth=0) -> None:
        self.bandwidth = bandwidth
        self.connected = 0
        self.capacity = capacity
        self.children = []


graph = defaultdict(Node)

for router in range(n):
    cap, band = list(map(int, input().split()))
    node = Node(cap, band)
    graph[router] = node

for hotspt in range(m):
    hotspot = n + m
    cap, parent = list(map(int, input().split()))
    node = Node(cap, 0)
    graph[hotspot] = node
    graph[parent].children.append(hotspot)
    graph[parent].connected += 1


for hotspt in range(m):
