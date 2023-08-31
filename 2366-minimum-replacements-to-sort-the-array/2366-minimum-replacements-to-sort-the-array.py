class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        
        4, 1, 3, 6
        
        the largest replacement number is sum(nums)
        
        
        to make it minimum
        
        3, 3, 3, 3, 3
        
        3, 8, 3
        
        1 , 8 => 2
        
        
        6, 8, 3
        
        
        [8, 6, 3]


        when we encounter a number we need to know how many numbers are greater than it on the right side.
        what about the left side would it matter?
        
        if the left side is smaller it wouldn't, well it kinda would since we need to break it in such a way that it's not smaller.
        
        so it would matter
        
        in that case we can do it in a sort of n * 2 way.
        
        
        for the problem above what if we started from the largest elements?
        
        we then check if we have smaller elements on the left?
        
        if there are we try to convert the current element to the next smaller one?
        
        slight problem, that would cause us to have to reivaluate the next smaller one, since the largets one when we convert it might be the next smallest.
        
        9 => 3, 3, 3
        
        8 => 7
        
        
        
        what if we have a store that stores the new elements in their place and we do a binary search to find where the one popped from the heap is removed
        
        
        
        so for the current answer we go from the last to the first
        
        and while doing that we divide the current element with the minimum, and that will be the amount we add to the total this is basically us converting the current num to the minimum element.
        
        the remaining then becomes the minimum element from now on if no remaining then the minimum is the previous number
        
        is there a proof to this???
        
        
        the problem that I found with this solution is that when we encounter a number that is not divisible by the previous minim, it means that the parity betwee
        
        """
        total = 0
        minim = nums[-1]
        for idx in reversed(range(len(nums))):
            minim = min(minim, nums[idx])
            total += nums[idx] // minim - 1
            if nums[idx] % minim:
                total += 1
                ceild = nums[idx] // minim + 1
                minim = nums[idx] // ceild
                
            
        return total