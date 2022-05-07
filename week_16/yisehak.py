n = int(input())

answers = []
for column in range(n):
    hidden = 0
    number = int(input())
    students = list(map(int, input().split()))

    i = len(students) - 2
    max_ = students[-1]
    while i >= 0:
        if max_ > students[i]:
            hidden += 1
        else:
            max_ = max(max_, students[i])
        i -= 1
    answers.append(hidden)

for answer in answers:
    print(answer)