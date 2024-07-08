class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        frequent = []
        
        for num, count in counter.items():
            buckets[count].append(num)
            
            
        while k and buckets:
            vals = buckets.pop()
            while k and vals:
                val = vals.pop()
                frequent.append(val)
                k -= 1
            
        return frequent