class Solution:
    def numTrees(self, n: int) -> int:
        """
        IDEA:
        
        if we are asked the numTrees(n)
        then the basic thing is we have to place all the nodes from 1 - n as the root and then find the total
        so it's basically
        numTrees(n) = place(1, n) + place(2, n) + place(3, n) ..... + place(n, n)
        
        to calculaute the number of trees when we place a node as a root node is the number of trees in the left branch multiplied by the number of trees in the right branch.
        
        place(x, n) = numTrees(x - 1) * numTrees(n - x)
        
        one of the main ideas behind these two formulas is that the actual nodes in the subbranch don't actually matter
        
        if we are asked numTrees(2) wether we are finding for the nodes (1, 2), (2, 3) or (9, 100) doesn't matter it's all the same numTrees(2) will always be equal to 2, and it's the same for numTrees(n).
        
        now when we combine these two ideas we arrive at.
        
        numTrees(n) = place(1, n) = numTrees(1 - 1) * numTrees(n - 1)
                    + place(2, n) = numTrees(2 - 1) * numTrees(n - 2)
                    + place(3, n) = numTrees(3 - 1) * numTrees(n - 3)
                    .
                    .
                    .
                    + place(n, n) = numTrees(n - 1) * numTrees(n - n)
                    
                    
        since we don't know numTrees(n - 1) at first, we change this formula in such a way that the smalles sizes will be cacluated first
        
        so to find numTrees(n) we go from numTrees(1) -- numTrees(n)
        
        numTrees(0) = 0
        numTrees(1) = 1
        numTrees(2) = place(1, 2) = numTrees(1 - 1) * numTrees(2 - 1) = 1
                    + place(2, 2) = numTrees(2 - 1) * numTrees(2 - 2) = 1
                    = 2
        numTrees(3) = place(1, 3) = numTrees(1 - 1) * numTrees(3 - 1) = 2
                    + place(2, 3) = numTrees(2 - 1) * numTrees(3 - 2) = 1
                    + place(3, 3) = numTrees(3 - 1) * numTrees(3 - 3) = 2
                    = 5
                    
        we do this until we arrive at numTrees(n)
        
        """
        trees = [0] * (n + 1)
        trees[0] = 1
        trees[1] = 1
        
        for size in range(2, n + 1):
            for node in range(1, size + 1):
                trees[size] += trees[node - 1] * trees[size - node]
                
        return trees[n]