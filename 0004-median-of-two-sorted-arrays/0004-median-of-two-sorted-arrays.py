class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        small, large = nums1, nums2

        if len(nums2) < len(nums1):
            small, large = nums2, nums1

        left, right = 0, len(small) - 1

        while True:
            mid = (left + right) // 2
            large_mid = half - mid - 2

            small_left  = small[mid] if mid >= 0 else -float("inf")
            small_right = small[mid + 1] if mid + 1 < len(small) else float("inf")
            large_left  = large[large_mid] if large_mid >= 0 else -float("inf")
            large_right = large[large_mid + 1] if large_mid + 1 < len(large) else float("inf")

            if small_left <= large_right and large_left <= small_right:
                if total % 2:
                    return min(large_right, small_right)
                return (max(small_left, large_left) + min(small_right, large_right)) / 2

            elif small_left > large_right:
                right = mid - 1
            else:
                left = mid + 1