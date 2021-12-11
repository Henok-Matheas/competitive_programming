def sortColors(nums):
    ## this uses a better counting algorithm
    colors = [0]*3

    for num in nums:
        colors[num]+=1
            
    indice = 0
    for color in range(len(colors)):
        for value in range(colors[color]):
            nums[indice] = color
            indice += 1
                
    return nums

    ## Below we will be using the method using the counting sort algorithm
    # colors = [0]*3
    # final = []

    # for num in nums:
    #     colors[num]+=1

    # for color in range(len(colors)):
    #     for value in range(colors[color]):
    #         final.append(color)
    # print(final)


    # def isSmaller(a,b):
    #     if a < b:
    #         return -1
    #     if a == b:
    #         return 0

    #     return 1

    ## The method below uses the insertion sort algorithm to find the solution
    # for i in range(len(nums)):
    #     low_index = i
    #     for j in range(i,len(nums)):
    #         if isSmaller(nums[j], nums[low_index]) == -1:
    #             low_index = j
    #     nums[i] , nums[low_index] = nums[low_index] , nums[i]
    # return nums

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

print(sortColors(nums))