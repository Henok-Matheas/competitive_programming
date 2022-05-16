class Solution:

    def simplifyPath(self, path: str) -> str:
        final = []

        # first = 0
        index = 1

        temp = ""
        while index < len(path):

            while index < len(path) and path[index] != "/":
                temp += path[index]
                index += 1

            if temp == "..":
                if final:
                    final.pop()
                    final.pop()
            elif temp and temp != ".":
                final.append("/")
                final.append(temp)

            temp = ""
            index += 1

        return "".join(final) if final else "/"





# shorter lines
class Solution:

    def simplifyPath(self, path: str) -> str:
        final = []
        for char in path.split("/"):
            if char == "..":
                if final: final.pop()
            elif char and char != ".":
                final.append(char)
        return "/" + "/".join(final)