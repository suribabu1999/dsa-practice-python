#we have one array we need to find the total sum value to certain range of elements.

list1 = [1,2,3,4,5,6,7,8,9]
n = len(list1)

prefix = [0] * (n+1)
print("prefix",prefix)

for i in range(n):
    prefix[i+1] = list1[i] + prefix[i]

print(prefix)

#from range x to y // l to r
x = 2
y = 6
result = prefix[y+1] - prefix[x]
print(result)

