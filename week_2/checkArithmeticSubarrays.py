class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        m = len(l)
        for index in range(m):
            bound = nums[l[index]:r[index] + 1]
            bound.sort()
            progression = bound[1] - bound[0]
            temp_output = True
            for i in range(1,len(bound)):
                if bound[i] - bound[i - 1] != progression:
                    temp_output = False
                    break
            output.append(temp_output)
        return output
            