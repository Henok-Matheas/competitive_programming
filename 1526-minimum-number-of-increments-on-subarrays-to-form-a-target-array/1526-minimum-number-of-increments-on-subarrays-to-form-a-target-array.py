class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        """
        we have source which is all zero:
        
        one operation
        choose subarray and increment each by one.
        
        return minimum number of operations to make source == target
        
        
        
        source = [0, 0, 0, 0, 0]
        target = [1, 2, 3, 2, 1]
        
        
        
        one thought: the minimums are really important, they kind of give us the range for increasing.
        
        
        
        3 1 1 2
        
        in a brute force way the way it would be done is
        
        find minimum and subtract
        
        what if it's a graph problem? kind of like a union find?
        
        
        so the answer is a monotonic stack
        
        the reason for it is when you find a smaller number than yourself it is clear that you and that the subarray that includes you and that smaller number can be reached at using a single operation * smaller number times.
        
        but after that your subarray that doesn't include that smaller number becomes it's own region, which means you have to look for the next greater element that is larger than the previously smaller number and have divisions of regions and so and so on forth
        
        psuedo code
        
        for num in target:
        while stack and stack[-1] >= num:
            remove from stack
            left = left of the stack
            right = num
            
            total += min(abs(left - removed), abs(right, removed))
            
        add to stack
        """
        
        target = [0] + target + [0]
        stack = []
        total = 0
        
        for num in target:
            while stack and stack[-1] >= num:
                current = stack.pop()
                left = stack[-1] if stack else 0
                right = num
                total += min(current - left, current - right)
                
            stack.append(num)
            
        return total