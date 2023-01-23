class Solution:
    def checkPartitioning(self, s: str) -> bool:
        """
        bruteforce
        
        we can have two four loops
        which take care of the first and the second part
        
        the third part we just have to find if it can be a palindrome or not
        """
        """
        we find the end of the first partition first
        
        for all the ends we try to find another partition for the second part
        
        then we found the last part
        """
        @cache
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            
            return isPalindrome(left + 1, right - 1)
        
        for firstend in range(len(s) - 2):
            if isPalindrome(0, firstend):
                for secondend in range(firstend + 1, len(s) - 1):
                    if isPalindrome(firstend + 1, secondend) and isPalindrome(secondend + 1, len(s) - 1):
                        return True
        
        
        return False