class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        stack = []
        output = []
        
        for i in nums2:
            if len(stack) == 0 or stack[-1] > i:
                stack.append(i)
                # print(f"appended {i}")
            else:
                while len(stack) > 0 and stack[-1] < i:
                    dict[stack[-1]] = i
                    # print(f"dict is {dict}")
                    # print(f"popped {i}")
                    stack.pop()
                    
                stack.append(i)
        
        
        for i in stack:
            dict[i] = -1
        # print(dict)
                    
        
        for z in nums1:
            output.append(dict[z])
            
        return output   