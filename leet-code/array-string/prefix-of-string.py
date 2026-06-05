arr = ['suri','surya','sun']

arr.sort()
print(arr)
print(arr[:-1])

start = arr[0]
end = arr[-1]
prefix = ''

for i in range(len(arr)):
    if start[i] == end[i]:
        prefix = prefix + start[i]
    else:
        break
print(prefix)

    