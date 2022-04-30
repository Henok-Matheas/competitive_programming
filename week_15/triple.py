from collections import defaultdict

n = int(input())

answers = []
for i in range(n):
    size = int(input())
    strings = input().split()
    counting = defaultdict(int)
    final = -1
    for string in strings:
        number = int(string)
        counting[number] += 1
        if counting[number] >= 3:
            final = number
            break
    answers.append(final)

for answer in answers:
    print(answer)