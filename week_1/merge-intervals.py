



def merge(intervals):

    for i in range(len(intervals)):
        for j in range(len(intervals) - 1):
            if intervals[j][0] > intervals[j + 1][0]:
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]

    print(intervals)

    finals = []

    for i in range(len(intervals)-1):
        print(i,'this is i')
        for j in range(i+1,len(intervals)):
            print(i,j,"this is i and j respectively")
            print(intervals[i],intervals[j],"these are the intervals of i and j")
            if len(intervals[i]) == 2 and intervals[i][0] <= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                intervals[i][1] = intervals[j][1]
                intervals[j] = 'i'
            elif len(intervals[i]) == 2 and intervals[i][0] <= intervals[j][0] and intervals[i][1] > intervals[j][1]:
                intervals.remove(intervals[j])

    return intervals

print(merge([[1,4],[4,5],[1,3]]))