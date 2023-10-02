class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        defaultdict
        
        for char in s:
        
        """
        
        counts = Counter(s)
        
        
        for char in t:
            if char in counts and counts[char]:
                counts[char] -= 1
                
        return sum(counts.values())