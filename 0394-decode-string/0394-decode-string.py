class Solution:
    def decodeString(self, s: str) -> str:
        """
        
        
        """
        
        def recur(idx):
            array = []
            number = 0
            
            while idx < len(s):
                if s[idx].isdigit():
                    number = number * 10 + int(s[idx])
                    
                elif s[idx] == "[":
                    string, idx = recur(idx + 1)
                    array.append("".join(string * number))
                    number = 0
                    
                elif s[idx] == "]":
                    return "".join(array), idx
                
                else:
                    array.append(s[idx])
                    
                idx += 1
                
            return "".join(array), idx
        
        return recur(0)[0]
                    