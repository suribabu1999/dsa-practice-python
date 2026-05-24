t1 = (1,2,3,4,5,6)
t2 = (3,4,5,6,5,6,7,8,9,6,5,4,3,4,3,4,5,5,6,6)
l2 = []
unique = []


for i in range(len(t1)):
    for j in range(len(t2)):
        if t1[i] == t2[j]:
            l2.append(t1[i])
print("Common elemnt", l2)

#removing duplicates 

for item in l2:
    if item not in unique:
        unique.append(item)

print("Unique elements in common",unique)