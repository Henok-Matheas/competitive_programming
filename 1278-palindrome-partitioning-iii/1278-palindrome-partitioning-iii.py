class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        same as the other partitioning
        
        we just need to have a k value to store how many we have changed, if the number we have changed is less than we return true
        
        so the ispalindrome function returns the amount we had to change to make it a function
        """
        
        """
        the different thing is that we divide the string into k parts, exactly
        
        so how to do that
        
        we can change the dp function to account for that.
        
        if the current is a palindrome we add k by one and call the dp function
        
        if the len == s and k == k we then also return 0
        
        if k overtakes k w return float("inf")
        
        if it's equal to len(s) and k is less also return float("inf")
        """
        
        @cache
        def isPalindrome(left, right):
            if left >= right:
                return 0
            unequal = 0
            if s[left] != s[right]:
                unequal += 1
            return unequal + isPalindrome(left + 1, right - 1)
        
        @cache
        def dp(part, start):
            if start == len(s):
                if part == k:
                    return 0
                return float("inf")
            
            if part >= k:
                return float("inf")
            
            minim = float("inf")
            for idx in range(start, len(s)):
                minim= min(minim, isPalindrome(start, idx) + dp(part + 1, idx + 1))
                
            return minim
        
        return dp(0, 0)