class Solution:


maxScore(self, cardPoints: List[int], k: int) -> int:

curr = 0

maxim = 0

        for i in range(k):
            curr += cardPo ints[maxim = max(maxim, curr)

        # print(curr)
        begin = k - 1
        end = len(cardPoints) - 1
        while begin > -1:
            curr = curr - cardPoints[begin] + cardPoints[end]

            maxim = max(maxim, curr)
            end -= 1
            begin -= 1

        return maxim
