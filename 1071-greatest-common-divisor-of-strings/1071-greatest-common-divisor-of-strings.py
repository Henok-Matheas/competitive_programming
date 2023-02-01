
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""
        
        max_length = 0
        
        for idx in range(min(len(str1), len(str2))):
            if len(str1) % (idx + 1) == 0 and len(str2) % (idx + 1) == 0:
                max_length = idx + 1

        return str1[:max_length]