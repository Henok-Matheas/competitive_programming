class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        max number of points that can be found
        
        this question looks like a pick don't pick question.
        
        
        it's either pick this and jump two steps/ don't pick this and go to the next one.
        
        
        since we have to delete every element equal to a thing we want to have a counter dictionary, we then sort that bitch.
        """
        count_dict = Counter(nums)
        counts = [(value, count) for value, count in count_dict.items()]
        counts.sort() 
        
        @cache
        def dp(idx):
            if idx >= len(counts):
                return 0
            
            return max(counts[idx][0] * counts[idx][1] + (dp(idx + 2) if counts[idx][0] + 1 in count_dict else dp(idx + 1)), dp(idx + 1))
        
        
        return dp(0)