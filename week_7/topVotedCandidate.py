class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.people = [0] * 5000

        max_index = None
        for idx in range(len(self.persons)):
            person = self.persons[idx]
            self.people[person] += 1
            if max_index == None or self.people[person] >= self.people[
                    max_index]:
                max_index = person
            self.persons[idx] = max_index

    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        lower = 0

        while left <= right:
            mid = (left + right) // 2

            if self.times[mid] == t:
                lower = mid
                return self.persons[lower]

            elif self.times[mid] < t:
                lower = mid
                left = mid + 1
            else:
                right = mid - 1

        return self.persons[lower]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)