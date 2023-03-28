class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        """
        create a decreasing
        """
        
        nums = [nums1[idx] - nums2[idx] for idx in range(len(nums1))]
        
        def merge(left, right):
            nums = []
            idx = 0
            for num in left:
                while idx < len(right) and right[idx] > num:
                    nums.append(right[idx])
                    idx += 1
                nums.append(num)
            
            return nums + right[idx:]
        
        def count(left, right, diff):
            total = 0
            idx = 0
            for num in left:
                while idx < len(right) and right[idx] >= num - diff:
                    idx += 1
                    
                total += idx
                
            return total
        
        
        def mergeSort(nums, diff):
            if len(nums) == 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, lcount = mergeSort(nums[:mid], diff)
            right, rcount = mergeSort(nums[mid:], diff)
            
            return merge(left, right), count(left, right, diff) + lcount + rcount
        
        nms, cnt = mergeSort(nums, diff)
        return cnt
            