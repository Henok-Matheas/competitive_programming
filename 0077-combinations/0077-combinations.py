class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        
        """
        combinations = []
        combination = []
        def backtrack(num, combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return
            
            if num > n:
                return
            
            combination.append(num)
            backtrack(num + 1, combination)
            combination.pop()
            
            backtrack(num + 1, combination)
                
        
        backtrack(1, combination)
        return combinations