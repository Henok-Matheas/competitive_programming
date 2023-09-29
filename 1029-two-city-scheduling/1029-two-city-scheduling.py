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
        costs.sort(key= lambda cost: cost[0] - cost[1])
        
        return sum([city1 for (city1, city2) in costs[:len(costs) // 2]]) + sum([city2 for (city1, city2) in costs[len(costs) // 2:]])