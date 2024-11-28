class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sums = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            sums[start] += 1 if direction else -1
            sums[end + 1] -= 1 if direction else -1
            
        final = []
        tot = 0
        
        for idx in range(len(s)):
            tot += sums[idx]
            order = ord(s[idx]) - ord("a")
            order = (order + tot) % 26
            char = chr(ord("a") + order)
            final.append(char)
            
        return "".join(final)