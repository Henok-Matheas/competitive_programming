


def largestNumber4(nums):
    if not any(map(bool,nums)):
        return "0"
    nums  = list(map(str,nums))

    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if (int(nums[j]+nums[j+1]) < int(nums[j+1] + nums[j])):
                nums[j+1], nums[j] = nums[j], nums[j+1]

    return "".join(nums)



# nums = [10,2]
# # Output:"210"


# nums = [3,30,34,5,9]
# # Output:"9533034"

nums = [111311, 1113]
# output = "1113111311"

print(largestNumber4(nums))
