class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sub = defaultdict(int)
        sub[0] += 1
        count = 0
        sum_ = 0
        
        for num in nums:
            sum_ += num
            count += sub[sum_ % k]
            sub[sum_ % k] += 1
            
        return count