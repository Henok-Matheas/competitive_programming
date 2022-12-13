class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        next_ = [None, None]
        nexts = [[] for _ in range(len(binary))]
        for idx in reversed(range(len(binary))):
            value = int(binary[idx])
            nexts[idx] = next_[::]
            next_[value] = idx
            
        
        @lru_cache(None)
        def dp(index):
            
            total = 1
            if nexts[index][1] is not None:
                total += dp(nexts[index][1])
                
            if nexts[index][0] is not None:
                total += dp(nexts[index][0])
            return total
        
        total = min(binary.count("0"), 1)
        
        if next_[1] is not None:
            total += dp(next_[1])
            
        return total % (7 + 10 ** 9)
            
        
        
        