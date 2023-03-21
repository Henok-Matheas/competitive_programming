class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        
        we want to expand as much as possible
        to do that we can do a for while loop.
        
        for every char
            if char is 0 count += 1
            else:
                do the math thing add to thing
                count = 0
        """
        total = 0
        count = 0
        filler = 9
        nums.append(filler)
        for num in nums:
            if num:
                total += (count + 1) * count // 2
                count = 0
            else:
                count += 1
                
        return total
                
        