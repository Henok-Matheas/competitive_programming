class Solution:
    def findOriginalArray(changed):
        counted= [0] * 100000
        
        for i in changed:
            counted[i] += 1
            
        final = []
        if counted[0] % 2  != 0:
            return []
        for i in changed:
            if counted[i] > 0 and counted[i * 2] > 0:
                counted[i] -= 1
                # print(i,counted[i])
                counted[i * 2] -= 1
                final.append(i)
        # print(final)
        
        return final if len(final) * 2 == len(changed) else []
    print(findOriginalArray([6,3,0,1]))
    