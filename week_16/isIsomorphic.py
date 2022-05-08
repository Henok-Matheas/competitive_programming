class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        visited = {}
        mapped = {}
        for index in range(len(s)):
            letterS = visited[s[index]] if s[index] in visited else s[index]
            letterT = mapped[t[index]] if t[index] in mapped else t[index]
            if letterS != t[index] or letterT != s[index]:
                if s[index] in visited or t[index] in mapped:
                    return False
                visited[s[index]] = t[index]
                mapped[t[index]] = s[index]
            else:
                visited[letterS] = letterT
                mapped[letterT] = letterS
        return True