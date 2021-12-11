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


    # num=arr[-1]
    # for i in range(n - 1,0,-1):
    #     for j in range(i,n - 1):
    #         if num == None or arr[j] > num:
    #             arr[j - 1] = arr[j]
    #             print(arr)
    #             continue
    #         else:
    #             arr[j - 1] = num
    #             print(arr)
    #             break


insertionSort1(14,[1,3,5,9,13,22,27,66,46,51,55,83,87,23])
# insertionSort1(3,[3,2,1])