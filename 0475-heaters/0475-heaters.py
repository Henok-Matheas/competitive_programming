class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        what if we do binary search over the answer?
        
        the solution will be nlog(val highest - lowest)
        
        3 * 10 ** 4
        8 * 3
        
        300 * 10 ** 4
        
        3 * 10 ** 6
        
        WORKS BUT TLE
        
        so we can do for every house we find the lowest heater which is right next to house and also 
        the highest heater left to the current house
        
        solution
        
        left_list = [10 ** 9] * len(houses)
        right = [10 ssss777777s)
        
        for house in houses:
            while idx < len(heaters) and heaters[idx] < house:
            idx += 1
            
            if idx < len(heaters):
            
        """
        houses.sort()
        heaters.sort()
        dists = [10 ** 9] * len(houses)
        idx = len(heaters) - 1
        
        
        for house_idx in range(len(houses) - 1, -1, -1):
            house = houses[house_idx]
            while idx > -1 and heaters[idx] > house:
                idx -= 1
            
            if idx == -1:
                idx += 1
            dists[house_idx] = abs(house - heaters[idx])
                
        idx = 0
        for house_idx, house in enumerate(houses):
            while idx < len(heaters) and heaters[idx] < house:
                idx += 1
                
            if idx == len(heaters):
                idx -= 1
            dists[house_idx] = min(dists[house_idx], abs(heaters[idx] - house))
                
        
        return max(dists)