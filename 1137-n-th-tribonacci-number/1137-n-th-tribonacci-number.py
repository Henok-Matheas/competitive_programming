class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]
        
        for idx in range(3, n + 1):
            trib.append(trib[idx - 1] + trib[idx - 2] + trib[idx - 3])
            
        return trib[n]