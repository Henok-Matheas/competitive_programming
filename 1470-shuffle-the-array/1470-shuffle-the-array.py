class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        given nums 2n elems
        return in x1,y1
        """
        final = []
        
        for idx in range(n):
            final.append(nums[idx])
            final.append(nums[n + idx])
        
        return final