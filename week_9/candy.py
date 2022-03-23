class Solution:

    def candy(self, ratings: List[int]) -> int:

        newRatings = [float("inf")]

        needed = []
        for rating in ratings:
            newRatings.append(rating + 1)
            needed.append(1)
        newRatings.append(float("inf"))

        bound = lambda row: row >= 0 and row < len(ratings)
        idx = 1
        while idx <= len(ratings):
            if newRatings[idx] > newRatings[idx - 1]:
                needed[idx - 1] += needed[idx - 2] if bound(idx - 2) else 1
            idx += 1

        indx = len(ratings)
        while indx > 0:
            if newRatings[indx] > newRatings[indx + 1]:
                # if needed[indx - 1] < 2 and bound(indx):
                needed[indx - 1] = max(needed[indx - 1], needed[indx] + 1)
                # print(indx, ratings[indx - 1], needed[indx - 1])
                # needed[indx - 1] += needed[indx] if bound(indx) and needed[indx - 1] < 2 else 1
            indx -= 1

        answer = 0

        for candy in needed:
            answer += candy

        return answer