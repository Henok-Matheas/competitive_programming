class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        i = 0

        t = n
        while i < len(flowerbed):
            if i == len(flowerbed) - 1 and flowerbed[i] == 0:
                t -= 1
            elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                i += 1
            elif i + 1 < len(flowerbed) and flowerbed[i] == 0 and flowerbed[
                    i + 1] == 0:
                t -= 1
            i += 2
        return True if t <= 0 else False