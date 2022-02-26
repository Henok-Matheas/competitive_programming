tests = int(input())
answer = []
for i in range(tests):
    first = input().split()
    second = input().split()

    n = int(first[0])
    h = int(first[1])
    times = []

    for time in second:
        times.append(int(time))

    left = 1
    right = h
    best = 0

    while left <= right:
        k = (left + right) // 2

        damage = 0
        for idx in range(len(times) - 1):
            damage += min(k, (times[idx + 1] - times[idx]))
        damage += k

        if damage < h:
            left = k + 1
        else:
            best = k
            right = k - 1
    answer.append(best)
for j in answer:
    print(j)
