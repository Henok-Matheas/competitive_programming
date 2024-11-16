class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        have a for while the for is for the right and the left is for removing while the num of unique is k
        
        we will have a while loop we will use to expand until it becomes invalid
        while doing that we will store where the first valid is stored, and expand until the end
        then total += end - first valid + 1
        
        when we then move on to the next then we make the first_valid to be the next index in the array for the same nums
        id
        
        so basically we will have a dict of queues for the nums to store next_valid indexes
        when popping we will move the next_valid to the popped index
        when we have noting to pop then that's when we expand until we can't expand no more
        but when we are expanding then it's also where we will store the next_valid
        
        
        next_valid = -1
        valids = {} ## dict of queues
        
        right = 0
        for left:
            while right is bound and (len(valid) < k or len(valid) == k and right char in valid):
            if next_valid == -1 and len(valids) == k:
            next_valid = right
            add into valids
            
            if len(valids) == k:
                total += right - next_valid + 1
                
            valids[left_char].popleft()
            
            if not valids[left char]:
            valids.pop(left char)
            next_valid = -1
            else:
            next_valid = max(next_valid, valids[left_char][0])
            
            total = 3 + 2 + 1
            {
            2: [3]
            3: [4]
            }
            valid_idx = 4
            right = 5
        """
        total = 0
        valid_idx = -1
        indices = {}
        right = 0
        for idx, num in enumerate(nums):
            while right < len(nums) and (len(indices) < k or (len(indices) == k and nums[right] in indices)):
                if nums[right] not in indices:
                    indices[nums[right]] = deque([])
                indices[nums[right]].append(right)
                
                if valid_idx == -1 and len(indices) == k:
                    valid_idx = right
                
                right += 1
                    
            if len(indices) == k:
                total += right - valid_idx
            
            indices[num].popleft()
            if not indices[num]:
                indices.pop(num)
                
            if len(indices) == k:
                valid_idx = max(valid_idx, indices[num][0])
            else:
                valid_idx = -1
                
        return total
                    
                    
            
        