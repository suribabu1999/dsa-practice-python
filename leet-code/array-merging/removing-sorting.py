def removing(arr):
    k = 1
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i] != arr[k-1]:
            arr[k] = arr[i]
            k+=1
    return arr
        

arr = removing([5,4,3,3,3,2,2,1,2])
print(arr)