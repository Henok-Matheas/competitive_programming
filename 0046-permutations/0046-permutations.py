class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        visited = set()
        
        
        def backtrack(permtuation, visited):
            if len(permtuation) == len(nums):
                answer.append(permtuation[::])
                
                
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    permtuation.append(num)
                    backtrack(permtuation, visited)
                    permtuation.pop()
                    visited.remove(num)
                  
        permtuation = []
        backtrack(permtuation, visited) 
                    
        return answer
            