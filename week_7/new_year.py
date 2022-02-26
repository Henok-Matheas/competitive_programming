listi = input().split()

n = int(listi[0])
k = int(listi[1])


def solved(n, k):
    max_time = 1440 - k
    left = 1
    right = n
    best = 0

    while left <= right:
        mid = (left + right) // 2

        tot = (mid * (mid + 1) // 2)

        time = 5 * tot + 1200

        if time > max_time:
            right = mid - 1
        else:
            best = mid
            left = mid + 1
    return best


print(solved(n, k))
