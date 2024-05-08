class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal"
        }
        answer = [0] * len(score)
        score_idx = [(singular_score, idx) for idx, singular_score in enumerate(score)]
        score_idx.sort(reverse = True)
        
        for rank,(_, idx) in enumerate(score_idx):
            if rank + 1 in ranks:
                answer[idx] = ranks[rank + 1]
            else:
                answer[idx] = str(rank + 1)
        
        return answer