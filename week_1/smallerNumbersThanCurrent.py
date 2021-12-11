'took 7 minutes and 1 try'

def smallerNumbersThanCurrent(nums):
    ## this method uses the counting algorithm
    count = [0]*102
    final = []

    for num in nums:
        count[num]+=1
    
    elements_smaller_than = 0
    for index in range(len(count)):
        if count[index] != 0:
            count[index], elements_smaller_than = elements_smaller_than, elements_smaller_than+count[index]
            print(index,count[index])
    for num in nums:
        final.append(count[num])
    
    return final




    ##this is the insertion algorithm version which is very slow
    # smallerNumbersList= [0]*len(nums)
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[j] < nums[i]:
    #             smallerNumbersList[i] +=1
    # return smallerNumbersList


nums = [8,1,2,2,3]

print(smallerNumbersThanCurrent(nums))