class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]],
                      firstPerson: int) -> List[int]:
        meetings.sort(key=lambda lst: lst[-1])
        parents = [i for i in range(n + 1)]
        times = [lst[-1] for lst in meetings]
        times = list(set(times))
        times.sort()

        parents[0] = firstPerson

        def find(root):
            if root == parents[root]:
                return root
            parents[root] = find(parents[root])
            return parents[root]

        def union(root1, root2):
            parent = find(root1)
            child = find(root2)
            if child == firstPerson:
                parent, child = child, parent
            parents[child] = parent

        i = 0
        for time in times:
            first = i
            while i < len(meetings) and meetings[i][-1] <= time:
                # unionized the values of that meeting
                union(meetings[i][0], meetings[i][1])
                i += 1
            while i <= len(meetings) and first < i:
                if find(meetings[first][0]) == firstPerson or find(
                        meetings[first][1]) == firstPerson:
                    # unionize the values with firstPerson
                    union(firstPerson, meetings[first][0])
                    union(firstPerson, meetings[first][1])
                    print
                else:
                    parents[meetings[first][0]] = meetings[first][0]
                    parents[meetings[first][1]] = meetings[first][1]
                first += 1

        answer = [0]

        for numb in range(1, n):
            if find(numb) == firstPerson:
                answer.append(numb)
        print("answer is ", parents)
        return answer
