class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        n piles
        speed of eating =  k
        
        she wants to finish in h hours but wants to take it as slow as possible so find k
        
        
        1000
        
        30 * 10 ** 4
        nlogk
        
        """
        
        def getHours(piles, speed):
            hours = 0
            
            for pile in piles:
                hours += ceil(pile / speed)
                
            return hours
        
        
        low, high = 1, max(piles)
        best = 1
        
        
        while low <= high:
            mid = (low + high) // 2
            
            hours = getHours(piles, mid)
            
            if hours > h:
                low = mid + 1
            else:
                best = mid
                high = mid - 1
                
        return best