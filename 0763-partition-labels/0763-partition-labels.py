class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        have = set()
        left = 0
        output = []
        
        """
        have a dictionary and for every index if the index is less than the last end
        then we continue else since we are starting again
        
        or rather than making it when it is greater we can do it when it is equal
        
        """
        
        ends = {}
        start = 0
        end = 0
        output = []
        for idx in range(len(s)):
            ends[s[idx]] = idx
        
        for idx in range(len(s)):
            end = max(end, ends[s[idx]])
            if idx == end:
                output.append(idx - start + 1)
                start = end + 1
        return output