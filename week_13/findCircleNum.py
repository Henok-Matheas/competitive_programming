class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        height = [0] * len(isConnected)
        parent = [idx for idx in range(len(isConnected))]

        def isParent(root):
            return root == parent[root]

        def find(child):
            if child == parent[child]:
                return child
            parent[child] = find(parent[child])
            return parent[child]

        def union(root1, root2):
            dad = find(root1)
            child = find(root2)

            if dad != child and height[child] > height[dad]:
                child, dad = dad, child
            parent[child] = dad
            height[dad] = max(height[child] + 1, height[dad])

        def connected(root1, root2):
            return find(root1) == find(root2)

        for root1 in range(len(isConnected)):
            for root2 in range(len(isConnected)):
                if isConnected[root1][root2] == 1:
                    union(root1, root2)

        count = 0
        for root in range(len(isConnected)):
            if isParent(root):
                count += 1
        return count
