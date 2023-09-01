class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        """
        -3, -1, 1
        -2 - (-2)
        
        1 -3, -1
        
        1 - - 3
        
        4
        
        2
        
        final_num = num + (-d if L else d)
        total += abs(idx * final_num - (prev_sum))
        prev_sum += final_num
        -1 +3 
        
        2 0
        4
        x, y, z
        
        (x - y) + (x - z) + (x - a)
        3x + (- y - z)
        
        -9 - (y + z)
        6
        
        -1 - (1)
        
        3, -2
        
        1, -3
        
        1 * -3 - 1
        prev_sum = -2
        
        final_num = -1
        
        2 * -1 - (-2)
        -2 + 2
        0
        
        
        for every generate the final one.
        
        for every again
        
        
        """
        total = 0
        prev_sum = 0
        for idx, num in enumerate(nums):
            nums[idx] = num + (-d if s[idx] == "L" else d)
            
        nums.sort()
        for idx, num in enumerate(nums):
            total += abs(idx * num - prev_sum)
            prev_sum += num
        
        
        return total % (10 ** 9 + 7)
        