class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        value = 0
        i = 0
        j = 1
        while i < len(prices):
            while j < len(prices) and prices[j - 1] - 1 == prices[j]:
                j += 1
            n = (j - i)
            value += int(((n * (n + 1)) / 2))
            i = j
            j += 1
        return value