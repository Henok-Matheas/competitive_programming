class Solution:
    def maxJump(self, stones: List[int]) -> int:
        jump = stones[1] - stones[0]
        for i in range(2, len(stones)):
            jump = max(jump, stones[i] - stones[i - 2])
            
        return jump
        