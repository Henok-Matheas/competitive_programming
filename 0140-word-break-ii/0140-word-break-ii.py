class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        
        this is a backtracking question
        
        since it asks us to list out all the possible ways of splitting
        
        
        and it's also a trie question since it asks us to match strings
        
        
        so first we construct a trie using wordDict
        
        after that we will have a recursive function which will take a trieNode and idx 
        
        and if the char is a child of the trieNode we will go a recursive step
        
        if the current trienode has an index != -1:
            path.append(index)
            we can choose to start a new trieNode 
            path.pop()
            
            
        but since it also required us to have a separated string we need to know the actual indexes of the words.
        so we need a path variable as well.
        """
        trie = {"#" : -1}
        answer = []
        
        for idx, word in enumerate(wordDict):
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {"#": -1}
                current = current[char]
                
            current["#"] = idx
        
            
        def recur(idx, path, current):
            
            if idx == len(s):
                answer.append(" ".join(wordDict[index] for index in path))
                return
            
            if s[idx] in current:
                if idx + 1 < len(s):
                    recur(idx + 1, path, current[s[idx]])
                
                if current[s[idx]]["#"] != -1:
                    path.append(current[s[idx]]["#"])
                    recur(idx + 1, path, trie)
                    path.pop()
                    
        recur(0, [], trie)
        return answer