def sum_of_elements(arr)-> int :
    n = len(arr)
    sum = 0

    for i in range(n):
        sum = sum + arr[i]
    return sum

print(sum_of_elements([1,2]))