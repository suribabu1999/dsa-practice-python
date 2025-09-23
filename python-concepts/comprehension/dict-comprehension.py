squares = {x: x**2 for x in range(5)}
print(squares)

even_squares = {x : x**2 for x in range(50) if x%2==0}
print(even_squares)


ls = [1,3,4,5,6,7,8,9,3,44,66,88]

#cubes of even numbers present in list 

cubes= { x:x**3 for x in ls if x %2 ==0}
print(cubes) 