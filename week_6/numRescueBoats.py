class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        ppl = collections.deque(people)

        count = 0
        while ppl:
            if len(ppl) == 1:
                return count + 1

            first = ppl[0]
            last = ppl.pop()

            if first + last <= limit:
                ppl.popleft()
            count += 1
        return count