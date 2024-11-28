class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        we have two rules
        firt rule of alternative
        arr[k - 1] > arr[k] when k is even
        arr[k - 1] < arr[k] when k is odd
        
        arr[k - 1] < arr[k] when k is even
        arr[k - 1] > arr[k] when k is odd
        
        so we will have two counters for the two rules and take the maximum of the two counters
        
        code
        f_count, s_count = 0, 0
        for num
        -> first rule
        if even and prev > curr:
        s_count = 0
        f_count += 1
        if even and prev < curr
        f_count = 0
        s_count += 1
        if even:
        f_count, s_count = 0, 0
        
        
        
        if odd and 
        """
        f_count, s_count = 1, 1
        maxim = 1
        
        for idx in range(1, len(arr)):
            curr, prev = arr[idx], arr[idx - 1]
            
            if idx % 2 == 0 and prev > curr:
                f_count += 1
                s_count = 1
            if idx % 2 == 0 and prev < curr:
                s_count += 1
                f_count = 1
            if idx % 2 == 0 and prev == curr:
                s_count, f_count = 1, 1
                
            if idx % 2 and prev < curr:
                f_count += 1
                s_count = 1
            if idx % 2 and prev > curr:
                s_count += 1
                f_count = 1
            if idx % 2 and prev == curr:
                f_count, s_count = 1, 1
                
            maxim = max(maxim, f_count, s_count)
        
        return maxim