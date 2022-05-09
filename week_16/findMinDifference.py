class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()

        min_ = float("inf")
        for index in range(len(timePoints)):
            first = list(map(int, timePoints[index].split(":")))
            second = list(
                map(int, timePoints[(index + 1) % len(timePoints)].split(":")))

            # put in place
            actualMax = max(first, second)
            actualMin = min(first, second)

            if actualMax == actualMin:
                return 0
            elif actualMax[0] == actualMin[0]:
                min_ = min(min_, actualMax[1] - actualMin[1])
            else:
                mins = 60 - actualMin[1] + actualMax[1]
                hrs = actualMax[0] - actualMin[0] - 1

                tot = hrs * 60 + mins

                tempMins = 60 - mins
                temphrs = 23 - hrs

                reverseTot = temphrs * 60 + tempMins

                min_ = min(min_, tot, reverseTot)

        return min_