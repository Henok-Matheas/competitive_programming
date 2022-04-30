inputs = input().split()

charge1 = int(inputs[0])
charge2 = int(inputs[1])

answer = 0
while (charge1 > 0 and charge2 > 0) and max(charge1, charge2) > 1:
    answer += 1
    value1 = min(charge1, charge2)
    value2 = max(charge1, charge2)
    charge1 = value1 + 1
    charge2 = value2 - 2

print(answer)
