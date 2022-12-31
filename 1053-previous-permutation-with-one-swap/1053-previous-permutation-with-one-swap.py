class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        stack = []
        
        for idx in reversed(range(len(arr))):
            curr = arr[idx]
            last = None
            while stack and arr[stack[-1]] < curr:
                last = stack.pop()
            
            if last is not None:
                arr[idx], arr[last] = arr[last], arr[idx]
                return arr
            
            if stack and arr[stack[-1]] == curr:
                stack[-1] = idx
            else:
                stack.append(idx)
        return arr