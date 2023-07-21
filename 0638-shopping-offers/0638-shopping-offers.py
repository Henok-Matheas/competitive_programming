class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        """
        n offers. and some special ones
        price, needs, special
        special[i][j] = no of j items in ith offer
        special[i][n] = price of offer
        
        lowest price for no of items given. can't buy more items than wanted
        
        price = [2, 5]
        needs = [3, 2]
        special = [
        [3, 0 , 5]
        [1, 2, 10]
        ]
        
        buy speical offer 1 -> 1 time
        
        
        we convert the price to go into the special thing 
        
        then it becomes an unbounded knapsack problem
        
        we can take this special offer or the other offer
        
        """
        
        
        size = len(needs)
        
        for idx in range(size):
            deal = [0] * (size + 1)
            deal[idx] = 1
            deal[size] = price[idx]
            
            special.append(deal)
        
        @lru_cache(None)
        def dp(idx, needs):
            if idx == len(special):
                return float("inf")
            
            if list(needs) == [0] * size:
                return 0
            
            for need in needs:
                if need < 0:
                    return float("inf")
                
            copy_needs = list(needs)        
            
            for amount in range(size):
                copy_needs[amount] -= special[idx][amount]
             
            copy_needs = tuple(copy_needs)
            take = special[idx][-1] + dp(idx, copy_needs)
                
            skip = dp(idx + 1, needs)
            
            return min(skip, take)
        
        
        answer = dp(0, tuple(needs))
        
        return answer