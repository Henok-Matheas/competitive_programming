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
        
        
        n = houses
        m = heaters
        
        nlogn, (n + m)log(n + m)
        time complexity = (n + m)log(n + m)
        space complexity = n + m 
        """
        heaters.sort()
        radius=0
        for i,c in enumerate(houses):
            if c>heaters[-1]:
                idx=len(heaters)-1
            else:
                idx=bisect.bisect_left(heaters,c)
            f_elemnt=heaters[idx]
            if idx==0:
                s_element=heaters[idx]
            else:
                s_element=heaters[idx-1]
            m=min(abs(f_elemnt-c),abs(s_element-c))
            radius=max(m,radius)
        return radius

            
        
        