class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        
        """
        anagram_dict = defaultdict(list)
        
        for word in strs:
            anagram = ["0"] * 26
            for char in word:
                anagram[ord(char) - ord("a")] = str(int(anagram[ord(char) - ord("a")]) + 1)
                
            anagram_dict[tuple(anagram)].append(word)
            
        return anagram_dict.values()