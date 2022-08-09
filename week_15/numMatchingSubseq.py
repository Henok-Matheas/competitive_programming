class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        letter_dict = defaultdict(list)
        
        for index,word in enumerate(words):
            # index of word, index of letter
            letter_dict[word[0]].append([index,0])
        count = 0   
        for letter in s:
            if letter not in s:
                continue
            letter_list = [] 
            while letter_dict[letter]:
                w_index, l_index = letter_dict[letter].pop()
                
                l_index += 1
                if l_index >= len(words[w_index]):
                    count += 1
                    continue
                letter_list.append([w_index, l_index])
                c_letter = words[w_index]
            
            while letter_list:
                w_index, l_index = letter_list.pop()
                c_letter = words[w_index][l_index]
                letter_dict[c_letter].append([w_index, l_index])
        return count