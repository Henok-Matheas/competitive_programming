# [[2,1,1],[1,1,0],[0,1,1]]
# [[2,1,1],[0,1,1],[1,0,1]]
# [[0,2]]
# [[2,1,1,1],[1,1,1,2],[2,1,1,1]]

import collections


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        parents = collections.deque([])
        children = collections.deque([])

        #left, right, up, down
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        one = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    parents.append([i, j, 0])
                if grid[i][j] == 1:
                    one = True

        if not parents:
            if one:
                return -1
            else:
                return 0

        bound = lambda row, column: row >= 0 and row < len(
            grid) and column >= 0 and column < len(grid[0])
        level = 0
        while parents or children:

            while parents:
                parent = parents.popleft()

                if parent:
                    level = parent[2]
                for direction in directions:
                    row = parent[0] + direction[0]
                    column = parent[1] + direction[1]

                    if not bound(row, column) or grid[row][column] != 1:
                        continue
                    children.append([row, column, level + 1])

            while children:
                child = children.popleft()
                grid[child[0]][child[1]] = 2
                if child:
                    parents.append(child)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return level
