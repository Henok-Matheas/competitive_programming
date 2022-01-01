class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono_stack = []
        rm_count = 0
        for current in num:
            curr_int = int(current)
            while len(mono_stack) > 0 and rm_count < k and curr_int < mono_stack[-1]:
                mono_stack.pop()
                rm_count += 1
            mono_stack.append(curr_int)
        
        while rm_count < k:
            mono_stack.pop()
            rm_count += 1
        answer = "".join(map(str, mono_stack)).lstrip("0")
        return answer if len(answer) > 0 else "0"