def reverse_list(arr):
    n = len(arr)
    result = []

    for i in range(len(arr)-1, -1,-1):
        result.append(arr[i])
    return result

print(reverse_list([1,2,3,4,5]))

