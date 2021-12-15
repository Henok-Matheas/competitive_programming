

def kthLargestNumber(nums, k):
    nums = list(map(int,nums))

    for i in range(len(nums)):
        low_index = i
        for j in range(i,len(nums)):
            if nums[j] < nums[low_index]:
                low_index = j
        nums[i], nums[low_index] = nums[low_index], nums[i]
    
    return str(nums[len(nums[k])])