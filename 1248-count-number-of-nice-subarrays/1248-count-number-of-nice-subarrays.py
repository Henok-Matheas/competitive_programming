class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        
        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        k = 2
        
        odds = [3, 6]
               [l, r]  right = 10 - 6 = 4
        left = 3 - - 1 = 4
        
        left * right = 16
        
        [1, 1, 2, 1, 2, 2, 2, 1, 2, 2]
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        odds = [0, 1, 3, 7]
                  [l,    r] right = next_odd_idx - right_idx
             left = left_idx - prev_odd_idx / -1
        
        
        [1, 2, 2, 1]
          []
          [2]
          [2, 2]
        
        
            []                             []
            [2]            [1, 2, 2, 1]    [2]
            [2, 2]                         [2, 2]
            [2, 2, 2]                      [2, 2, 2]
            4                              4
            4 * 4 = 16
            
            
            
            
            
               3 [1, 2, 2, 1] 3
                 [1, 2, 2, 1, 2]
                 [1, 2, 2, 1, 2, 2]
                 [1, 2, 2, 1, 2, 2, 2]
              [2, 1, 2, 2, 1]
              [2, 1, 2, 2, 1, 2]
              [2, 1, 2, 2, 1, 2, 2]
              [2, 1, 2, 2, 1, 2, 2, 2]
           [2, 2, 1, 2, 2, 1]
           [2, 2, 1, 2, 2, 1, 2]
           [2, 2, 1, 2, 2, 1, 2, 2]
           [2, 2, 1, 2, 2, 1, 2, 2, 2]
        [2, 2, 2, 1, 2, 2, 1]
        [2, 2, 2, 1, 2, 2, 1, 2]
        [2, 2, 2, 1, 2, 2, 1, 2, 2]
        [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        
        pseudo
        
        odds = [] -> construct this
        
        go over odds
            find right evens amount
            find left evens amount
            
            if odd_count is greater than k move left idx by one.
            
            total += right * left
           
           
        """
        odds = [-1] + [idx for idx in range(len(nums)) if nums[idx] % 2] + [len(nums)]
        total = 0
        
        for right in range(k, len(odds) - 1):
            left = right - (k - 1)
            
            left_evens = odds[left] - odds[left - 1]
            right_evens = odds[right + 1] - odds[right]
            
            total += left_evens * right_evens
            
        return total