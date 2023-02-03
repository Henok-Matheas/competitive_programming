class Solution:
    def simplifyPath(self, path: str) -> str:
        final = []
        for char in path.split("/"):
            if char == "..":
                if final:
                    final.pop()
            elif char and char != ".":
                final.append(char)
        return "/" + "/".join(final)