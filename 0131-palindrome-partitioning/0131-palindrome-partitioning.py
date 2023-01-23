class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        
        # this is a backtrack question.
        
        answers = []
        path = []
        def backtrack(start):
            if start == len(s):
                answers.append(path[::])
                
            for idx in range(start, len(s)):
                ## check if it's a palindrome
                if isPalindrome(start, idx):
                    path.append(s[start: idx + 1])
                    backtrack(idx + 1)
                    path.pop()
        backtrack(0)
        return answers
        
#         @lru_cache(None)
#         def dp(index):
#             if index == len(s):
#                 return [[]]
#             answer = []
#             for j in range(index, len(s)):
#                 if not isPalindrome(index, j):
#                     continue
#                 for lst in dp(j + 1):
#                     answer.append([s[index: j + 1]] + lst)
#             return answer
        
        
#         return dp(0)
        
        