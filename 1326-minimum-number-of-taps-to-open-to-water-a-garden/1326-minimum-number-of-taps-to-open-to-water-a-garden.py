class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        it's a minimization problem
        it's wants to minimize open taps
        to minimize we want to take the taps that water the largest range
        how to do that??
        first idea:
        what if we sort using start and end??
        after that we have a stack and if the incoming tap handles all of the previous ones
        meaning that it could water for the range, then we use it.
        
        how can you make sure that it can water for all the range??
        
        when we insert we remove the part that intersects, and only take the part that doesnt'
        e.g
        start, range
        [0, 4], we now have [1, 5] it doesn't engulf the previous one
        so we will have [0, 4], [4, 5]
        [0, 4], [4, 5], we now have [2, 9]
        it overtakes [4, 5] so we delete it.
        [0, 4], [4, 9]
        [1, 5] we now have [2, 9]
        
        to make sure that it takes in everything
        """
        
        
        """
        if the current bound is conversely less than the previous we ignore it
        meaning if my end is less than the previous continue it.
        if my start is larger than my previous end we return -1
        """
        
        """
        step1= preprocess to make range from 0 - n
        step2 = sort
        step4 = add [0, 0], and [n, n] into the list
        current_start, current_end
        step5 = {
        if current_start > prev_end return -1
        while stack and current_start <= prev_start <= prev_end <= current_end
            pop from stack
        append to stack if prev_start <= current_start <= prev_end
        
        return len(stack) - 2
        """
        
        for idx, range_ in enumerate(ranges):
            start, end = max(idx - range_, 0), min(idx + range_, n)
            ranges[idx] = [start, end]
            
        ranges.append([n, n * 2])
        ranges.sort()
        
        stack = [[-1, 0]]
        for start, end in ranges:
            while stack and start <= stack[-1][0] and stack[-1][1] <= end:
                stack.pop()
                
            prev_start, prev_end = stack[-1]
            if start > prev_end:
                print([start, end], [prev_start, prev_end])
                return -1
            
            if end <= prev_end:
                continue
            
            stack.append([prev_end, end])
            
        return len(stack) - 2
            
        
        