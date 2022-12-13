class Solution:
    def binary(self, profit, endTime, stack, target):
        best = 0
        left, right = 0, len(stack) - 1
        while left <= right:
            mid = (left + right) // 2
            
            index = stack[mid]
            
            if endTime[index] > target:
                right = mid - 1
            else:
                best = profit[index]
                left = mid + 1
                
        return best
    
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        indices = [idx for idx in range(len(startTime))]
        ## stack holds indexes
        stack = []
        
        indices.sort(key = lambda idx: (endTime[idx], startTime[idx]))
        
        for index in indices:
            prev_profit = self.binary(profit, endTime, stack, startTime[index])
            
            profit[index] += prev_profit
            
            if not stack or profit[stack[-1]] < profit[index]:
                stack.append(index)
        
        return max(profit)
        