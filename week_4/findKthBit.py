class Solution:
    def recur(self, n):
        if n == 1:
            return "0"
        KthBit = self.recur(n - 1)
        
        final = ""
        dicti = {"1":"0","0":"1"}
        for i in KthBit[::-1]:
            final += dicti[i]
        return KthBit + "1" + final
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.recur(n)[k - 1]
        
        