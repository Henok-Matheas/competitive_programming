class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        4, 16
        
        10  valid
        
        4 10
        
        7 valid
        
        4 7
        
        5 invalid
        
        6 7
        
        6
        
        [1, 2, 2, 3, 4, 4]
        """
        left, right = max(weights), sum(weights)
        best = right
        
        def calc_days(max_cap : int) -> int:
            day = 0
            cap = -1
            
            for weight in weights:
                if cap - weight >= 0:
                    cap -= weight
                else:
                    cap = max_cap - weight
                    day += 1
            
            return day
        
        while left <= right:
            mid = (left + right) // 2
            day = calc_days(mid)
            
            if day > days:
                left = mid + 1
            else:
                best = mid
                right = mid - 1
            
            
        return best