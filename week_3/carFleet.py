class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos2speed = {}
        for i in range(len(position)):
            pos2speed[position[i]] = speed[i]
        print("pos2speed = ",pos2speed)
            
        position.sort()
        
        mono_stack = []
        mono_stack.append(position[0])
        for z in range(len(position)):
            
            try_before = (target - mono_stack[-1])/pos2speed[mono_stack[-1]]
            try_now = (target - position[z])/pos2speed[position[z]]
            
            if try_before <= try_now:
                while len(mono_stack) > 0:
                    if (target - mono_stack[-1])/pos2speed[mono_stack[-1]] <= (target - position[z])/pos2speed[position[z]]:
                        pos2speed[position[z]] =min(pos2speed[mono_stack[-1]],pos2speed[position[z]])
                        
                        mono_stack.pop()
                    else:
                        break
                
            mono_stack.append(position[z])
            
        
        return len(mono_stack)
        
        
            
        