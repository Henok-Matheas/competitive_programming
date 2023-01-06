class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        stores = n icecreams
        costs = cost i = price of buying icecream i
        coins = amount to spend
        """
        costs.sort()
        
        for index, cost in enumerate(costs):
            coins -= cost
            if coins < 0:
                return index
            
        return len(costs)