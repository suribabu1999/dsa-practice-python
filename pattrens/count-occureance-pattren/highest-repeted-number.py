nums = [1,2,3,3,4,2,8,8,8,8,9,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,55,5,5,5,5,5,5,5,5,5,5]
rep = {}
arr = []

for num in nums:
    if num in rep:
        rep[num] += 1
    else:
        rep[num]=1

maxcount = 0
answer = None
for key,value in rep.items():
    if value > maxcount:
        maxcount =  value
        answer = key
    

print("highest repeted number", answer)
print("no of time ", maxcount)