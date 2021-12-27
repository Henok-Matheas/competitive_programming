class Solution:
        
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        
        counted = [0]*27

        for i in tasks:
            counted[ord(i) - 65] += 1
        
        counted.sort(reverse = True)
        
        f_index = 0
        for j in range(len(counted)):
            if counted[j] == 0:
                f_index = j
                break
        final = []
        
        final = counted[:f_index]
        
        
        count = (final[0] - 1) * (n + 1)
        
        for cnt in final:
            if cnt == final[0]:
                count += 1
            else:
                break
                
        return max(count,len(tasks))
        
        
        
        
        
#         if n == 0 or len(tasks) <= 1:
#             return len(tasks)
        
        
        
#         cnt = 0 
        
#         counted = [0] * len(tasks)
        
#         for i in tasks:
#             counted[ord(i) - 65] += 1
            
#         counted.sort()
        
#         index = 0
#         for j in counted:
#             if counted[index] == 0:
#                 index += 1
#             else: break
                
#         final = counted[index:]
#         final.sort(reverse = True)
        
#         minus = 0
        
#         if len(final) <= n:
#             while len(final) > 0:
                
#                 final[-1] -= minus
#                 print("final is", final)
#                 if final[-1] == 0:
#                     final.pop()
#                 else:
#                     cnt += (n - len(final) + 1) * (final[-1] - 1) 
#                     minus += final.pop()
            
        
#         else:
#             stack = []
#             for i in range(len(final)):
#                 if len(stack) - 1 < n:
#                     stack.append(final[i])
#                 if len(stack) - 1 == n:
#                     minu = stack[-1]
#                     j = len(stack) - 1
#                     while j >= 0:
#                         stack[j] -= minu
#                         if stack[j] == 0:
#                             stack.pop()
#                         j -= 1
#             while len(stack) > 0:
#                 print("got in")
#                 z = 0
#                 stack[-1] -= minus
#                 if stack[-1] == 1:
#                     z = 1
#                 cnt += (n - len(stack) + 1) * (stack[-1] - 1 + z)
#                 minus += stack.pop()
#         return (cnt + len(tasks))
    
                
            
            
            
        
        
                        
            