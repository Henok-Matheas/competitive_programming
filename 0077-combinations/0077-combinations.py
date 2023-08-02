class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        
        """
        combinations = []
        paths = set()
        combination = []
        def backtrack(num, combination, path):
            if len(combination) == k:
                combinations.append(combination[:])
                return
            
            if num > n:
                return
            
            if not 2 ** num & path and 2 ** num | path not in paths:
                    paths.add(2 ** num | path)
                    combination.append(num)
                    backtrack(num + 1, combination, 2 ** num | path)
                    combination.pop()
            
            backtrack(num + 1, combination, path)
                
        
        backtrack(1, combination, 0)
        return combinations