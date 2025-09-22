def find_max(arr) -> int:
    n = len(arr)
    max = arr[0]
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
    return max

print(find_max([6,555,8,9,10,98]))