class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        maxim = 1
        i, j = 0, 0
        
        n = len(nums) -1

        while j<n:
            diff = nums[i] - nums[j + 1]

            if diff <= k:
                k -= diff
                j +=1 
                maxim = max(maxim, (j - i + 1))
            else:
                k += (nums[i] - nums[i + 1]) * (j - i)
                i += 1
        return maxim