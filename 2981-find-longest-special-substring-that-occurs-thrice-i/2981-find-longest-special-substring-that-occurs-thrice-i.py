class Solution:
    def maximumLength(self, s: str) -> int:
        """
        first we gather the special char count in a dict
        
        then we have three scenarios
        a: [5, 5, 5] then answer if 5
        b: [5, 5] then answer if 4
        c: [5, 4] then answer if 4
        d: [5, 3] then answer is 3
        
        basically if we just need the three largest counts
        
        if all 3 are equal then max is that
        
        if the difference between the first and second is 1 then return the second variable
        
        else: then we return the maxim - 2
        
        
        to construct the dicti thing
        
        we will have a counting dict thing but
        
        have a for loop and when you find a value that is less than curr then we use insert
        """
        maxim = -1
        count = 0
        counts = [[] for _ in range(26)]
        
        def add_counts(char, count):
            ## adds count into counts array
            char_idx = ord(char) - ord("a")
            target_idx = len(counts[char_idx])
            for idx, val in enumerate(counts[char_idx]):
                if val < count:
                    target_idx = idx
                    break
            counts[char_idx].insert(target_idx, count)
            
            while len(counts[char_idx]) > 3:
                counts[char_idx].pop()
        
        ## gather consecutive char count
        for idx in range(len(s)):
            count += 1
            if idx + 1 == len(s) or s[idx] != s[idx + 1]:
                add_counts(s[idx], count)
                count = 0
            
        ## finds the maxim    
        for curr in counts:
            if not len(curr):
                continue
            
            ## handle when the length is 3 and all are equal
            if len(curr) == 3 and curr[0] == curr[1] == curr[2]:
                maxim = max(maxim, curr[0])
            
            ## we have to handle when we have [1, 1] and length is 2 if the length is greater than 2 a
            elif len(curr) == 2 and curr[0] == curr[1] == 1:
                continue
                
            ## handle when length is > 1 and the difference between the first and second is 1
            elif len(curr) > 1 and curr[0] - curr[1] <= 1:
                maxim = max(maxim , curr[0] - 1)
            ## handle when it's ath else
            elif curr[0] - 2:
                maxim = max(maxim, curr[0] - 2)
            
            
                
        return maxim
        