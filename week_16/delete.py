s = input()
t = input()

i = len(s) - 1
j = len(t) - 1

while i >= 0 and j >= 0:
    if s[i] == t[j]:
        i -= 1
        j -= 1
    else:
        break

answer = 0 + abs(0 - i - 1) + abs(0 - j - 1)
print(answer)