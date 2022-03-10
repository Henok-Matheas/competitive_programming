import collections

tests = int(input())
answers = []

parallel = {True: "YES", False: "NO"}
for test in range(tests):
    n = int(input())

    temp = input().split()
    arr = []
    for t in range(n):
        arr.append(int(temp[t]))

    arr.sort(reverse=True)

    arr = collections.deque(arr)

    sumR = 0
    sumB = 0
    countR = 0
    countB = 0

    while arr:
        if sumR > sumB and countR < countB:
            break
        while arr and sumR <= sumB:
            sumR += arr.popleft()
            countR += 1
        while arr and countR >= countB:
            sumB += arr.pop()
            countB += 1
    answers.append(parallel[sumR > sumB and countR < countB])

for answer in answers:
    print(answer)