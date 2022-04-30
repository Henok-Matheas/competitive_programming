people, conditions = list(map(int, input().split()))
parents = [person for person in range(people)]
rank = [1] * people


def find(root):
    if root != parents[root]:
        parents[root] = find(parents[root])
    return parents[root]


def union(root1, root2):
    parent = find(root1)
    child = find(root2)

    if rank[child] > rank[parent]:
        parent, child = child, parent

    rank[parent] += rank[root2]
    parents[child] = parent
    return rank[parent]


max_ = -float("inf")
for condition in range(conditions):
    person1, person2 = list(map(int, input().split()))
    size = union(person1 - 1, person2 - 1)
    max_ = max(max_, size - 1)
    print(max_)
