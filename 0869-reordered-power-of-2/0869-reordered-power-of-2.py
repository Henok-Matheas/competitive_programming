class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        have actual number
        
        have some given number
        
        while given number <= n:
        number *= 2
        
        if the sorted() of the given number and n is the same return
        
        """
        num = list(str(n))
        num.sort()
        
        given = 1
        POWER = 2
        MAXIM = 10 ** 9 + 1
        
        while given < MAXIM:
            curr = list(sorted(str(given)))
            if curr == num:
                return True
            given *= POWER
                
        return False