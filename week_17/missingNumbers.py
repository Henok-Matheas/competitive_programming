class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        zor = 0
        for elem in range(len(nums)):
            zor ^= elem + 1
        fin = 0
        for elem in nums:
            fin ^= elem
        return fin ^ zor