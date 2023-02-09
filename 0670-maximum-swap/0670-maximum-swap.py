class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        have a list of characters
        
        find two indexes swap them and check them against the maximum
        
        n ** 2 approach
        """
        
        num_list = list(str(num))
        maxim = num_list[::]
        
        
        for start in range(len(num_list)):
            for end in range(start + 1, len(num_list)):
                num_list[start], num_list[end] = num_list[end], num_list[start]
                
                if num_list > maxim:
                    maxim = num_list[::]
                
                num_list[start], num_list[end] = num_list[end], num_list[start]
                
        return int("".join(maxim))