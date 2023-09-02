class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        
        string 
        dictionary
        
        so its a basic dp then
        
        
        using n ** 3 method we know every part which is in dictionary.
        
        
        after that we want to know the highest combination of non overlapping strings
        
        
        so to do that in an n ** 2 way we find all the substrings which are in dictionary and while doing that we also try to find the highest combination of non overlapping strings up until the ending point
                
        """
        word_set = set(dictionary)
        sub_count = [0] * (len(s))
        for start in range(len(s)):
            prev = sub_count[start - 1] if start else 0
            maxim = prev
            for end in range(start, len(s)):
                word = s[start: end + 1]
                if word in word_set:
                    maxim = max(maxim, prev + end - start + 1)
                sub_count[end] = max(maxim, sub_count[end])
                
                
        return len(s) - sub_count[len(s) - 1]