size = int(input())
given = input().split()

for i in range(size):
    given[i] = int(given[i])

left = 2
right = len(given) if len(given) % 2 == 0 else len(given) - 1
best = 2

while left <= right:
    mid = (left + right) // 2

    i = 0

    works = True
    while i <= len(given) - mid - 1:
        p1 = i
        p2 = i + mid
        first = given[i]
        second = given[i + mid]

        while p1 < p2:
            if given[p1] != first:
                works = False
                break
            p1 += 1
        while p2 < len(given):
            if given[p2] != second:
                works = False
            p2 += 1
        i += 1

    if works == False:
        right = mid - 2
    else:
        best = mid
        left = mid + 2

print(best)