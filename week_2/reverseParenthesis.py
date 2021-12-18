class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        s_list = []
        
        tag_indices = []
        
        for i in s:
            s_list.append(i)
            
        for j in range(len(s_list)):
            if s_list[j] == "(":
                tag_indices.append(j + 1)
                s_list[j] = ""
            elif s_list[j] == ")":
                open_index = tag_indices.pop()
                sliced  = s_list[open_index:j]
                s_list[open_index:j] = sliced[::-1]
                s_list[j] = ""
        
        return "".join(s_list)
        