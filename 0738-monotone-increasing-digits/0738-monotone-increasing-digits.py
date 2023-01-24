class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        we want to create an increasing number
        
        so for every number if it's greater than th
        """
        
        final = [int(char) for char in str(n)]
        marker = len(final)
        for idx in range(len(final) - 1, 0, -1):
            curr, prev = final[idx], final[idx - 1]
            if curr < prev:
                marker = idx
                final[idx - 1] -= 1
                
        for idx in range(marker, len(final)):
            final[idx] = 9
            
            
        return int("".join(list(map(str, final))))