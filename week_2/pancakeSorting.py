# https://leetcode.com/problems/pancake-sorting/submissions/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        k = len(arr)
        output = []
        
        while k >1:
            maxim = 0
            for i in range(k):
                if arr[i] > arr[maxim]:
                    maxim = i
            
            # print("maxim = ",maxim)
            rev_sliced = arr[maxim::-1]
            arr[:maxim + 1] = rev_sliced
            
            rev = arr[0:k]
            rev = rev[:: -1]
            arr[0: k] = rev
            
            output.append(maxim + 1) if maxim > 0 else None
            output.append(k) if k > 0 else None
            k -= 1
        return output