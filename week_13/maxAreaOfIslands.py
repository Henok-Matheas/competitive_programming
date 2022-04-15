class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # left, right, up , down

        size = []
        parent = []
        for row in range(len(grid)):
            temp = []
            prnt = []
            for column in range(len(grid[row])):
                temp.append(1)
                prnt.append([row, column])
            size.append(temp)
            parent.append(prnt)

        directions = [[-1, 0], [1, 0], [0, 1], [0, 1]]

        valid = lambda row, column: 0 <= row < len(grid) and 0 <= column < len(
            grid[-1])
        bound = lambda row, column: row < len(
            grid) and row >= 0 and column < len(grid[0]) and column >= 0

        max_ = -float("inf")

        def find(root):
            if root == parent[root[0]][root[1]]:
                return root
            parent[root[0]][root[1]] = find(parent[root[0]][root[1]])
            return parent[root[0]][root[1]]

        def union(root1, root2):
            # print("in union for {} and {}".format(root1, root2))
            parnt = find(root1)
            child = find(root2)

            if size[parnt[0]][parnt[1]] < size[child[0]][child[1]]:
                parnt, child = child, parnt
            parent[child[0]][child[1]] = parnt

            size[parnt[0]][parnt[1]] += size[child[0]][
                child[1]] if parnt != child else 0
            return size[parnt[0]][parnt[1]]

        def connected(root1, root2):
            return find(root1) == find(root2)

        visited = set()
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 1:
                    # print("{}'s value is 1".format([row,column]))
                    for direction in directions:
                        newRow = row + direction[0]
                        newColumn = column + direction[1]

                        if bound(newRow,
                                 newColumn) and grid[newRow][newColumn] == 1:
                            # print("{} direction for {}".format(direction,[row,column]))
                            # print(newRow,newColumn)
                            siz = union([row, column], [newRow, newColumn])
                            max_ = max(siz, max_)
                            # print("this is the size",siz)
                    max_ = max(max_, size[row][column])
                    # print("{}'s maximum is 1".format([row,column]))
        return max_ if max_ != -float("inf") else 0
