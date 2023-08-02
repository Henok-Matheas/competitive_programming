class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        thought
        
        pos1
        neg1
        
        pos2
        neg2
        
        pos1 -> pos2
        pos1 -> neg2
        neg1 -> pos2
        neg1 -> neg2
        
        
        then binary search from -10 ** 10 - 10 ** 10
        """
        
        left = 10 ** 10 * -1
        right = 10 ** 10
        best = 0
        
        pos1 = [num for num in nums1 if num >= 0]
        neg1 = [num for num in nums1 if num < 0]
        pos2 = [num for num in nums2 if num >= 0]
        neg2 = [num for num in nums2 if num < 0]
        
        neg12 = neg1[::-1]
        neg21 = neg2[::-1]
        
        def counter(target, array1, array2, start, end, increment):
            total = 0
            left = 0
            for idx in range(start, end, increment):
                num = array1[idx]
                
                while left < len(array2) and array2[left] * num <= target:
                    left += 1
                total += left
                
            return total
        
        while left <= right:
            mid = (left + right) // 2
            
            count = counter(mid, pos1, pos2, len(pos1) - 1, -1, -1) + counter(mid, pos1, neg2, 0, len(pos1), 1) + counter(mid, pos2, neg1, 0, len(pos2), 1) + counter(mid, neg12, neg21, len(neg12) - 1, -1, -1)

            
            if count < k:
                left = mid + 1
            else:
                best = mid
                right = mid - 1

                  
        return best