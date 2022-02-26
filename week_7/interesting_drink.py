shops = int(input())
prices = input().split()
for i in range(shops):
    prices[i] = int(prices[i])
prices.sort()
days = int(input())
output = []

for i in range(days):
    coin = int(input())

    left = 0
    right = len(prices) - 1
    best = -1

    while left <= right:
        mid = (left + right) // 2

        if coin < prices[mid]:
            right = mid - 1
        else:
            best = mid
            left = mid + 1
    output.append(best + 1)
for j in output:
    print(j)
