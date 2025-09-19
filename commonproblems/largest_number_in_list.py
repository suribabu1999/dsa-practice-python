# Method 1: Using built-in max()
numbers = [10, 45, 2, 99, 23, 67]
largest = max(numbers)
print("Largest number is:", largest)



numbers = [10, 45, 2, 99, 23, 67]


largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
