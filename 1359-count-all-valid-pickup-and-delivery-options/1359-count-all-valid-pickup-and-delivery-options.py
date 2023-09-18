class Solution:
    def countOrders(self, n: int) -> int:
        """
        pickup and delivery
        
        1000!
        
        seems like a simple math question of permtuation
        
        in the first place only opening is possible which means we have n possible options
        
        in the next place we can close it or have another open
        
        closing will let us move to the next index
        
        
        we only need to know the number of open ones, and the number of remaining
        
        
        rem, open
        
        2
        
        2, 0
        
        if there are any pickups possible
        
        
        pickups_remaining, deliveries_remaining
        
        dp(2, 0)
        
        2 * dp(1, 1)
        
        
        dp(1, 1) = 3
        
        1 * dp(0, 2) = 2
        
        1 * dp(1, 0) = 1
        
        
        
        
        
        dp(1, 0) = 1
        
        
        dp(0, 2) = 2
        
            
        
        
        
        total = 0
        if there are any pickups:
            total += pickups * dp()
            pickupups -= 1
            deliveries += 1
            
        if there are any deliveries:
            deliver which means reduce delivereies by one.
            total += deliveries * dp()
            deliveries -= 1
            
        """
        
        
        @lru_cache(None)
        def dp(pickups, deliveries):
            total = 0
            
            if pickups:
                total += pickups * dp(pickups - 1, deliveries + 1)
                
            if deliveries:
                total += deliveries * dp(pickups, deliveries - 1)
            
            
            return max(total % (10 ** 9 + 7), 1)
        
        return dp(n, 0) % (10 ** 9 + 7)