class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        """
        k candies are sold
        tastiness of k candies = min difference b/n prices of candies in the basket
        
        maximize tastiness
        1, 2, 5, 8, 13, 21
        1, 3, 8, 16, 29, 50
                     13
                     0, 20
                     10
                     9
        k = 4
        
        nlogn
        
        so we guess a difference and try to see if we can include the elements from the price to make it a reality if we can then atleast this works
        if we can't then we have to look for a lower difference
        
        solution
        left, right = 0, max_diff
        max_tastiness = 0
        while left <= right:
        mid
        is_valid()
        
        if is_valid
        maxim = mid
        left = mid + 1
        else
        right = mid - 1
        
        is_valid(diff)
        have a left and right
        if right - left >= diff
        total -= 1
        else:
        return False
        
        10 * 10 * 10
        
        return True
        """
        def is_valid(diff, num):
            num -= 1 ## the first element is taken by default
            left, right = 0, 0
            while num and left < len(price):
                while num and right < len(price) and price[right] - price[left] < diff:
                    right += 1
                    
                if right < len(price):
                    num -= 1 
                    left = right
                else:
                    return False
            return num <= 0
        
        price.sort()
        left, right = 0, price[-1] - price[0]
        max_tastiness = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if is_valid(mid, k):
                max_tastiness = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_tastiness
        