class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        """
        given nums and pivot, rearange nums
        
        rules:
            - nums < pivot  appear before nums > pivot
            - nums == pivot appear in between greater and lesser
            - relative order is maintained
        """
        less = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]
        
        return less + equal + greater