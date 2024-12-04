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
        idx, ans = 0, 0
        
        for house_idx, house in enumerate(houses):
            min_rad = 10 ** 9
            while idx < len(heaters) and heaters[idx] < house:
                min_rad = abs(house - heaters[idx])
                idx += 1   
            if idx == len(heaters):
                idx -= 1
            min_rad = min(min_rad, abs(heaters[idx] - house))
            
            if idx > 0:
                min_rad = min(min_rad, abs(heaters[idx - 1] - house))
            
            ans = max(ans, min_rad)
        
        return ans