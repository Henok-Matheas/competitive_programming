class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = [[0,0]]*100000
        for i in nums:
            counted[i] = [i, counted[i][1] + 1]
        
        
        counted.sort(key = lambda x : x[1], reverse = True)
        
        
        final = []
        for i in range(k):
            final.append(counted[i][0])
        return final