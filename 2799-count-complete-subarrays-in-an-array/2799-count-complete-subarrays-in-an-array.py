class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = Counter(nums)
        k = len(count)
        
        valid_idx = -1
        valids = {}
        right = 0
        total = 0
        
        for idx, num in enumerate(nums):
            while right < len(nums) and (len(valids) < k or (len(valids) == k and nums[right] in valids)):
                if nums[right] not in valids:
                    valids[nums[right]] = deque([])
                valids[nums[right]].append(right)
                
                if len(valids) == k and valid_idx == -1:
                    valid_idx = right
                
                right += 1
                
            
            if len(valids) == k:
                total += right - valid_idx
                
            valids[num].popleft()
            
            if not valids[num]:
                valids.pop(num)
                
            if len(valids) == k:
                valid_idx = max(valid_idx, valids[num][0])
            else:
                valid_idx = -1
                
        return total