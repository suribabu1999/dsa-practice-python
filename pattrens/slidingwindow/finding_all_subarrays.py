def all_sub_arrays(arr) -> list[list]:
    n = len(arr)
    sub_arrays = []

    for start in range(n):
        for end in range(start,n):
            sub_arrays.append(arr[start:end+1])
    return sub_arrays
            
l1 = [1,2,3,4,5,6,7,8,9]
# print("All Sub arrays",all_sub_arrays(l1), end=" ")

allarrays = all_sub_arrays(l1)
allarrays.sort()
print(allarrays)