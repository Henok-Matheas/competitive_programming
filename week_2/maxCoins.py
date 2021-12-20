class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        output = 0
        for i in range(len(piles) - 2,(len(piles) // 3) - 1,-2):
            print(piles[i])
            output += piles[i]
        return output