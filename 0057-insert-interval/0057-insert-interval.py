class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        new_start, new_end = newInterval
        for idx, (curr_start, curr_end) in enumerate(intervals):
            ## if the current interval is strictly lower, then let's append it.
            if curr_end < new_start:
                newIntervals.append(intervals[idx])

            ## if the current interval is strictly greater, then we append the newInterval
            ## and all the rest of the intervals as well because they are also non overlapping
            elif curr_start > new_end:
                newIntervals.append([new_start, new_end])
                return newIntervals + intervals[idx:]

            ## if there is some overlap, then let's maximize our interval and search again
            else:
                new_start, new_end = min(new_start, curr_start), max(new_end, curr_end)

        ## the final interval is always going to be left out, so we append it.
        newIntervals.append([new_start, new_end])
        return newIntervals