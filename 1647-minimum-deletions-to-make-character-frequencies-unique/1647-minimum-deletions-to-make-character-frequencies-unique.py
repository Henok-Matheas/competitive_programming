class Solution:
    def minDeletions(self, s: str) -> int:
        """
        s is good if char frequency of two chars doesn't match
        
        return min operations to make s good
        
        in one operation you can delete a single char
        """
        
        """
        step1: freqcount
        step2: sort the freq
        step3 for every freq
                stepp4: pop a freq that isn't held
                step5: total += the difference between the popped and self
        
        """
        counts = [count for count in Counter(s).values()]
        counts.sort()
        available = []
        last = 1
        deleted = 0
        for count in counts:
            while last <= count:
                available.append(last)
                last += 1
                
            ## if there is
            unique = available.pop() if available else 0
            
            deleted += count - unique
                
        return deleted 
            ## if the current
                
            
            
        
        