class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        normal checking would take n ** 2 time complexity
        
        how can we do it in a fast way
        
        
        we can try to find where they are unequal
        then the only two possible answers is deleting the last or the first
        we check if it can be a palindrome under those cases if not remove
        
        
        """
        n = len(s) - 1
        def isPalindrome(start, end):
            curr = s[start: end + 1]
            return curr == curr[::-1]
        
        for idx in range(len(s)):
            if s[idx] != s[~idx]:
                return isPalindrome(idx, n - idx - 1) or isPalindrome(idx + 1, n - idx)
        
        return True