

def kthLargestNumber(nums, k):
    nums = list(map(int,nums))

    for i in range(len(nums)):
        low_index = i
        for j in range(i,len(nums)):
            if nums[j] < nums[low_index]:
                low_index = j
        nums[i], nums[low_index] = nums[low_index], nums[i]
    
    return str(nums[len(nums)-k])


# nums = ["2","21","12","1"]
# k = 3
# # Output: "2"

nums = ["3","6","7","10"]
k = 4
# Output: "3"

print(kthLargestNumber(nums,k))
print(type(kthLargestNumber(nums,k)))