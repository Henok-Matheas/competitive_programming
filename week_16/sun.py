from collections import defaultdict

chair_count, m = list(map(int, input().split()))
x_greater = defaultdict(set)
x_less = defaultdict(set)
y_greater = defaultdict(set)
y_less = defaultdict(set)

chairs = defaultdict(int)

answers = []
for chair_input in range(chair_count):
    chr = list(map(int, input().split()))
    chair = (chr[1], chr[0])
    chairs[chair] += 1
for chr in chairs:
    for chair in chairs:
        if chair[0] <= chr[0]:
            x_less[chr[0]].add(chair)

        if chair[0] >= chr[0]:
            x_greater[chr[0]].add(chair)

        if chair[1] <= chr[1]:
            y_less[chr[1]].add(chair)

        if chair[1] >= chr[1]:
            y_greater[chr[1]].add(chair)

for rct_input in range(m):
    rect = list(map(int, input().split()))
    upperx = rect[1]
    while upperx not in x_greater and upperx <= 100:
        upperx += 1
    uppery = rect[0]
    while uppery not in y_greater and uppery <= 100:
        uppery += 1
    lowerx = rect[3]
    while lowerx not in x_less and lowerx >= 0:
        lowerx -= 1
    lowery = rect[2]
    while lowery not in y_less and lowery >= 0:
        lowery -= 1

    x_grt = x_greater[upperx]
    x_lss = x_less[lowerx]
    y_grt = y_greater[uppery]
    y_lss = y_less[lowery]

    x_intr = x_lss.intersection(x_grt)
    y_intr = y_lss.intersection(y_grt)

    final = x_intr.intersection(y_intr)
    total = 0
    for chair in final:
        total += chairs[chair]

    if upperx > lowerx or uppery > lowery:
        total = 0

    answers.append(total)

for answer in answers:
    print(answer)