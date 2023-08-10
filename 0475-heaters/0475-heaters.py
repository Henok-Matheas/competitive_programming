class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        we can do it using heap
        
        when all the houses are visited we stop
        
        
        so we add the heaters into the house list
        
        make it a set.
        
        
        then the heaters are the begining of the 
        
        
        visited is houses before the adding of the heaters
        
        the heap holds (radius, idx)
        house_
        initially the heap is (0, idx of the heaters after they get added to the houses)
        
        
        while house_set exists and heap:
            remove = radius, index
            
            max_radisu = max
            
            if index in house_set:
                remove it from house_set
                
        
        return max_radius
        
        
        house_set = set(house)
        """
        
        house_set = set(houses)
        heaters_set = set(heaters)
        houses  = list(set(houses + heaters))
        houses.sort()
        index_changes = [-1, 1]
        min_radius = 0
        
        heap = []
        
        for idx, val in enumerate(houses):
            if val in heaters_set:
                heap.append([0, idx])
                
                
                
        while heap and house_set:
            radius, index = heapq.heappop(heap)
            
            if houses[index] in house_set:
                house_set.remove(houses[index])
                min_radius = max(radius, min_radius)
                
                
            for change in index_changes:
                if 0 <= index + change < len(houses) and houses[index + change] in house_set:
                    new_radius = radius + abs(houses[index + change] - houses[index])
                    heapq.heappush(heap, [new_radius, index + change])
                    
        return min_radius

            
            
        
        