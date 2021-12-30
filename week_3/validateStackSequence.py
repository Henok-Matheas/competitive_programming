class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        i, j = 0, 0
        
        while j < len(popped) and i < len(pushed):
            if len(stack) != 0 and stack[-1] == popped[j] :
                stack.pop()
                j += 1
            elif pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                j += 1
                while len(stack) != 0 and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                i += 1
        
#         for i in popped:
#             if len(stack) == 0:
                
#             while (len(stack) == 0 or stack[-1] != i) and j < len(pushed) and pushed[j] != i:
#                 stack.append(pushed[j])
#                 j += 1
#             if len(stack) != 0 and stack[-1] == i:
#                 stack.pop()
            
#             if j < len(pushed): 
#                 j += 1
                
            # else:
            #     print(stack,i,pushed[j])
            #     stack.pop()
            #     j += 2
            
        print(stack)
        return len(stack) == 0
            
            
        
        
        