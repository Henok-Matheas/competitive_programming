def selectionSort1(n,arr):
    for i in range(len(arr)):
        low_index = i
        for j in range(i,len(arr)):
            if arr[j] < arr[low_index]:
                low_index = j
        arr[i] , arr[low_index] = arr[low_index] , arr[i]
    return arr

arr = [1,3,5,9,13,22,27,66,46,51,55,83,87,23]
arr_len = 14
print(selectionSort1(arr_len,arr))
# insertionSort1(3,[3,2,1])