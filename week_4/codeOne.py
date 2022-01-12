# num, l, r = list(map(int, input().split()))

num = 2 ** 50
l = 10 ** 5 - 1
r = 10 ** 5


def log(r, count):
    if r == 1 or r == 0:
        return count
    return log(r // 2, count + 1)


h = log(r, 0)
right = 2 ** (h) + 2 ** h - 1
left = 1


def codeOne(num, left, right, l, r):
    # print("this is when we choose three alternatives","the left is ",left, " the right is ",right," the num is ",num)
    # if left > right:
    #     return 0
    if l <= left <= right <= r:
        # print("the left is ",left, " the right is ",right," the num is ",num)
        return num
    elif num == 0 or num == 1:
        return 0
    elif left > r or right < l:
        return 0
    return (
        codeOne(num // 2, left, (((left + right) // 2) - 1), l, r)
        + codeOne(num % 2, (left + right) // 2, (left + right) // 2, l, r)
        + codeOne(num // 2, (left + right) // 2 + 1, right, l, r)
    )


# print("height is ",logar(r,0))
# print("right is ",right)

print(codeOne(num, left, right, l, r))
