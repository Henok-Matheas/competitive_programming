    
    
def longestSubarray( nums, limit):   
    max_len = 0
    for i in range(len(nums)):
        temp_len = 0
        for j in range(i,len(nums)):
            if abs(nums[i] - nums[j]) <= limit:
                print(nums[i],nums[j])
                temp_len += 1
            else:
                break
        if temp_len > max_len:
            max_len = temp_len
    return max_len


# nums = [8,2,4,7]
# limit = 4
# # Output: 2

# nums = [10,1,2,4,7,2]
# limit = 5
# # Output: 4 


nums = [1,5,6,7,8,10,6,5,6]
limit = 4
# output = 5

print(longestSubarray(nums,limit))