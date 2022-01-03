class Solution:
    def recur(self, n, k , cnt):
        rev_count = cnt
        if n == 1:
            return rev_count % 2
        elif k > 2 ** (n - 1) / 2:
            return self.recur(n - 1, k - (2 ** (n - 1)) / 2 , rev_count + 1)
        else:
            return self.recur(n - 1, k , rev_count)
        
    
    def kthGrammar(self, n: int, k: int) -> int:
        return self.recur(n, k , 0)