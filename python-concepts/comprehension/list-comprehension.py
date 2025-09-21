#list comprehension'

#syntax [expression for item in iterble if condition]
n=100
list1 = [x for x in range(1,n+1)] #list of 100 number
print(list1)

#lets find evens
evens = [x for x in range(1,n+1) if x %2 == 0]
print(evens)

#odds 

odds = [x for x in range(1,n+1) if x%2 != 0]
print(odds)
