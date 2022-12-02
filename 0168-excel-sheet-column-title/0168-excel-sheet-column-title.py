class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        size = ord("Z") - ord("A") + 1
        columnTile = []
        while columnNumber > size:
            div, rem = (columnNumber - 1) // size, (columnNumber - 1) % size
            columnTile.append(chr(ord("A") + rem))
            columnNumber = div
        
        columnTile.append(chr(ord("A") + (-1 + columnNumber) % size))

        return "".join(columnTile[::-1])