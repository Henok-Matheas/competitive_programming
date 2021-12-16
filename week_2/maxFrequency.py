

def maxFrequency(nums,k):
    nums.count(reverse = True)
    maxim = 1
    i, j = 0, 1

    while j<n:
        diff = nums[i] - nums[j]

        if diff <= k:
            k -= diff
            maxim = max(maxim, (j - i))
            j +=1 
        else:
            k += (nums[i] - nums[i + 1])(j - i)
            i += 1


print(maxFrequency([]))
