class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) == 1 or len(fruits) == 2:
            return len(fruits)

        i = 0
        j = 0

        first_basket = fruits[0]
        first_last = i
        while j < len(fruits) and fruits[j] == fruits[0]:
            if fruits[j] == first_basket:
                first_last = j
            j += 1

        if j == len(fruits):
            return len(fruits)

        second_basket = fruits[j]
        second_last = j

        max_ = j + 1

        while i < len(fruits):
            while j < len(fruits) and (fruits[j] == second_basket
                                       or fruits[j] == first_basket):
                if fruits[j] == second_basket:
                    second_last = j
                else:
                    first_last = j
                j += 1

            max_ = max(max_, j - i)
            if j >= len(fruits):
                return max_

            i = min(first_last, second_last) + 1
            first_last = max(first_last, second_last)
            first_basket = fruits[first_last]
            second_last = j
            second_basket = fruits[second_last]
        return max_
