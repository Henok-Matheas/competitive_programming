class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        implementation is kinda ass
        
        but basically we will choose days using binary search and for that day
        
        have a check_bouqs(day, bouq_size, flow_size):
        bouq, flow = 0, 0
        
        for bloom in bloomDay:
        if bloom > day:
        flow = 0
        continue
        flow += 1
        
        if flow == flow_size:
        flow = 0
        bouq += 1
        
        return bouq >= max_bouqs
        
        
        we will go over the indexes and check that we can ma
        """
        left, right = min(bloomDay), max(bloomDay)
        best = -1
        
        def check_bouqs(day, bouq_size, flow_size):
            bouq, flow = 0, 0
            for bloom in bloomDay:
                if bloom > day:
                    flow = 0
                    continue
                    
                flow += 1
                if flow == flow_size:
                    bouq += 1
                    flow = 0
            return bouq >= bouq_size
        
        while left <= right:
            mid = (left + right) // 2
            
            if check_bouqs(mid, m, k):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best