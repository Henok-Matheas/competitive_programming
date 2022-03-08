class Solution:

    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""
        stri = []
        for letter in palindrome:
            stri.append(letter)
        rng = len(palindrome) // 2
        i = 0
        while i < len(palindrome) // 2:
            if ord(stri[i]) > 97:
                stri[i] = "a"
                return "".join(stri)
            i += 1
        stri[-1] = "b"
        return "".join(stri)