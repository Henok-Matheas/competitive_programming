class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        n people
        
        if judge
        
        trust nobody
        everybody trust him
        exactly one person
        """
        
        """
        one approach
        
        count the no of people who trust one person if it's n- 1 then it's a valid candidate
        we also count the number of people who I trust, it needs to be zero
        
        if we can find one person then thats the only person
        
        how to implement
        
        have two list of sets
        trustme
        itrust
        
        for every node we check if the leng of trustme == n - 1 and itrust == 0
        
        in this case we can have a list of counts
        
        and there also needs to be only one person who satisfies this, well if
        """
        trustme = [0] * (n + 1)
        itrust = [0] * (n + 1)
        
        for truster, trustee in trust:
            trustme[trustee] += 1
            itrust[truster] += 1
            
        for node in range(1, n + 1):
            if trustme[node] == n - 1 and itrust[node] == 0:
                return node
        
        return -1