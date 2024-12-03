class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        so if the count of other rabbits such as me is n
        
        then the count of of n should be n + 1
        if it's lower then all of them are their own colors
        
        if it's higher we will take n + 1 from it and say these have the same color and the remaining will be treated again which means
        
        if count of n is n + 1 we will do total + 1
        
        if count of n is lower we do:
        
        each is it's own so (n + 1) * count of n
        
        
        so in mathematical terms
        
        we do (counts[n] // (n + 1)) * (n + 1)
        rem = counts[n] % (n + 1)
        
        for the reaminders we do (n + 1) * rem
        """
        total = 0
        counts = Counter(answers)
        
        for size in counts:
            group = counts[size] // (size + 1)
            total += group * (size + 1)
            
            rem = counts[size] % (size + 1)
            
            total += min(rem, 1) * (size + 1)
            
        return total