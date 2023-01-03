class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        what if we sort using grow_time, and process the ones that take too much time to grow, while they are growing we can grow the others.
        
        code:
        firt sort it using growTime
        and take the largest first
        we grow it.
        next
        if next planting <= prev growing
            we plant the next while curr grows, we then take the maximum
            between what's left for prev_growing, and curr_growing
        else
            we grow unitl prev_growing ends.
            we take the rest of time left for curr planting and add it to total
            and take the curr growing
        """
        indices = [idx for idx in range(len(growTime))]
        indices.sort(reverse = True, key = lambda idx: [growTime[idx], -plantTime[idx]])
        total = 0
        prev_growing = 0
        for idx in indices:
            plant, grow = plantTime[idx], growTime[idx]
            total += plant
            
            growing_left = prev_growing - plant
            prev_growing = max(growing_left, grow)
        return total + prev_growing