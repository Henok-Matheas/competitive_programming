class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        boats = 0
        sum_ = 0
        for right in reversed(range(len(people))):
            if right < left:
                return boats
            
            if left < right and people[right] + people[left] <= limit:
                left += 1
            boats += 1
            
        return boats