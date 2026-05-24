t = tuple("python")
t2 = tuple("SURI")
# t3 = t + t2 # concatination happeins 
# print(t)

# l1 = list(t)
# print(l1)
# l1.append(6)
# print(l1)
# print(t3)

#tuple accessing [Elements]
a = t[0]
b = t[1]

print("ELement at t[0]",a)
print("ELement at t[1]",b)

# 1. Reverse a tuple
# 2. Find maximum number
# 3. Count occurrences
# 4. Merge two tuples
# 5. Convert tuple to string
# 6. Remove duplicates
# 7. Sort tuple values
# 8. Find common elements
# 9. Flatten nested tuples
# 10. Swap tuples

t2 = (1,2,3,4,5,6,7,9)
t2 = list(t2)
rev_t2 = t2[::-1]
print("reversed tuple", rev_t2)
print("before reversing ---->",t2)
for i in range(len(t2)//2):
    t2[i], t2[len(t2)-i-1] = t2[len(t2)-i-1],t2[i]
print("after reversing ---->",t2)
    

