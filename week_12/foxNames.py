from collections import defaultdict

n = int(input())
names = []
for i in range(n):
    names.append(input().strip("\n"))

path = set()
visited = set()

impossible = []

answer = []


def dfs(node):
    if len(impossible) > 0:
        return
    for child in graph[node]:
        if child in path:
            impossible.append("Impossible")
            return
        elif child in visited:
            continue
        visited.add(child)
        path.add(child)
        dfs(child)
    answer.append(node)
    path.remove(node)


graph = defaultdict(set)

i = 0
while i < len(names) - 1:
    if names[i] != names[i + 1]:
        idx = 0
        while idx < len(names[i]) and idx < len(
                names[i]) and names[i][idx] == names[i + 1][idx]:
            idx += 1
        first = names[i][idx] if idx < len(names[i]) else None
        second = names[i + 1][idx] if idx < len(names[i + 1]) else None
        if second != None and first != None:
            graph[first].add(second)
        elif first != None:
            graph[first].update(set())
        elif second != None:
            graph[second].update(set())
    else:
        graph[i].update(set())
    i += 1

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
for letter in letters:
    if letter in graph and letter not in visited:
        visited.add(letter)
        path.add(letter)
        dfs(letter)
letterset = set([
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
])
answer = answer[::-1]
final = []
for letter in answer:
    letterset.remove(letter)
    final.append(letter)

for letter in letterset:
    final.append(letter)
print("".join(final) if len(impossible) == 0 else impossible[0])
