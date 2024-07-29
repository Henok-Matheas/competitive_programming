class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        we want to build an array with each value being the largest from that window
        
        
        we will have a increasing_deque = deque([])
        and a max_sums array
        
        for every idx, val
        
        while val <= nums[inc_stack[-1]]:
            pop them from the inc_stack since they are useless
            
        if inc_deque[0] <= idx - k:
            deque.popleft()
            
        if idx - k >= 0:
            max_sums.append(stack[inc_deque[0]])
        """
        
        inc_stack = deque([])
        max_sums = []
        
        for idx, val in enumerate(nums):
            while inc_stack and val >= nums[inc_stack[-1]]:
                inc_stack.pop()
                
            inc_stack.append(idx)
                
            if inc_stack and inc_stack[0] <= idx - k:
                inc_stack.popleft()
            
            if idx - k + 1 > -1:
                max_sums.append(nums[inc_stack[0]]) 
                
            
        return max_sums