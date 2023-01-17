class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        we can use a pointer to find the point at which the string changes from zero to one
        
        how do we do that?
        
        first the pointer points at zero meaning that we want all to be one
        for all to be one all zeroes need to be one, so we count them
        
        then we move the pointer and if the current value is one
        we want to change it to zero so it's cost is added
        we also sub from right cost
        """
        left = 0
        right = s.count("0")
        minim = left + right
        
        for char in s:
            if char == "0":
                right -= 1
            else:
                left += 1
            
            minim = min(minim, left + right)
                
        
        return minim
        