vals = input().split()
n = int(vals[0])
m = int(vals[1])
print("this is n", n)
students = []
studs = input().split()
# print(studs, "this is m", m)
for stud in range(n):
    students.append(int(studs[stud]))

# this should be a list of lists
members = [[]] * n
for idx in range(n):
    if students[idx] == idx:
        continue
    members[students[idx]].append(idx)
coverage = [0] * m

topices = []
visited = set()
for i in range(n):
    all = input().split()
    tot_topics = int(all[0])
    i = 1

    temp = []
    while i < len(all):
        if not all[i] in visited:
            temp.append(int(all[i]))
            visited.add(all[i])
        i += 1
    topices.append(temp)

for student in range(n):
    multiplier = members[student]
    for topic in topices[student]:
        coverage[topic] += multiplier

stringi = ""
for cover in coverage:
    stringi += " " + str(cover)

stringi.strip()
print("these are the topics each student knows", topices)
print("these are the members", members)
print(stringi)
