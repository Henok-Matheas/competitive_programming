class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        final = 1
        
        dec_que = deque([])
        inc_que = deque([])
        start = 0
        for index in range(len(nums)):
                
            while inc_que and abs(nums[index] - nums[inc_que[0]]) > limit:
                # print("fail values in inc",nums[index],nums[inc_que[0]])
                val = inc_que.popleft()
                start = max(start, val + 1)
                
                if dec_que and dec_que[-1] == val:
                    dec_que.pop()
                # count -= 1
                
            while dec_que and abs(nums[index] - nums[dec_que[0]]) > limit:
                val = dec_que.popleft()
                start = max(val + 1, start)
                # print("fail values in dec",nums[index],nums[dec_que[0]])
                if inc_que and inc_que[-1] == val:
                    inc_que.pop()
                # count -= 1
                # print("count",count)
                
            while inc_que and nums[inc_que[-1]] > nums[index]:
                inc_que.pop()

            while dec_que and nums[dec_que[-1]] < nums[index]:
                dec_que.pop()
                
            dec_que.append(index)
            inc_que.append(index)
            
#             print("dec_que",dec_que)
#             print("inc_que",inc_que)
            
            final = max(final, (index - start + 1))
            
        return final

    
