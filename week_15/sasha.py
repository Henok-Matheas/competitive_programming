# the optimized answer is, 0(1) SOLUTION
n, v = list(map(int, input().split()))
v = n - 1 if v >= n else v
print(v - 1 + ((n - v) * (n - v + 1) // 2))

# n-squared version.
inputs = input().split()

n = int(inputs[0])
v = int(inputs[1]) if int(inputs[1]) < n else n - 1
numbers = [0] * n
numbers[0] = v
valid = lambda row: row >= 0

for index in range(1, n):
    birr = index + 1
    best = float("inf")
    for prev in range(index - v, index):
        if not valid(prev):
            continue
        pay = (numbers[prev] +
               ((index - prev) * birr)) if index < n - 1 else numbers[prev]
        best = min(best, pay)
    numbers[index] = best
print(numbers[-1])
