n = int(input())

nums = input().split()
numbers = []

for num in nums:
    numbers.append(int(num))


def One(numbers):
    count = 0
    zero = 0
    negatives = 0
    for number in numbers:
        if number == 0:
            zero += 1
            continue
        elif number < 0:
            count += abs(number + 1)
            negatives += 1
        else:
            count += abs(number - 1)

    if negatives % 2 != 0:
        count += zero if zero != 0 else 2
    else:
        count += zero
    return count


print(One(numbers))