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
