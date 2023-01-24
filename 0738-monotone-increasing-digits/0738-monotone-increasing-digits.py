class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        we want to create an increasing number
        
        so for every number if it's greater than th
        """
        
        final = [0]
        string = str(n)
        for idx in range(len(string)):
            num = int(string[idx] )
            if num >= final[-1]:
                final.append(num)
                continue
            next_ = 9
            for rev in range(len(final) - 1, 0, -1):
                final[rev] -= 1
                curr, prev = final[rev], final[rev - 1]
                if not(prev <= curr <= next_):
                    final[rev] = 9
                    next_ = final[rev]
                else:
                    break
                    
            final += [9] * (len(string) - idx)
            break
            
            
        return int("".join(list(map(str, final))))