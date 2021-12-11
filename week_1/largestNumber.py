import functools
import operator

def largestNumber(nums):
    nums.sort(key = lambda x:(1/int(str(x)[0])))
    final = functools.reduce(operator.add, map(str, nums))
    print(final)

# nums = [10,2]
# # Output: "210"

nums = [4,3,30,34,5,9]
# Output: "95434330"

largestNumber(nums)