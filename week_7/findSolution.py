"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:

    def findSolution(self, customfunction: 'CustomFunction',
                     z: int) -> List[List[int]]:

        answer = []

        for x in range(1, 1001):
            left = 1
            right = 1000 if not answer else answer[0][1]

            while left <= right:
                y = (left + right) // 2
                if customfunction.f(x, y) < z:
                    left = y + 1
                elif customfunction.f(x, y) > z:
                    right = y - 1
                else:
                    answer.append([x, y])
                    break
            if customfunction.f(x, 1) > z:
                break

        return answer
