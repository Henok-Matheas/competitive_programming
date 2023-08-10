class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        so we find the pivot index, and after that
        we call the function twice and return an or
        
        now how to find the pivot index
        
        try to find the lowest idx
        
        if the current idx is higher then go right
        if the current idx is lower then it's a potential and go left
        """
        pivot = 0
        
        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                pivot = idx
                
        print(pivot)
        def binary(left, right, target):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1
                    
                else:
                    return True
            
            return False
        
        
        return binary(0, pivot - 1, target) or binary(pivot, len(nums) - 1, target)