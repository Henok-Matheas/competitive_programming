def longestSubarray(nums, limit):
        
        max_len = 0
        
        bound = []
        
        i, j  = 0, 0
        
        while j < len(nums) and i < len(nums):
            if i == len(nums) - 1:
                return max_len
            elif len(bound) == 0:
                l_bound = nums[i] - limit
                h_bound = nums[i] + limit
                bound.append(l_bound)
                bound.append(h_bound)
                j += 1
                print(nums[i:j],"appended")
                print("bound",bound)
                max_len = max((j - i),max_len)
            elif bound[0] <= nums[j] and nums[j] <= bound[1]:
                print(bound[0],nums[i],bound[1],"l_bound  num h_bound")
                l_temp = nums[j] - limit
                h_temp = nums[j] + limit
                print(l_temp, h_temp, "these are j's low and high")
                bound[0] = max(bound[0],l_temp)
                bound[1] = min(bound[1],h_temp)
                print(bound[0],bound[1],"bound[zero] and bound[one]")
                j += 1
                print(nums[i:j],"case passed")
                print("bound",bound)
                max_len = max((j - i),max_len)
            else:
                i += 1
                j -= 1
                print(nums[i],"i moved")
        return max_len


# nums = [10,1,2,4,7,2]
# limit = 5
# # Output: 4 

# nums = [4,2,2,2,4,4,2,2]
# limit = 0
# # Output: 3


nums = [1,5,6,7,8,10,6,5,6]
limit = 4
# output = 5

print(longestSubarray(nums,limit))