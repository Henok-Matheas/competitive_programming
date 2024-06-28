class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """
        
        n cities
        
        roads = [city1, city2]
        
        importance of a road = val[city1] + val[city2]
        
        
        maximum total importance
        
        
        what if we give the highest value to the most connected one?
        
        this means this question is a topological sorting question.
        
        
        
        top sort defnition?
        
        create a connection array to count the number of times a node appears
        
        
        connection dictionary = [0] * n
        
        for cities in roads:
        connection[cities] += 1
        
        
        count_list = create a zip of dictionary
        
        for val, 
        
        """
        
        connection = [0] * n
        total = 0
        
        for city1, city2 in roads:
            connection[city1] += 1
            connection[city2] += 1
            
        connection.sort()
        
        for idx, count in enumerate(connection):
            total += (idx + 1) * count
            
        return total
        
            