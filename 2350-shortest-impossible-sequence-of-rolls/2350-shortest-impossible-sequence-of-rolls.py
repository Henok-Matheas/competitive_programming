class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        """
        rolls
        k
        
        the highest is min(counts) + 1
        
        keep in mind that you are only asked for length
        
        
        the orientation matters as well.
        
        
        so maybe we can do a 
        
        [1, 2, 1, 2]
        
        [4, 2, 1, 2, 3, 3, 2, 4, 1, 4, 1, 3]
        
        
        4  1 2
           2
           3
           4
          
        maybe for all k we do a dp on them
        
        
        the dp just checks what if any characters are missing for an index if not it goes dp again for the indexes.
        
        now all we have to do is 
        
        
        for every index when going forwards we pick the minimum from k ones and we add the minimum + 1 for that k, this means that for the current index the number of shortest 
        
        we need to know how to replace from a heap, basically remove and add.
        
        so before doing ath, when removing from a heap we remove the unupdated ones.
        """
        answer = 1
        sequence = set()
        for roll in rolls:
            sequence.add(roll)
            if len(sequence) == k:
                answer += 1
                sequence.clear()
                
        return answer