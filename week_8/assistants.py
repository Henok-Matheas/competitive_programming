def isAbsent(assistants, n):
    minim = assistants[0][0]
    maxim = assistants[0][1]

    for assistant in assistants:
        if minim <= assistant[0]:
            if assistant[0] - 1 <= maxim:
                maxim = max(maxim, assistant[1])
                minim = min(minim, assistant[1])
        else:
            return "YES"

    if maxim < n or minim > 0:
        return "YES"

    return "NO"


vals = input().split()

n = int(vals[0])
m = int(vals[1])

assistants = []
for i in range(m):
    asstnts = input().split()
    assistants.append([int(asstnts[0]), int(asstnts[1])])

assistants.sort()

print(isAbsent(assistants, n - 1))
