class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        find the differnece of words and check if it's valid
        
        for every two words find the first difference of words and if their indices
        aren't valid return invalid
        """
        indices = {char: idx for idx, char in enumerate(list(order))}
        indices["N"] = -1
        
        for idx in range(len(words) - 1):
            curr, next_ = words[idx], words[idx + 1]
            
            for index in range(max(len(curr), len(next_))):
                curr_letter = curr[index] if index < len(curr) else "N"
                next_letter = next_[index] if index < len(next_) else "N"
                
                if indices[curr_letter] > indices[next_letter]:
                    return False
                
                if curr_letter != next_letter:
                    break
        return True