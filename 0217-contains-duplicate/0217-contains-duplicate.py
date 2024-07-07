class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        sort or map
        """
        
        counter = Counter(nums)
        
        for num in counter:
            if counter[num] > 1:
                return True
            
        return False