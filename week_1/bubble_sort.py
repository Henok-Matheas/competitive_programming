n = [10,9,8,7,6,5,4]

def bubble_sort(n):
    count=0
    sorted = [0] * len(n)
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                count+=1
                sorted[j] , sorted[j + 1] = n[j + 1] , n[j]
            else:
                sorted[j] , sorted[j + 1] = n[j], n[j + 1]
    return (sorted,count)


print(bubble_sort(n))