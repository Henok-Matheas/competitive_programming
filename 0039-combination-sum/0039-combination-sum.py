class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        
        """
        answer = []
        def backtrack(path, idx, target):
            if target == 0:
                answer.append(path.copy())
                return
            
            if target < 0:
                return
            
            for curr_idx in range(idx, len(candidates)):
                path.append(candidates[curr_idx])
                backtrack(path, curr_idx, target - candidates[curr_idx])
                path.pop()
                
        backtrack([], 0, target)
        return answer