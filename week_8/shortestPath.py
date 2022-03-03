from collections import deque

maze = [[0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]
working = deque()
visited = set()
# left,right, down, up
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

# length = 0
bound = lambda row, column: row >= 0 and row < len(
    maze) and column >= 0 and column < len(maze[0])


def solve(maze, target):
    length = 0
    starting = [0, 0, 0]
    working.append(starting)
    visited.add(str(0) + " " + str(0))
    while working:
        curr = working.popleft()
        length = curr[2]
        if [curr[0], curr[1]] == target:
            print("equals", curr[0], curr[1])
            return curr[2]

        print("row and column", curr)

        for direction in directions:
            print(length, "this is length")
            row = curr[0] + direction[0]
            column = curr[1] + direction[1]

            if not bound(row, column) or str(row) + " " + str(
                    column) in visited or maze[row][column] == 1:
                continue

            print(row, column)
            working.append([row, column, length + 1])
            visited.add(str(row) + " " + str(column))


print(solve(maze, [2, 1]))
