def second_highest(arr):
    freq = {}

    for element in arr:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    highest = 0
    for count in freq.values():
        if count > highest:
            highest = count
    # print(highest)
    
    second = 0

    for count in freq.values():
        if count < highest and count > second:
            second =  count
    # print(second)

    result = -1

    for num in freq:
        if freq[num] == second and num > result:
            result = num
    return num



a=second_highest([1,2,3,3,3,4,4,4,5,6])
print(a)
