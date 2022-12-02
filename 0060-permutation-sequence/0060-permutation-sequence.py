class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        order = [str(idx) for idx in range(1, n + 1)]
        permtuation = [1]
        for idx in range(2, n):
            permtuation.append(permtuation[-1] * idx)
        k -= 1
        answer= []
        
        while permtuation:
            perm = permtuation.pop()
            div, rem = k // perm, k % perm
            answer.append(order.pop(div))
            k = rem
        if order:
            answer.append(order.pop())
        return "".join(answer)
        