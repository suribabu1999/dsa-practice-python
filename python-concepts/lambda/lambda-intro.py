
#A lambda function is essentially like a normal function but with a single expression and no name.

#normal function
def sum(x,y):
    return x + y
sum1 = sum(2,3)
print(sum1)

#lambda function .. in here "lambda" -> keyword ::: (x,y) -> parameters :::  : -> colon after Expression
sum2 = lambda x,y: x+y
sum3 = sum2(4,5)
print(sum3)

#do some basics practice on sqare , cube , even , odd muliplcation

sqare = lambda x : x ** 2
print("Square of given number",sqare(6))
 
cube = lambda x : x ** 3
print("Cube of given number ", cube(2))

even = lambda x : x % 2 == 0

print(even(4))
