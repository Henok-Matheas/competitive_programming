class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = m - 1, n - 1
        
        for index in reversed(range(len(nums1))):
            if pointer2 > -1 and (pointer1 < 0 or nums2[pointer2] >= nums1[pointer1]):
                ## swap
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            else:
                ## swap
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
        