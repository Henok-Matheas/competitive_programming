class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        vocabulary = {'END': False}

        if not needle:
            return 0
        current = vocabulary
        for letter in needle:
            current[letter] = {'END': False}
            current = current[letter]
        current['END'] = True

        def search(index):
            # print("search called for",index)
            current = vocabulary
            while index < len(haystack) and haystack[index] in current:
                # print("current is",current)
                current = current[haystack[index]]
                index += 1
            return current['END']

        # print("haystack is",haystack)
        # print("needle",needle)
        for index in range(len(haystack)):
            if search(index):
                return index

        return -1
