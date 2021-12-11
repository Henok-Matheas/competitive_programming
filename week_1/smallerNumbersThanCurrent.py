'took 7 minutes and 1 try'

def smallerNumbersThanCurrent(nums):
    #this is the bruteforced version
    smallerNumbersList= [0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                smallerNumbersList[i] +=1
    return smallerNumbersList


nums = [8,1,2,2,3]

print(smallerNumbersThanCurrent(nums))