

def targetIndices(nums, n):
    new = [0]*100
    final = []
    indices = []
    
    for i in nums:
        new[i] += 1

    indice = 0
    for i in range(len(new)):
        for z in range(new[i]):
            final.append(i)
            if n == i:
                indices.append(indice)
            indice+=1
    return indices

# nums = [1,2,5,2,3]
# target = 4
# # output = []

# nums = [1,2,5,2,3]
# target = 5
# # output = [4]

# nums = [1,2,5,2,3]
# target = 3
# # Output: [3]

nums = [1,2,5,2,3]
target = 2
# Output: [1,2]

print(targetIndices(nums,target))
