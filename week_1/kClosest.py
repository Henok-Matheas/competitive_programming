import math
def kClosest(points, k):
    "uses the default method for lists, the sort method."
    dis_points = []
    closest_points = []
    for point in points:
        distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
        dis_points.append([point,distance])

    dis_points.sort(key = lambda x: x[1])
    for i in range(k):
        closest_points.append(dis_points[i][0])

    return closest_points
        



# points = [[1,3],[-2,2]]
# k = 1
# # Output: [[-2,2]]

points = [[3,3],[5,-1],[-2,4]]
k = 2
# Output: [[3,3],[-2,4]]


print(kClosest(points,k))