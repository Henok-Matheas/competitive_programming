class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0

        for index in range(len(heights)):
            idx = index
            while mono_stack and heights[index] <= mono_stack[-1][0]:
                popped = mono_stack.pop()
                idx = popped[1]
                max_area = max(max_area, popped[0] * ( index - idx))
            mono_stack.append([heights[index],idx])

        for tup in mono_stack:
            max_area = max( max_area, tup[0] * (len(heights) - tup[1]))

        return max_area