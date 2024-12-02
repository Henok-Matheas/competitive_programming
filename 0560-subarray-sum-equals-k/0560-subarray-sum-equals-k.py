class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_sum = 0
        self.t_dict = defaultdict(int)
        self.t_dict[0] += 1
        total = 0
        
        for num in nums:
            p_sum += num
            total +=self.t_dict[p_sum - k]
            self.t_dict[p_sum] += 1
        
        return total