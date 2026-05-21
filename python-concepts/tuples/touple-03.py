"""
BIG TUPLE DEMONSTRATION PROGRAM
Covers almost every tuple concept in Python
"""

print("\n--- TUPLE CREATION ---")

t1 = (1, 2, 3, 4)
print("Tuple with parentheses:", t1)

t2 = 5, 6, 7, 8
print("Tuple without parentheses:", t2)

single = (10,)
print("Single element tuple:", single)

t3 = tuple([9, 8, 7])
print("Tuple from list:", t3)

t4 = tuple("python")
print("Tuple from string:", t4)

t5 = tuple(range(5))
print("Tuple from range:", t5)



print("\n--- INDEXING ---")

print("First element:", t1[0])
print("Last element:", t1[-1])



print("\n--- SLICING ---")

print("First three:", t1[:3])
print("Middle slice:", t1[1:3])
print("Reverse tuple:", t1[::-1])



print("\n--- IMMUTABILITY DEMO ---")

t = (1, 2, 3)

try:
    t[0] = 100
except TypeError as e:
    print("Cannot modify tuple:", e)



print("\n--- TUPLE OPERATIONS ---")

a = (1, 2)
b = (3, 4)

print("Concatenation:", a + b)
print("Repetition:", a * 3)

print("Membership check:", 2 in a)



print("\n--- TUPLE METHODS ---")

nums = (1, 2, 2, 3, 4, 2)

print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))



print("\n--- LOOPING THROUGH TUPLE ---")

languages = ("Python", "Java", "Go", "Rust")

print("Using for loop")

for lang in languages:
    print(lang)


print("\nUsing index loop")

for i in range(len(languages)):
    print(i, languages[i])



print("\n--- PACKING ---")

person = ("Alice", 25, "Engineer")
print("Packed tuple:", person)



print("\n--- UNPACKING ---")

name, age, job = person

print("Name:", name)
print("Age:", age)
print("Job:", job)



print("\n--- EXTENDED UNPACKING ---")

numbers = (1,2,3,4,5,6)

a,b,*rest = numbers

print("a:", a)
print("b:", b)
print("rest:", rest)



print("\n--- NESTED TUPLES ---")

matrix = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

print("Matrix:", matrix)
print("Access nested element:", matrix[1][2])



print("\n--- MUTABLE OBJECT INSIDE TUPLE ---")

t = ([1,2], [3,4])

t[0].append(99)

print("Tuple with modified list:", t)



print("\n--- FUNCTION RETURNING TUPLE ---")

def get_user():
    name = "Bob"
    age = 30
    return name, age

user = get_user()

print("Function returned tuple:", user)

name, age = get_user()

print("Unpacked values:", name, age)



print("\n--- TUPLE COMPARISON ---")

t1 = (1,2,3)
t2 = (1,2,4)

print("t1 < t2:", t1 < t2)



print("\n--- TUPLE AS DICTIONARY KEY ---")

coordinates = {}

point = (10,20)

coordinates[point] = "Location A"

print("Dictionary with tuple key:", coordinates)



print("\n--- SWAPPING VARIABLES USING TUPLE ---")

x = 5
y = 10

print("Before swap:", x, y)

x, y = y, x

print("After swap:", x, y)



print("\n--- LIST TO TUPLE ---")

list_data = [1,2,3]

tuple_data = tuple(list_data)

print("Converted tuple:", tuple_data)



print("\n--- TUPLE TO LIST ---")

t = (4,5,6)

list_version = list(t)

print("Converted list:", list_version)



print("\n--- ITERATING WITH ENUMERATE ---")

colors = ("red", "green", "blue")

for index, value in enumerate(colors):
    print(index, value)



print("\n--- USING ZIP WITH TUPLES ---")

names = ("Alice", "Bob", "Charlie")
scores = (90, 85, 88)

combined = tuple(zip(names, scores))

print("Zipped tuple:", combined)



print("\n--- MAX MIN SUM ---")

nums = (5,10,15,20)

print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))



print("\n--- SORTED TUPLE ---")

t = (4,1,3,2)

sorted_tuple = tuple(sorted(t))

print("Sorted tuple:", sorted_tuple)



print("\n--- LENGTH OF TUPLE ---")

print("Length:", len(t))



print("\n--- FINAL MESSAGE ---")

print("You just reviewed almost every important tuple concept in Python!")