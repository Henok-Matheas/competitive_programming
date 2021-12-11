def sortColors(nums):
    for i in range(len(nums)):
        low_index = i
        for j in range(i,len(nums)):
            if nums[j] < nums[low_index]:
                low_index = j
        nums[i] , nums[low_index] = nums[low_index] , nums[i]
    return nums

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

print(sortColors(nums))