import math


def good(students, question):
    # print(len(students))
    if students[(len(students) - 1) // 2] < question:
        return "NO"
    #
    if students[0] >= question:
        return "NO"
    return "YES"


vals = input().split()

n = int(vals[0])
m = int(vals[1])

students = []
studs = input().split()
for stud in range(m):
    students.append(int(studs[stud]))

students.sort()

questions = []
for idx in range(n):
    questions.append(int(input()))

for question in questions:
    print(good(students, question))
