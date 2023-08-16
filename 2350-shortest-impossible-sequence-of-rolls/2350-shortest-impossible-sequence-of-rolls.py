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
        sequence = {idx: -1 for idx in range(1, k + 1)}
        heap = [[1, -1, idx] for idx in range(1, k + 1)]
        
        for idx in reversed(range(len(rolls))):
            roll = rolls[idx]
            while heap and (sequence[heap[0][2]] != heap[0][1] or heap[0][2] == roll and heap[0][0] == 1):
                heapq.heappop(heap)
                
            seq, index, val = heap[0] if heap else [1, 0, roll]
            
            sequence[roll] = idx
            heapq.heappush(heap, [seq + 1, idx, roll])
            
        while heap and sequence[heap[0][2]] != heap[0][1]:
            heapq.heappop(heap)
            
        return heap[0][0]