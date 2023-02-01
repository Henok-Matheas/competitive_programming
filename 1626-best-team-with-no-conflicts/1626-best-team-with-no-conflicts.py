class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        conflict is when
        
        young player          old player
        score          >      score
        """
        indices = [idx for idx in range(len(ages))]
        indices.sort(key = lambda idx: (ages[idx], scores[idx]))
        total_scores = [scores[idx] for idx in indices]
        
        for start_idx, start in enumerate(indices):
            for end_idx in range(start_idx + 1, len(indices)):
                end = indices[end_idx]
                ## granted that either if curr_score <= end_score
                if scores[start] <= scores[end]:
                    total_scores[end_idx] = max(total_scores[end_idx], total_scores[start_idx] + scores[end])
        
        return max(total_scores)