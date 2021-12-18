def kthLargestNumber(nums, k):
        nums.sort(key = lambda x: int(x))
        return str(nums[len(nums)-k])