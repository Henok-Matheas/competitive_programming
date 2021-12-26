
def shortestSubarray(nums, k):
    nums.sort()
        
    leng = -1
        
    if len(nums) < 2:
        if nums[-1] >= k:
            return 1
        else:
            return -1
        
    for i in range(1, len(nums)):
        nums[i] +=nums[i - 1]
        if nums[i] >= k:
            return i + 1


# nums = [1]
# k = 1
# # Output: 1

nums = [2,-1,2]
k = 3
# Output: 3

print(shortestSubarray(nums,k))