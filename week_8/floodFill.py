#https://leetcode.com/problems/flood-fill/


#another optimized recursive solution
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:

        oldColor = image[sr][sc]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        if newColor == oldColor:
            return image

        bound = lambda row, column: row < len(
            image) and row >= 0 and column < len(image[0]) and column >= 0

        def recur(sr, sc):
            image[sr][sc] = newColor

            for direction in directions:
                row = sr + direction[0]
                column = sc + direction[1]

                if not bound(row, column) or image[row][column] != oldColor:
                    continue
                recur(row, column)

        recur(sr, sc)
        return image


#recurrence solution
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:

        oldColor = image[sr][sc]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visited = set()

        def recur(sr, sc):
            image[sr][sc] = newColor

            for direction in directions:
                row = sr + direction[0]
                column = sc + direction[1]

                if (row, column) in visited or row >= len(
                        image) or row < 0 or column >= len(
                            image[0]
                        ) or column < 0 or image[row][column] != oldColor:
                    continue

                visited.add((row, column))
                recur(row, column)

        recur(sr, sc)
        return image


# iterative solution
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        #right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        color = image[sr][sc]

        image[sr][sc] = newColor

        visited = set()

        stack = []

        stack.append([sr, sc])

        stringi = str(sr) + " " + str(sc)
        visited.add(stringi)

        while stack:
            img = stack.pop()
            row = img[0]
            column = img[1]
            for direction in directions:
                rw = row + direction[0]
                cl = column + direction[1]
                if rw >= len(image) or cl >= len(image[0]) or rw < 0 or cl < 0:
                    continue
                elif str(rw) + " " + str(
                        cl) not in visited and image[rw][cl] == color:
                    image[rw][cl] = newColor
                    stack.append([rw, cl])
                    visited.add(str(rw) + " " + str(cl))

        return image
