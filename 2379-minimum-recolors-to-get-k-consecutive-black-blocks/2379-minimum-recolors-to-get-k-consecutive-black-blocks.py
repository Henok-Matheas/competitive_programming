class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        minim = k
        count = 0
        for right, block in enumerate(blocks):
            count += int(block == "W")
            if right - left + 1 == k:
                minim = min(count, minim)
                count -= int(blocks[left] == "W")
                left += 1
        return minim
            
            