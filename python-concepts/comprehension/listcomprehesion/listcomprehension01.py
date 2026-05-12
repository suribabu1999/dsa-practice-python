"""
COMPLETE LIST COMPREHENSION DEMO
Run this file to understand everything about list comprehensions
"""

import sys

print("\n==============================")
print("1. BASIC LIST CREATION (WITHOUT COMPREHENSION)")
print("==============================")

numbers = []
for i in range(10):
    numbers.append(i)

print("Normal loop list:", numbers)


print("\n==============================")
print("2. BASIC LIST COMPREHENSION")
print("==============================")

numbers = [i for i in range(10)]

print("List comprehension:", numbers)


print("\n==============================")
print("3. SQUARE NUMBERS")
print("==============================")

squares = [x*x for x in range(10)]

print("Squares:", squares)


print("\n==============================")
print("4. FILTER EVEN NUMBERS")
print("==============================")

even_numbers = [x for x in range(20) if x % 2 == 0]

print("Even numbers:", even_numbers)


print("\n==============================")
print("5. FILTER ODD NUMBERS")
print("==============================")

odd_numbers = [x for x in range(20) if x % 2 != 0]

print("Odd numbers:", odd_numbers)


print("\n==============================")
print("6. IF-ELSE IN LIST COMPREHENSION")
print("==============================")

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]

print("Labels:", labels)


print("\n==============================")
print("7. STRING MANIPULATION")
print("==============================")

names = ["python", "java", "c++", "go"]

upper_names = [name.upper() for name in names]

print("Uppercase:", upper_names)


print("\n==============================")
print("8. LENGTH OF EACH WORD")
print("==============================")

lengths = [len(word) for word in names]

print("Word lengths:", lengths)


print("\n==============================")
print("9. MULTIPLE FOR LOOPS")
print("==============================")

pairs = [(x, y) for x in range(3) for y in range(3)]

print("Pairs:", pairs)


print("\n==============================")
print("10. MATRIX FLATTENING")
print("==============================")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flatten = [num for row in matrix for num in row]

print("Flatten matrix:", flatten)


print("\n==============================")
print("11. NESTED LIST COMPREHENSION")
print("==============================")

matrix_square = [[x*x for x in row] for row in matrix]

print("Squared matrix:", matrix_square)


print("\n==============================")
print("12. REMOVE EMPTY STRINGS")
print("==============================")

data = ["apple", "", "banana", "", "cherry"]

clean_data = [x for x in data if x]

print("Clean list:", clean_data)


print("\n==============================")
print("13. DICTIONARY COMPREHENSION")
print("==============================")

square_dict = {x: x*x for x in range(6)}

print("Dictionary:", square_dict)


print("\n==============================")
print("14. SET COMPREHENSION")
print("==============================")

set_example = {x % 3 for x in range(10)}

print("Set:", set_example)


print("\n==============================")
print("15. CONDITIONAL DICTIONARY")
print("==============================")

even_square_dict = {x: x*x for x in range(10) if x % 2 == 0}

print("Even square dict:", even_square_dict)


print("\n==============================")
print("16. GENERATOR VS LIST COMPREHENSION")
print("==============================")

list_comp = [x for x in range(1000000)]
gen_exp = (x for x in range(1000000))

print("List memory:", sys.getsizeof(list_comp))
print("Generator memory:", sys.getsizeof(gen_exp))


print("\n==============================")
print("17. REAL WORLD EXAMPLE: FILE PROCESSING")
print("==============================")

lines = [
    "  Python  ",
    " Java ",
    "  Go  ",
    "Rust "
]

clean_lines = [line.strip().lower() for line in lines]

print("Processed lines:", clean_lines)


print("\n==============================")
print("18. FILTERING OBJECT DATA")
print("==============================")

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 30}
]

adult_users = [user["name"] for user in users if user["age"] >= 18]

print("Adults:", adult_users)


print("\n==============================")
print("19. CREATE CARTESIAN PRODUCT")
print("==============================")

colors = ["red", "blue"]
sizes = ["S", "M", "L"]

products = [(c, s) for c in colors for s in sizes]

print("Product combinations:", products)


print("\n==============================")
print("20. PIPELINE STYLE PROCESSING")
print("==============================")

data = [1,2,3,4,5,6]

result = [x*x for x in data if x % 2 == 0]

print("Square of even numbers:", result)


print("\n==============================")
print("END OF LIST COMPREHENSION DEMO")
print("==============================")