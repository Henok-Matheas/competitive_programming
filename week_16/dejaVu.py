import collections

t = int(input())
answers = []

for _ in range(t):
    word = collections.deque()
    for char in input():
        word.append(char)
    if not word:
        answers.append('NO')
        continue

    first = []
    second = []
    possible = False
    while word:
        if word[0] != "a":
            word.append("a")
            possible = True
            break
        elif word[-1] != "a":
            word.appendleft("a")
            possible = True
            break
        first.append(word.popleft())
        if word:
            second.append(word.pop())

    if possible:
        answers.append("YES")
        answers.append(("".join(first).strip() + "".join(word).strip() +
                        "".join(second[::-1]).strip()).strip())
    else:
        answers.append("NO")

for answer in answers:
    print(answer)