class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        the simplest version of the problem is
        if we are given a list of letters
        find the substrings which are a permtuation of the letters
        """
        
        """
        it's the same as sliding window minimum
        
        we want to find the different substrings which have the given elements and nothing else
        
        if we find sth else we break
        
        for every letter
        we try to go by size of the given words
        
        if it's 3 and curr idx is 0 the next value is 3 then we try if that value is in 
        
        if the current idx is visited we continue
        
        we jump as much as possible until we are out of bounds or if the current word is not in words
        
        [0,1,2,3,4] [] 2
        """
        count = Counter(words)
        needed = set(words)
        visited = set([])
        jump = len(words[0])
        answer= []
        
        exist = defaultdict(str)
        
        for start in range(len(s)):
            if start in visited:
                continue
            curr_count = defaultdict(int)
            have = set([])
            for end in range(start, len(s) - jump + 1, jump):
                visited.add(end)
                current = s[end: end + jump]
                if current not in count:
                    break
                
                exist[end] = current
                    
                curr_count[current] += 1
                
                if count[current] <= curr_count[current]:
                    have.add(current)
                actual_end = end + jump
                while len(have) == len(needed):
                    left = exist[start]
                    ## way of checking if the the current start to end only includes
                    if (actual_end - start) // jump == len(words):
                        answer.append(start)
                    curr_count[left] -= 1
                    if count[left] > curr_count[left]:
                        have.remove(left)
                        
                    start += jump
                    
        return answer