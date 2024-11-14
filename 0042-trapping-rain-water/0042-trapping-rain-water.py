class Solution:
    def trap(self, height: List[int]) -> int:
        """
        when I find a bigger one then I don't matter
        I should just calculate 
        
        we remove all the lowest and then append ourselves
        to do the sum in the middle we will just take the lower of the popped and ourselves * distance
        
        but has a unique problem which is if the middle ones have been calculated themselves to take care of this since the middle ones have already calculated their areas we just have to put them out of the equation to do that we just take the popped height and reduce it from either the current or previous we do this to basically make it start from the ground since the middle area is already calculated
        
        """
        total = 0
        stack = []
        for idx, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                popped = stack.pop()
                if not stack:
                    break
                prev = stack[-1]
                bounded_height = min(height[prev], h) - height[popped]
                total += bounded_height * (idx - prev - 1)
                
            stack.append(idx)
        return total