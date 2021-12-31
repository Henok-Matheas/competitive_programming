class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        print(ceil(n / 2))
        m = 10 ** 9 + 7
        return (pow(5, ceil(n / 2),m) * pow(4 ,(n // 2),m))%m