class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def dp(idx, opened):
            if opened < 0:
                return False
            
            if idx == len(s):
                return opened == 0
            
            valid = False
            
            if s[idx] == "(" or s[idx] == "*":
                valid |= dp(idx + 1, opened + 1)
                
            if s[idx] == ")" or s[idx] == "*":
                valid |= dp(idx + 1, opened - 1)
                
            if s[idx] == "*":
                valid |= dp(idx + 1, opened)
            return valid
        
        return dp(0, 0)