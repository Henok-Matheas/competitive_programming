class Solution:
    def minSteps(self, n: int) -> int:
        """
        only A present initially
        
        operations
            - copy all characters
            - paste previously copied characters
            
            
        min number of operations to reach n characters
        
        so basically the question can be simplified to
        how many copy and paste to reach n
        
        I think this can be thought of as a dp question since n <= 1000
        
        
        if you have copied then you have to paste
        
        so if the current operation is copy then the next operation is paste
        
        when you pasted, you have the option copy with the previous copy or copy with the new one
        
        
        copy
        
        
        1, 1
        
        1 + copy
        
        
        2, 2, 3
        
        2 1, 2
        
        
        when on copy
        
        if current number is different from copy
            copy with new one
            
            copy = 1 + dp(number, number, paste)
            
            
        return copy
        
        
        
        paste(number, copy_size)
        if number == n:
        return 0
        
        return 1 + (number + copy_size, copy_size, copy)
            
        return copy
            
        
                for every dp return the minimum between copy and paste and paste with old copy
        return min(2 + dp(1 + copy, 1 + copy), 1 + dp(1 + copy, copy))
        
        
        for a number we have what we have copied so far
        
        dp(number, copy):
            if number > n:
                return float
            if number == n:
                return 0
                
                
        6 / 2
        
        3
        
        3 + 2
        
        8 // 2
        
        4 2
        
        
        4 // 2
        
        
                
            
        
        """
        if n == 1:
            return 0
        
        total = 0
        
        for div in range(2, int(math.sqrt(n)) + 1):
            while n and n % div == 0:
                total += div
                n //= div
                
        return total + (n if n > 1 else 0)
                
                