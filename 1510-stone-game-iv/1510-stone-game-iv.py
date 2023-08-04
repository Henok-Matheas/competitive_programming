class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        """
        they both remove some square number from n
        
        so when you are bob and you do dp and you will look for instances where alice lost to return it
        when you are alice you will look for instances where bob lost
        
        True for alice
        False for bob
        
        if idx ** idx > remaining:
            return not turn
        
        if turn:
            dp(idx, remaining - idx ^ 2, not turn) or dp(idx + 1, remaining, turn)
        else:
            dp(idx, remaining - idx ^ 2, not turn) and dp(idx + 1, remaining, turn)
            
            
        300 * 10 ** 5 * 2
        
        1500 * 10 ** 5
        
        15 * 10 ** 7
        
        do it in a top down because it's a fibonacci pattern/ stairs thing
        
        
        for stone:
            for every sqrt:
                remaining = stone - sqrt ** 2
                
                if remaining == 0
                    winner = 1
                else
                winner = winner or (winner[root ** 2] and not winner[remaining])
                
        this would reduce the time complexity to
        
        3 * 10 ** 7
        
        
        the above solution still doesn't pass but it has given us the most important insight
        since winner[root ** 2] is always going to be true
        we only have to worry about the remaining being false
        
        
        rewording it gives us, for index that is false we can then go to the indices that are
        remaining + root ** 2 and make them true
        
        for the indices that are true we just skip over them because we can't be sure what to make of them
        
        
        s
        """
        winner = [0] * max((n + 1), 3)
        winner[1], winner[2] = 1, 0
        
        
        for stone in range(2, n + 1):
            if winner[stone] == 1 or (int(math.sqrt(stone)) ** 2 == stone):
                winner[stone] = 1
                continue
                
            remain = n - stone
            for root in range(1, int(math.sqrt(remain)) + 1):
                winner[root ** 2 + stone] = 1
                
        return winner[n]
        
        
#         for stone in range(1, n + 1):
#             for root in range(1, int(math.sqrt(stone)) + 1):
#                 remaining = stone - (root ** 2)
                
#                 if remaining:
#                     winner[stone] = winner[stone] | (1 - winner[remaining])
#                 else:
#                     winner[stone] = 1
                    
#         return winner[n]
        
#         @lru_cache(None)
#         def dp(remaining, turn):
#             if remaining <= 0:
#                 return 1 - turn
            
#             answer = 1 - turn
#             for num in range(int(math.sqrt(remaining)), 0, -1):
#                 next_ = dp(max(remaining - (num ** 2), 0), 1 - turn)
#                 if turn:
#                     answer =  next_ | answer
#                 else:
#                     answer = next_ & answer
                
#             return answer
            
#         return dp(n, 1) == 1
                
        
        