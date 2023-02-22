class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        modulo = defaultdict(int)
        total = 0
        for curr in time:
            mod = curr % 60
            total += modulo[(60 - mod) % 60]
            
            modulo[mod] += 1
            
        return total