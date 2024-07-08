class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        
        """
        anagram_dict = defaultdict(list)
        
        for word in strs:
            anagram = [char for char in word]
            anagram.sort()
            anagram_dict["".join(anagram)].append(word)
            
        return anagram_dict.values()