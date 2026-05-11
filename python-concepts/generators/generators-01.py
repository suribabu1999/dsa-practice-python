"""
COMPLETE PYTHON GENERATOR DEMO
Run this file to understand almost everything about generators
"""

import sys

print("\n==============================")
print("1. BASIC GENERATOR FUNCTION")
print("==============================")

def simple_generator():
    print("Generator started")
    yield 1
    print("Generator resumed")
    yield 2
    print("Generator resumed again")
    yield 3
    print("Generator finished")

g = simple_generator()

print("Generator object:", g)

print("\nCalling next()")
print(next(g))

print("\nCalling next() again")
print(next(g))

print("\nCalling next() third time")
print(next(g))

try:
    print("\nCalling next() fourth time")
    print(next(g))
except StopIteration:
    print("Generator is exhausted")


print("\n==============================")
print("2. GENERATOR WITH LOOP")
print("==============================")

def count_up_to(n):
    for i in range(1, n + 1):
        yield i

gen = count_up_to(5)

for number in gen:
    print("Generated:", number)


print("\n==============================")
print("3. GENERATOR VS LIST MEMORY")
print("==============================")

def generator_numbers(n):
    for i in range(n):
        yield i

list_numbers = [i for i in range(1000000)]
gen_numbers = generator_numbers(1000000)

print("List memory size:", sys.getsizeof(list_numbers))
print("Generator memory size:", sys.getsizeof(gen_numbers))


print("\n==============================")
print("4. GENERATOR EXPRESSION")
print("==============================")

gen_expr = (x*x for x in range(5))

print("Generator expression values:")
for val in gen_expr:
    print(val)


print("\n==============================")
print("5. GENERATOR WITH send()")
print("==============================")

def echo_generator():
    value = yield "Start"
    while True:
        value = yield f"You sent: {value}"

g = echo_generator()

print(next(g))  # start generator

print(g.send("Hello"))
print(g.send("Python"))
print(g.send("Generators"))


print("\n==============================")
print("6. GENERATOR close() METHOD")
print("==============================")

def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

g = infinite_numbers()

print(next(g))
print(next(g))
print(next(g))

g.close()

print("Generator closed")


print("\n==============================")
print("7. REAL WORLD EXAMPLE")
print("Processing large dataset lazily")
print("==============================")

def read_large_data():
    for i in range(1, 1000000000):
        yield f"Record {i}"

data_stream = read_large_data()

print(next(data_stream))
print(next(data_stream))
print(next(data_stream))
print("...only generating data when needed")


print("\n==============================")
print("8. PIPELINE GENERATORS")
print("==============================")

def numbers():
    for i in range(10):
        yield i

def square(nums):
    for n in nums:
        yield n*n

def even_filter(nums):
    for n in nums:
        if n % 2 == 0:
            yield n

pipeline = even_filter(square(numbers()))

for value in pipeline:
    print("Pipeline result:", value)


print("\n==============================")
print("END OF GENERATOR DEMO")
print("==============================")