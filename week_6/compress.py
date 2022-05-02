class Solution:

    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        prev = 0
        size = 0
        while i < len(chars) and j < len(chars):
            while i < len(chars) and j < len(chars) and chars[i] == chars[j]:
                j += 1

            chars[prev] = chars[j - 1]
            size = str(j - i)
            if j - i > 1:
                for one in size:
                    prev += 1
                    chars[prev] = one
            prev += 1
            i = j

        return prev
