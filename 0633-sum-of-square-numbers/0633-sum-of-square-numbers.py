class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(ceil(sqrt(c))):
            b = int(sqrt(c - (a ** 2)))
            if b ** 2 + a ** 2 == c:
                return True
        return False if c != 0 else True