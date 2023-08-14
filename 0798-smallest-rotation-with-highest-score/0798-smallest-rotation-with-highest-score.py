class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        """
        rotate by k
        
        then score for one = if nums[i] <= i = 1
        
        return rotation index with highest score
        
        
        
        for every index we can know at what index it gets switched on and off
        
        so maybe we can have a off and on heap?
        
        and for every value of k we can check them
        
        what if we have [on_k, off_k]
        
        on_k is the amount of moves it takes for it to be on,
        off_k is the amount of movies it takes for an index to be off which
        
        
        so idx in range k
        
        if there are any idx values in the off heap with the off_k equal with the idx
        add the [on_k, off_k] into the on heap
        
        if there are any idx values in the on heap with the on_k equal with the idx
        add the [off_k, on_k] into the off heap
        
        
        
        two edges
        
        when it is sorted in the correct order?
        
        if current idx is greater than or equal the val
        place where it is open is
        [0, current_idx - val], [idx + 1, len(nums) - 1]
        
        else: if current idx is less than val
        len(nums) -  val = the number of instances where a value is valid
        4 is valid only one place
        [idx + 1, idx + len(nums) -  val]
    
        
        [1, 2, 0, 3, 4]
        
        
        
        [1, 3]
        
        [2, 3]
        
        [0, 1] 
        
        [3, 4]
        
        [4, 4]
        
        [0, 4] 
        
        [5, 4]
        
        
        
        [0, 1, 2, 3, 4, 5]
        [2, 1, 1, 1, 1, 1]
        [0, 0, 1, 0, 2, 4]
        [2, 1, 0, 1, -1, -3]
        
        
        0, 2
        1, 3
        2, 3
        3, 4
        4, 3
        
        
        after that it's just prefix sum
        
        [1, 3]
        [2, 3]
        [0, 1] []
        
        0 => [0, 4]
        1 =>
        
        
        for every index we can find the on parts and then it's just finding the largest
        
        """
        
        scores = [0] * (len(nums) + 1)
        
        
        for idx, val in enumerate(nums):
            scores[idx + 1] += 1
            if idx >= val:
                scores[0] += 1
                scores[idx - val + 1] -= 1
                scores[len(nums)] -= 1
            else:
                scores[idx + len(nums) - val + 1] -= 1
                
        maxim = 0
        count = 0
        index = 0
        
        
        for idx, score in enumerate(scores):
            count += score
            if maxim < count:
                index = idx
                maxim = count
                
        return index