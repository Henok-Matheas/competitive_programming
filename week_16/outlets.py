t = int(input())

answers = []

for test in range(t):
    total = 2
    n, m = list(map(int, input().split()))
    dividers = list(map(int, input().split()))

    if n <= 2:
        answers.append(0)
        continue
    dividers.sort(reverse=True)

    i = 0
    while total < n and i < len(dividers):
        total += dividers[i] - 1
        i += 1
    answers.append(i if total >= n else -1)

for answer in answers:
    print(answer)