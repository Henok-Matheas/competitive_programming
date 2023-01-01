class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        starting = defaultdict(int)
        ending = defaultdict(int)
        
        for num, from_, to_ in trips:
            starting[from_] += num
            ending[to_] += num
            
        MAX_POS = 1000
        pool = 0
        for pos in range(MAX_POS):
            pool -= ending[pos]
            pool += starting[pos]
            
            if pool > capacity:
                return False
        
        return True