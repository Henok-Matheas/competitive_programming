class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        #holds the visited rows.
        visited = set()

        provinces = 0

        # takes in the row index
        def provinceFind(row):

            for col in range(len(isConnected)):
                if isConnected[row][col] == 0 or col in visited:
                    continue
                visited.add(col)
                provinceFind(col)

        for row in range(len(isConnected)):
            if row not in visited:
                provinces += 1
                visited.add(row)
                provinceFind(row)

        return provinces
