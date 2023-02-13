class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        rem = 0
        ans = []
        to_append = {0: "0", 1 : "1", 2: "0", 3: "1"}
        
        for idx in range(max(len(a), len(b))):
            rem += int(a[idx]) if idx < len(a) else 0
            rem += int(b[idx]) if idx < len(b) else 0
            ans.append(to_append[rem])
            
            if rem < 2:
                rem = 0
            rem = min(rem, 1)
        
        ans += ["1"] * rem
        
        return "".join(ans[::-1])