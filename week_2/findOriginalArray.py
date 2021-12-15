

def findOriginalArray(changed):
    # if (len(changed)<2 and len(changed)%2 != 0): return []
    # if not any(map(bool,changed)): return []

    changed.sort(key = lambda x: x)

    final = []
    for i in range(len(changed)-1):
        for j in range(i+1,len(changed)):
            if changed[i] != 0 and changed[j] != 0 and changed[i]*2 == changed[j]:
                changed[j] = 0
                final.append(changed[i])
                print(final,changed)
    return  final if len(final)*2 == len(changed) else []


# changed = [1,3,4,2,6,8]
# # Output: [1,3,4]

changed = [6,3,0,1]
# Output: []


# print(type(changed))
print(findOriginalArray(changed))