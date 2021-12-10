max_value =5

def counting_sort(arr,max_value):
    new = [0]*(max_value+1)
    for i in arr:
        new[i]+=1
    return new[:]

print(counting_sort([1,4,3,2,4,3,2,1,4,3,4,4,5,5,2,2],5))