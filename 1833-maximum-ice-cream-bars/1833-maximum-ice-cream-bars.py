class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        stores = n icecreams
        costs = cost i = price of buying icecream i
        coins = amount to spend
        """
        total = 0
        costs.sort()
        
        for cost in costs:
            if cost > coins:
                continue
            coins -= cost
            total += 1
            
        return total