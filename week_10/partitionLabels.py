class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        letters = defaultdict(int)

        for idx in range(len(s)):
            letters[s[idx]] = idx

        begin = 0
        end = letters[s[0]]
        idx = 0
        answer = []

        while idx < len(s):

            if idx == end:
                answer.append(idx - begin + 1)

            elif idx <= end:
                end = max(letters[s[idx]], letters[s[end]])

            else:
                begin = idx
                end = letters[s[idx]]
                idx -= 1
            idx += 1

        return answer