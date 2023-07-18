class Solution:
    def integerBreak(self, n: int) -> int:
        """
        this is coin change but with the slight change of maximizing the product instead of minimizing the amount of coins.
        """
        products = [0] * (n + 1)
        products[1] = 1
        
        
        for product in range(2, n + 1):
            for num in range(1, product):
                products[product] = max(products[product], max(products[num], num) * max(products[product - num], product - num) )
                
        return products[n]