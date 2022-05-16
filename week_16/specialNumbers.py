t = int(input())

answers = []
for _ in range(t):
    sum = 0
    count = 0
    n, k = list(map(int, input().split()))
    num = k
    while num > 0:
        bn = bin(num)
        sum += n**count if bn[len(bn) - 1] == '1' else 0
        count += 1
        num >>= 1
    answers.append(sum % (7 + 10**9))

for answer in answers:
    print(answer)
