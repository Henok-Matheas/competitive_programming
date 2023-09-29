class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        interview 2n people
        
        we want to have n people in both cities.
        
        and we want to make the cost of flying as minimum as possible.
        
        it's like a dp sum question but simplifying it becomes for every inde
        
        idx, n, n
        100, 50, 50
        2.5 * 10 ** 5
        
        
        """
        @lru_cache(None)
        def dp(idx, city1, city2):
            if idx == len(costs):
                return 0
            
            fly1 = fly2 = float("inf")
            
            if city1:
                fly1 = costs[idx][0] + dp(idx + 1, city1 - 1, city2)
                
            if city2:
                fly2 = costs[idx][1] + dp(idx + 1, city1, city2 - 1)
            
            return min(fly1, fly2)
        
        
        return dp(0, len(costs) // 2, len(costs) // 2)