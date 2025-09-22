def sqares_of_all(arr):
    n = len(arr)
    result = [0]*n
    for i in range(len(arr)):
        result[i] = arr[i]**2
    result.sort()
    return result

print(sqares_of_all([3,5,4,3,2]))