def find_min(arr) -> int:
    n = len(arr)
    min = arr[0]
    for i in range(n):
        if arr[i] < min:
            min = arr[i]
    return min

print(find_min([6,555,8,9,10,98,1]))