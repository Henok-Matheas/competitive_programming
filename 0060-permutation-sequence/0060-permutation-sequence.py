class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        order = [str(idx) for idx in range(1, n + 1)]
        answer= []
        fac = [1,1]
        
        for idx in range(2, n):
            fac.append(fac[-1] * idx)
            
        k -= 1
        while n:
            perm = fac.pop()
            div, k = divmod(k, perm)
            answer.append(order.pop(div))
            n -= 1
            
        return "".join(answer)
        