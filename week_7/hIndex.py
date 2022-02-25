class Solution:

    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        citations.sort()
        j = len(citations)

        for idx in range(len(citations)):

            if j - idx <= citations[idx]:
                return j - idx

        return ans
