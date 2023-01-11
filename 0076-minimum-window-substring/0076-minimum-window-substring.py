class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        if this element is needed or wanted we add into the set
        if the count is satisfactory we discard from the needed set
        
        when the needed set is empty
        we have a probable answer
        then we remove elements from the last
        
        if the count is less than needed we add it into needed list
        """
        
        """
        needed set=
        two pointers
        minimum holds the starting and ending points
        """
        
        counts = Counter(t)
        current_count = defaultdict(int)
        needed = set(list(t))
        start = 0
        maxim = [-float("inf"), float("inf")]
        for end, char in enumerate(list(s)):
            if char not in counts:
                continue
                
            current_count[char] += 1
            
            if counts[char] <= current_count[char]:
                needed.discard(char)
                
            while not needed:
                maxim = min(maxim, [start, end], key = lambda lst: [lst[1] - lst[0]])
                left = s[start]
                if left  in counts:
                    current_count[left] -= 1
                    if counts[left] > current_count[left]:
                        needed.add(left)

                start += 1
                
        if maxim[0] == -float("inf"):
            return ""
        
        return s[maxim[0]: maxim[1] + 1]
        