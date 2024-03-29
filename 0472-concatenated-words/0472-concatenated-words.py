class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {'END':False}
        
        def add(word):
            current = trie
            for letter in word:
                if letter not in current:
                    current[letter] = {'END':False}
                current = current[letter]
            current['END'] = True
            
        def concat_count(index,word):
            current= trie
            count = 0
            for idx in range(index,len(word)):
                char = word[idx]
                if char == "" or char not in current:
                    return 0 if count == 0 else count + 1
                current = current[char]
                
                if current['END']:
                    if idx == len(word) - 1:
                        return count + 1
                    count += concat_count(idx + 1,word)
            return 0 if count == 0 else count + 1
        
        
        for word in words:
            add(word)
        
        duplicates = []
        for word in words:
            count = concat_count(0,word)
            if count > 1:
                duplicates.append(word)
        return duplicates