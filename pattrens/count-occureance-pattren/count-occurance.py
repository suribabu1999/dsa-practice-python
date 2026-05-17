nums = [1,1,2,2,2,2,2,2,2,3,3,3,3,36,6,6,6,6,6,7,7,7,]

count = {}

for num in nums:
    if num in count:
        count[num]+= 1
    else:
        count[num] = 1

print(count)