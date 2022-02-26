class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        macs = sum(weights)

        left = max(weights)
        right = macs
        best = left
        while left <= right:
            max_weight = (left + right) // 2

            tot_days = 0
            working = max_weight

            i = 0
            while i < len(weights):
                if working - weights[i] < 0:
                    working = max_weight
                    tot_days += 1
                else:
                    working -= weights[i]
                    i += 1
            tot_days += 1
            if tot_days > days:
                left = max_weight + 1
            else:
                best = max_weight
                right = max_weight - 1

        return best
