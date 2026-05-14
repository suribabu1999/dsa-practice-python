n = 121
original = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not palindrome")