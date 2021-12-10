def insertionSort1(n, arr):
    if n < 2:
        print(arr)
        return 0
    for i in range(n - 2,0):
        print(i)
        print('hello')
        for j in range(i,n - 2):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)



insertionSort1(5,[2,4,6,8,3])