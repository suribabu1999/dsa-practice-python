nums = [1,2,4,5,9,6,5,8,4,3,2,1]

duplactes =[]
sorted_li = []

#by removing duplicates sort the array and find the final sorted array

for n in nums:
    if n not in sorted_li:
        sorted_li.append(n)
print(sorted_li)
print("length ------------------>>>>",len(sorted_li))

for i in range(len(sorted_li)):
    for j in range(0,len(sorted_li)-i-1): #here in the first loop i = 0 , j = 0 , scnd loop i=1 but j = 7 -1 -1 = 5 , 
        if sorted_li[j] > sorted_li[j+1]:
            sorted_li[j], sorted_li[j+1] = sorted_li[j+1], sorted_li[j]
    
print("Sorted list",sorted_li)

list2 = [5,7,9,2,3,4,3]

for k in range(len(list2)):
    for n in range(0, len(list2)-k-1):
        if list2[n] > list2[n+1]:
            list2[n], list2[n+1] = list2[n+1], list2[n]
uni = []

[uni.append(x) for x in list2 if x not in uni]

print("uni",uni)
    

print(list2)