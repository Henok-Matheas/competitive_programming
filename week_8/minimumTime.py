class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        tTrip = 0

        left = 1
        right = time[0] * totalTrips

        best = right
        while left <= right:
            mid = (left + right) // 2

            trips = 0
            for t in time:
                trips += (mid // t)

            if trips < totalTrips:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
        return best
