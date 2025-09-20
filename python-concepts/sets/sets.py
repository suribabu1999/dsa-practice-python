l1 = [1,2,3,4,5,6,7]
l2 = [3,4,5,6,7,8,9]

set1 = set(l1) 
set2 = set(l2)

print(set1)
print(set2)

#we can perform 4 operations 

#1 union #2 intersection #

set3 = set1 | set2
print("Union",set3) #by removing duplicates all common elements present in both sets
                    #set doesn't allow duplicates in it 

set4 = set1 & set2
print("intersection",set4) #common elements

#add element to set 1
print("Before adding element",set1)
set1.add(10) #adding element
print(set1)
set1.remove(4) #removing element
print(set1)

#checking existence of elements

print(3 in set1)
