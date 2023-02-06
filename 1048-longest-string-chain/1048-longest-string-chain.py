class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        words
        
        wordA pred of wordB iff we can insert one char in wordA to make it equal to wordB
        
        wordChain is seq of words where word1 is pred of word2 and word2 is pred of word3 and so on forth
        
        
        the question becomes a dp question
        
        we go from the shortest to the longest
        
        and try to find
        """
        def is_pred(start, end):
            start_word = words[start]
            word = words[end]
            left = 0
            count = 0
            
            for right in range(len(word)):
                if left < len(start_word) and start_word[left] == word[right]:
                    left += 1
                else:
                    count += 1
                
            return count == 1
        
        dp = [1] * len(words)
        
        words.sort(key = lambda word: len(word))
        
        
        for start, word in enumerate(words):
            for end in range(start + 1, len(words)):
                if len(words[end]) == len(words[start]):
                    continue
                if len(words[end]) > len(words[start]) + 1:
                    break
                if is_pred(start, end):
                    dp[end] = max(dp[end], 1 + dp[start])
                    
                    
        return max(dp)