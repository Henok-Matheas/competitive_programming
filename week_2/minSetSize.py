class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        output = 0
        k = len(arr) // 2
        counted = [0]* 100002
        
        for i in arr:
            counted[i] += 1
        
        counted.sort(reverse = True)
        
        for i in counted:
            if k > 0:
                k -= i
                output += 1
            else:
                return output
            