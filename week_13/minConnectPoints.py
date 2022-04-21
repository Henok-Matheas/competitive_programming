class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = {(value[0], value[1]): (value[0], value[1])
                   for value in points}
        rank = {(value[0], value[1]): [1, 0] for value in points}
        size = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

        distances = []
        visited = set()
        for root in points:
            for child in points:
                if root == child or ((root[0], root[1], child[0],
                                      child[1])) in visited:
                    continue
                distances.append(
                    [size(root[0], root[1], child[0], child[1]), root, child])
                visited.add((root[0], root[1], child[0], child[1]))
                visited.add((child[0], child[1], root[0], root[1]))

        distances.sort()

        def find(root):
            if root != parents[root]:
                parents[root] = find(parents[root])
            return parents[root]

        def union(root1, root2, weight):
            parent = find(root1)
            child = find(root2)
            if rank[child][0] > rank[parent][0]:
                parent, child = child, parent

            if parent != child:
                parents[child] = parent
                rank[parent][0] += rank[child][0]
                rank[parent][1] += weight + rank[child][1]

        max_size = -float("inf")
        size_count = -float("inf")
        for distance in distances:
            if size_count == len(points):
                return max_size
            root1 = (distance[1][0], distance[1][1])
            root2 = (distance[2][0], distance[2][1])
            union(root1, root2, distance[0])
            max_size = max(rank[root1][1], rank[root2][1])
            size_count = max(rank[root1][0], rank[root2][0])
        return max_size if max_size != -float("inf") else 0
