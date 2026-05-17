nums = [1,2,3,1,4,2,8,8,8,8,9,6,6,6,6]
count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print(count)

for i, k in count.items():
    value = k
    # print("key", i, "value",k)
    if value > 1:
        print("Duplacte item", i, "times",value )