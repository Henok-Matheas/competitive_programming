class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        alice = ()
        
        X piles, M = max(M, X)
        
        1 <= X <= 2M
        
        
        [2, 7, 9, 4, 4]
        
        
        alice = [1, 2] = 2, 
        
        """
        @cache
        def dp(range_, index, person):
            if index >= len(piles):
                return (0, 0)
            
            maxim = (-inf, -inf)
            total = 0
            for idx in range(index, min(len(piles), index + range_)):
                total += piles[idx]
                current = [0, 0]
                returned = dp(max(range_,2 * (idx - index + 1)), idx + 1, 1 - person)
                current[0] += returned[0]
                current[1] += returned[1]
                current[person] += total
                current = tuple(current)
                
                
#                 if range_ == 4 and index == 4 and person == 0:
#                     print(total, current, "before", idx + 1, dp(max(range_,2 * (idx - index + 1)), idx + 1, 1 - person))
                # if range_ == 4 and index == 4 and person == 0:
                #     print(total, current)
                
                maxim = max(maxim, current, key = lambda pile : (pile[person]))
                
            # print(maxim, range_, index, person)
            return maxim
            
        return dp(2, 0, 0)[0]