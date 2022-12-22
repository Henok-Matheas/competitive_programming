class Solution:
    def traverse(self, node, down, graph):
        distance, count = 0, 1
        
        while graph[node]:
            neigh = graph[node].pop()
            ## remove node from neigh
            graph[neigh].discard(node)
            
            neigh_dist, neigh_count = self.traverse(neigh, down, graph)
            distance += neigh_dist + neigh_count
            count += neigh_count
            
        down[node] = (distance, count)
        return down[node]
    
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = collections.defaultdict(set)
        res = [0] * n
        count = [1] * n
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + n - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res