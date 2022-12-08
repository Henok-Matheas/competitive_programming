class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        """
        trie of digits, with one or zero
        for every number do this, then finally for every number look in the trie for a perfect xor.
        """
        ## index
        trie = {}
        maxim = 0
        
        
        for num in nums:
            working = trie
            for idx in reversed(range(32)):
                curr = 1 if num & 1 << idx else 0
                
                if curr not in working:
                    working[curr] = {}
                    
                working = working[curr]
                
        for num in nums:
            curr_max = 0
            working = trie
            for idx in reversed(range(32)):
                curr = 1 if num & 1 << idx else 0
                opposite = 0 if curr else 1
                
                if opposite in working:
                    curr_max |= 1 << idx
                    working = working[opposite]
                
                else:
                    working = working[curr]
                
            maxim = max(maxim, curr_max)
                
        return maxim