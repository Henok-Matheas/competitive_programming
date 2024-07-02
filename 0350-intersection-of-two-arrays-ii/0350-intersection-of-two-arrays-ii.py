class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
        answer = []
        
        for num in nums1_dict:
            
            for _ in range(min(nums1_dict.get(num), nums2_dict.get(num, 0))):
                answer.append(num)
                
        return answer