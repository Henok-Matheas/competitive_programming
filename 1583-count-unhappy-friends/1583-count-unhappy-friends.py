class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        pref
        
        pairs
        
        unhappiness
        
        x - y
        
        u - v
        
        x pref u over y
        u pref x over v
        
        
        number of unhappy friends
        
        pos[y]
        
        
        [0, 1]
        [2, 3]
        
        
        what this means is that for every node we need to know the indexes of it's children so as to compare where they are found
        
        so we need indexes = 
        
        for idx, pref in prefs:
            indexes[idx] = [0] * len(pref)
            
            for index, node in pref:
                indexes[node] = index
                
        pair = [] * n
        
        for pairs:
            pair[pair1] = pair2
            pair[pair2] = pair1
        
        
        for pair1, pair2 in pairs
        
        for u in range(index[pair1][pair2]):
            v = pair[u]
            if index[u][pair1] < index[u][v]:
            count += 1
            
        do this for pair2 as well
        """
        count = 0
        pair = [0] * (n)
        indexes = [[0] * n for _ in range(n)]
        
        for idx, preference in enumerate(preferences):
            for index, node in enumerate(preference):
                indexes[idx][node] = index
                
        for pair1, pair2 in pairs:
            pair[pair1] = pair2
            pair[pair2] = pair1
            
            
        def find_unhappy(x, y):
            for idx in range(indexes[x][y]):
                u = preferences[x][idx]
                v = pair[u]
                
                if indexes[u][x] < indexes[u][v]:
                    return 1
                    
            return 0
            
        for x, y in pairs:
            count += find_unhappy(x, y)
            count += find_unhappy(y, x)
                    
        return count