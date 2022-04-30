cities = int(input())

parents = [city for city in range(cities)]

redundant = []


# print("parents are", parents)
def find(root):
    if root != parents[root]:
        parents[root] = find(parents[root])
    return parents[root]


def union(root1, root2):
    parent = find(root1)
    child = find(root2)

    parents[child] = parent


for line in range(cities - 1):
    citys = input().split()
    city1 = int(citys[0]) - 1
    city2 = int(citys[1]) - 1

    if find(city1) == find(city2):
        redundant.append([city1, city2])
    union(city1, city2)

# print("the redundant paths are", redundant)

need_connection = []
for parent in range(len(parents)):
    if parent == parents[parent]:
        need_connection.append(parent)
# print("the need connections are", need_connection)
days = len(redundant)
print(days)
first = None
for day in range(days):
    u = need_connection.pop()
    v = need_connection.pop()
    need_connection.append(v)
    i, j = redundant.pop()
    print(i + 1, j + 1, u + 1, v + 1)
