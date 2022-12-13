class Solution:
    def numberOfWays(self, s: str) -> int:
        total = 0
        left = [0,0]
        right = [s.count("0"),s.count("1")]
        
        for middle in range(len(s)):
            current = int(s[middle])
            right[current] -= 1
            
            opposite = (current + 1) % len(left)
            total += left[opposite] * right[opposite]
            
            left[current] += 1
            
        return total
        