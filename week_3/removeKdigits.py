def removeKdigits(num,k):
    # if len(num) == k:
    #         return "0"
    # digits = []
    # for index in range(len(num) - 2):
    #     digits.append([index,index + k])

    # print(digits)

    # digits.sort()


            
    # # digits.sort(key = lambda x : int(num[:x[0]] + num[x[1:]]))
        
    # return digits[0]




        if len(num) == k:
            return "0"
        str = []
        digits = []
        for index in range(len(num) - 2):
            digits.append( num[:index] + num[index + k:])
            
        digits.sort(key = lambda x : int(x))
        
        return digits[0]


# num = "1432219"
# k = 3
# # Output: "1219"

num = "1" + "0" * 99999
k = 2
# Output: "0"


print(len(num))
print(removeKdigits(num,k))