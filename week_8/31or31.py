from collections import deque


def answerer(k):
    parents = deque([])
    children = deque([])
    visited = set([])

    parents.append([31, 31])
    parents.append([32, 32])
    visited.add(31)
    visited.add(32)

    answer = None
    while parents or children:
        while parents:
            parent = parents.popleft()

            if parent[0] == k and not answer:
                return parent[1]
            elif parent[0] < k:
                children.append([parent[0] + 4, parent[1]])
            else:
                children.append([parent[0] - 1, parent[1]])

        while children:
            child = children.popleft()
            visited.add(child[0])
            parents.append(child)


tests = int(input())

targets = []
for i in range(tests):
    targets.append(int(input()))

for target in targets:
    print(answerer(target))
