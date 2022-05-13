class Solution:
    def minWindow(self, s: str, t: str) -> str:
        relevant = []
        to_include = defaultdict(int)
        have = defaultdict(int)
        deque = collections.deque()
        
        for char in t:
            to_include[char] += 1
            
        havent = copy.deepcopy(to_include)
        i, j = 0, 0
        
        
        while i < len(s) and s[i] not in to_include:
                i += 1
                j += 1
        
        deque = collections.deque()
        while j < len(s) and havent:
            if s[j] in to_include:
                deque.append(j)
                havent[s[j]] -= 1
                if havent[s[j]] <= 0:
                    havent.pop(s[j])
                have[s[j]] += 1
            j += 1
        j -= 1
        
        answer = s[i:j + 1] if not havent else ""
        
        if not answer:
            return answer
        while j < len(s):
            while deque and have[s[deque[0]]] > to_include[s[deque[0]]]:
                have[s[deque[0]]] -= 1
                deque.popleft()
                
            answer = s[deque[0]:deque[-1] + 1] if deque and deque[-1] - deque[0] < len(answer) else answer
            
            j = deque[-1] + 1
            while j < len(s) and deque and have[s[deque[0]]] <= to_include[s[deque[0]]]:
                if s[j] in to_include:
                    deque.append(j)
                    have[s[j]] += 1
                    if have[s[deque[0]]] > to_include[s[deque[0]]]:
                        break
                j += 1
            answer = s[deque[0]:deque[-1] + 1] if deque and deque[-1] - deque[0] < len(answer) else answer
        return answer
            
        