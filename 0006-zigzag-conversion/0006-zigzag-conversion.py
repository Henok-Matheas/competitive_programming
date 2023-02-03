class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction, row = "positive", -1
        rows = [""] * numRows

        for char in s:
            row += 1 if direction is "positive" else -1

            rows[row] += char

            if row < 1:
                direction = "positive"
            if row == numRows - 1:
                direction = "negative"

        return "".join(rows)

        