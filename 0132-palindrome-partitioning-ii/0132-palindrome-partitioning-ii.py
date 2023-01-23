class Solution:
    def minCut(self, s: str) -> int:
        @cache
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            
            return isPalindrome(left + 1, right - 1)
        
        @cache
        def dp(start):
            if start == len(s):
                return -1
            minim = float("inf")
            for idx in range(start, len(s)):
                if isPalindrome(start, idx):
                    minim = min(minim,1 + dp(idx + 1))
                    
            return minim
        
        return dp(0)