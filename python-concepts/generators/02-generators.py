import sys

def generate_square(num):
    for x in range(num):
        yield x**2



print(generate_square(10)) #returns object reference  like <generator object generate_square at 0x000001E2D29E9490>


# first way using for loop 
for num in generate_square(10):
    print(num)

print("<->"*50)

#using next method 
second = generate_square(10)
print(next(second))
print(next(second))
print(next(second))
print(next(second))
print(next(second))
print(next(second))
