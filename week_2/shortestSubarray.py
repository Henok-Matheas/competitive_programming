from typing import Deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        count = -1

        prefix_sum = [0]
        mono_stack = [0]

        p_sum = 0
        for index in range(len(nums)):
            if nums[index] >= k:
                return 1
            p_sum += nums[index]
            prefix_sum.append(p_sum)

        deq = Deque()
        temp_val = None

        print("the prefix sum is ", prefix_sum)
        for index in range(len(prefix_sum)):
            # print("this is the current value of the prefix_sum",prefix_sum[index])
            if len(deq) == 0:
                deq.append(index)
            while len(deq) and prefix_sum[index] - prefix_sum[deq[0]] >= k:
                val = deq.popleft()
                # print(val)
                # print(prefix_sum[val],prefix_sum[index])
                if temp_val == None:
                    temp_val = index - val
                else:
                    temp_val = min(temp_val, index - val)
            while len(deq) and prefix_sum[index] <= prefix_sum[deq[-1]]:
                # print(deq,'this is deq')
                deq.pop()
            deq.append(index)
        print("this is the appended deq", deq)

        # i = 0
        # temp_val = None
        # for index in range(len(prefix_sum)):
        #     while prefix_sum[index] - prefix_sum[mono_stack[i]] >= k and i < len(mono_stack):
        #         if temp_val == None:
        #             temp_val = index - i
        #         else:
        #             temp_val = min(temp_val, index - i)
        #         i += 1
        #     while len(mono_stack) > 0 and prefix_sum[index] <= prefix_sum[mono_stack[-1]]:
        #         mono_stack.pop()
        #         i -= 1
        #     mono_stack.append(index)
        #     i += 1

        return temp_val if temp_val != None else -1
