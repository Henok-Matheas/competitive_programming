class Solution:

    def decodeString(self, s: str) -> str:
        opening = []
        integer = 0
        last_starting = 0
        new_num = False
        for index, letter in enumerate(s):
            try:
                int(letter)
                last_starting = index if new_num else last_starting
                integer = integer * 10 + int(letter) if not new_num else int(
                    letter)
                new_num = False
            except:
                new_num = True
                if letter == "[":
                    opening.append(index)
                elif letter == "]":
                    ope = opening.pop()
                    return self.decodeString(
                        s[:last_starting] + s[ope + 1:index] * integer +
                        (s[index + 1:] if index + 1 < len(s) else ""))

        return s
