class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        number of subs
        
        a sub is a sub with min = minK, and max = maxK
        
        if I am valid
        
        what if I break the array down into places whose values are in the range min_, max_
        
        valid = [_, _, _, _]
        
        have a function that handles the valid ones.
        
        valid_handler
        
        when ever a mf is satisfied in that we have min_, and max_
        we also need to keep track of min_s and max_s
        we will have += (last - END)
        we then move the left and do the same
        
        
        for right in range():
            if right == min
                append to min list
            append to max list
            
            while both min and max
                we add the (END - MAX)
        """
        
        def counter(start, end):
            count = 0
            left = start
            mins, maxs = 0, 0
            for right in range(start, end):
                if nums[right] == minK:
                    mins += 1
                    
                if nums[right] == maxK:
                    maxs += 1
                    
                while mins and maxs:
                    count += (end - right)
                    
                    if nums[left] == minK:
                        mins -= 1
                    
                    if nums[left] == maxK:
                        maxs -= 1
                        
                    left += 1
                    
            return count
        
        
        left = 0
        count = 0
        
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                count += counter(left, right)
                left = right + 1
                
        return count + counter(left, len(nums))
                    