class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        finals = [intervals[0]]

        for interval in intervals:
            if finals[-1][0] <= interval[0] and interval[0] <= finals[- 1][1]:
                finals[-1][1] = max(finals[- 1][1], interval[1])
                # print(finals[-1])
            else:
                finals.append(interval)
                # print(finals)
        return finals