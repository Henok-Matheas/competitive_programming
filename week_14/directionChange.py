import collections

t = int(input())

sizes = []

for val in range(t):
    value = input().split()
    n = int(value[0])
    m = int(value[1])
    sizes.append([n, m])

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

answers = []
for size in sizes:
    n = size[0]
    m = size[1]

    if n == 1 and m == 1:
        answers.append(0)
        continue

    elif n == 1 and m > 2 or m == 1 and n > 2:
        answers.append(-1)
        continue

    elif n == 1 and m == 2 or m == 1 and n == 2:
        answers.append(1)
        continue

    maxim = max(n, m) - 1
    minim = min(n, m) - 1

    times = maxim // minim

    final = minim * 2 * times

    left = maxim % minim

    if left == 1:
        final += 1
    else:
        final += (left * 2)
    answers.append(final)

for answer in answers:
    print(answer)