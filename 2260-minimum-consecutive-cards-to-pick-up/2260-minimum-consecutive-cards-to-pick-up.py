class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minim = len(cards) + 1
        unique = set()
        left = 0
        
        for right, num in enumerate(cards):
            while num in unique:
                minim = min(minim, right - left + 1)
                unique.remove(cards[left])
                left += 1
            unique.add(num)
        
        return -1 if minim == len(cards) + 1 else minim