class Solution:
    def trap(self, height: List[int]) -> int:
        removed_sum = [0] * len(height)
        stack = []
        i = 0
        total = 0
        while i < len(height):
            while i < len(height) and (not stack or height[stack[-1]] > height[i]):
                stack.append(i)
                i += 1
            if i >= len(height):
                break
            last = i - 1
            working_sum = 0
            while stack and height[stack[-1]] <= height[i]:
                popped = stack.pop()
                working_sum += height[popped] + removed_sum[popped]
                last = popped
            removed_sum[i] = working_sum if stack else working_sum - height[last] if working_sum else working_sum
            last = stack[-1] if stack else last
            total += ((min(height[i],height[last]) * (i - last - 1)) - removed_sum[i]) if not stack else 0
            removed_sum[i] = removed_sum[i] if stack else 0
        
        current = stack.pop()
        while stack:
            before = stack.pop()
            total += ((min(height[current],height[before]) * (current - before - 1)) - (removed_sum[current] if (current - before - 1) else 0))
            current = before
            
        return total
            