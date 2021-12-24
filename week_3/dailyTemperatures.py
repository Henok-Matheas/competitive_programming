class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = [0]
        # mono_stack = [[temperatures[0],0]]
        output = [0]*len(temperatures)

        j = 0

        while j < len(temperatures):
            if temperatures[j] > temperatures[mono_stack[-1]] :
                while len(mono_stack) > 0:
                    if temperatures[j] > temperatures[mono_stack[-1]] :
                        output[mono_stack[-1]] = j - mono_stack[-1]
                        mono_stack.pop()
                    else:
                        break
            mono_stack.append(j)
            j += 1
        
        
        return output