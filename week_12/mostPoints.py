class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        maxim = -float("inf")
        for idx in range(len(questions) - 1, -1, -1):
            indx = questions[idx][1] + 1 + idx
            questions[idx][0] = max(
                maxim, questions[idx][0] +
                (questions[indx][0] if indx < len(questions) else 0))
            maxim = max(maxim, questions[idx][0])
        return maxim
