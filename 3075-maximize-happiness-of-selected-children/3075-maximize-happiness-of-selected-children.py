class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        n children with happiness
        
        k turns to take k children
        
        single turn
            - select a child
            - -1 to the happiness of other children
        
        - happiness of a child >= 0
        
        return maximum sum of happiness of selected children
        
        """
        happiness.sort()
        max_happiness, sad = 0, 0
        
        
        for _ in range(k):
            max_happiness += max(happiness.pop() - sad, 0)
            sad += 1
            
        return max_happiness