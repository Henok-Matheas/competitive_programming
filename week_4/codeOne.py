num, l, r = list(map(int, input().split()))

import math

def log(r, count):
    if r == 1 or r == 0:
        return count
    return log(r // 2, count + 1)


h = log(num, 0)
right = 2 ** (h) + 2 ** h - 1
left = 1

def codeOne(num, left, right, l, r):
    if l <= left <= right <= r:
        return num
    elif left > r or right < l:
        return 0
    return (
        codeOne(num // 2, left, (((left + right) // 2) - 1), l, r)
        + codeOne(num % 2, (left + right) // 2, (left + right) // 2, l, r)
        + codeOne(num // 2, (left + right) // 2 + 1, right, l, r)
    )


print(codeOne(num, left, right, l, r))
