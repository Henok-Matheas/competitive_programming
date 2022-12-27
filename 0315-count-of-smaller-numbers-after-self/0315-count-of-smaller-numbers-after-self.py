class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        indices = [idx for idx in range(len(nums))]
        indices.sort(key = lambda idx : (nums[idx], idx))
        pos = []
        
        
        for idx in indices:
            counts[idx] = len(pos) - bisect.bisect(pos, idx, 0, len(pos))
            bisect.insort(pos, idx)
        
            
        return counts
                
            
        ## count of smaller elements to the right of i
        ## smaller is a max_heap
        ## larger is a min_heap
        ## what if we have two heaps, one larger than me, and the other that has the ones smaller than me.
        ## on every index we remove the ones that are larger than me and in smaller heap
        ## and put them into the larger heap
        ## we also add the ones that are smaller than me and in the larger heap into smaller heap