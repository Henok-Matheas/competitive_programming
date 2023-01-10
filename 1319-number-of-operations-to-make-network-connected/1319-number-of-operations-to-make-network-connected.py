class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        n computers 0 - (n - 1)
        connections[i] = [a, b]
        complete connection
        you can make two computers directly connected
        
        you can remove connections between two computers.
        then you can make other two computers connected.
        
        minimum number of such operations needed to make the computers completely connected
        """
        
        
        """
        asking as to create complete connection with minimal removal
        
        condition of removal?
        if a connection is redundant, meaning that it is connecting nodes
        which are already connected then it is not useful
        
        how to find out redundant connections?
        - go through each connection and if the connection connecting
        nodes is a redundant one then don't add it?
        
        problem?
        whould order of connections be a problem??
        I don't think so
        
        finally if the number of extra connections is less than the number of distinct regions then return -1
        
        if number of connections is greater or equal return the number of regions
        """
        
        """
        algo unionfind()
        
        step1 for every connection in connections
                - is conn redundant if so add to redundant count
                - if not connect the two and reduce the count of regions
        step2 is count of redundant < regions: return -1
                - if not return region count
                
        """
        def find(node):
            if parents[node] == node:
                return node
            parents[node] = find(parents[node])
            return parents[node]
            
        
        
        parents = [idx for idx in range(n)]
        redundant = 0
        regions = n - 1
        for node1, node2 in connections:
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                ## same regions
                redundant += 1
            else:
                parents[parent1] = parent2
                regions -= 1
            
        print(regions, redundant, n)
        if redundant < regions:
            return -1
        
        return regions
                