class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answers = []
        final = set()
        
        for num in nums:
            children = answers[::-1]
            for answer in answers:
                if answer[-1] <= num:
                    children.append(answer + [num])
                    
            answers = children[::]       
            answers.append([num])
        
        for answer in answers:
            if len(answer) > 1:
                final.add(tuple(answer))
                
                
        return final