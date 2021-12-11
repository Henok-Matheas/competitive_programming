def insertionSort1(n, arr):
    if n < 2:
        print(arr)
        return 0
    for i in range(n-1):
        num=arr[i+1]
        for j in range(i,-1,-1):
            if num >= arr[j]:
                arr[j + 1] = num
                print(arr)
                break
            else:
                arr[j + 1],arr[j] = arr[j],arr[j + 1]
                print(arr)



insertionSort1(5,[2,4,6,8,3])