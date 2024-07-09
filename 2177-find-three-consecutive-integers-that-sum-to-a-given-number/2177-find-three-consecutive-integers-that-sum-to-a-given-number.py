class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 == 0:
            low = (num - 3) // 3
            return [low, low + 1, low + 2]
        return []