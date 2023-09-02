class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0] * (n + 1)
        for idx in range(n + 1):
            current = idx
            while current != 0:
                answer[idx] += current & 1
                current = current >> 1
                
        return answer
            
        