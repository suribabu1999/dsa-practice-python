# Python Comments – Complete Notes

## 1. Introduction

Comments in Python are **non-executable text** used to explain code.  
They help developers understand:

- What the code does
- Why the code exists
- Important warnings or notes
- Documentation for functions and modules

Python **ignores comments during execution**.

Example:

```python
# This is a comment
print("Hello World")
```

Output:

```
Hello World
```

---

# 2. Why Comments Are Important

Comments are essential for:

### Code Readability
They help other developers understand the code.

### Debugging
You can temporarily disable code using comments.

### Documentation
Explain logic, algorithms, and functions.

### Collaboration
Useful when multiple developers work on the same project.

---

# 3. Types of Comments in Python

Python mainly supports the following types:

1. **Single-line comments**
2. **Inline comments**
3. **Multi-line comments**
4. **Docstrings (documentation comments)**

---

# 4. Single-Line Comments

Single-line comments start with **`#`**.

Everything after `#` on that line is ignored.

### Syntax

```python
# This is a single line comment
```

### Example

```python
# Calculate the sum
a = 10
b = 20

# Add numbers
result = a + b

print(result)
```

Output

```
30
```

---

# 5. Inline Comments

Inline comments are written **after code on the same line**.

### Example

```python
x = 10  # initial value
y = 20  # second value

total = x + y  # calculate total

print(total)
```

Best practice:  
Use inline comments **sparingly** and keep them short.

Bad example:

```python
x = 10  # assigning x to 10 because I want the value to be 10 for the next calculation
```

Good example:

```python
x = 10  # initial score
```

---

# 6. Multi-Line Comments

Python **does not have official multi-line comment syntax**, but we simulate it using:

### Method 1 — Multiple `#`

```python
# This program calculates
# the area of a rectangle
# using length and width

length = 10
width = 5

area = length * width
print(area)
```

---

### Method 2 — Triple Quotes (Not technically comments)

```python
"""
This is a multi-line explanation.
Python ignores it if not assigned to a variable.
Used sometimes as multi-line comments.
"""
```

Example:

```python
"""
Program: Area calculator
Author: Tarra
Description: Calculates rectangle area
"""

length = 10
width = 5

print(length * width)
```

Note:

Triple quotes are **actually strings**, not real comments.

---

# 7. Docstrings (Documentation Comments)

Docstrings are used to **document functions, classes, and modules**.

They use triple quotes:

```
"""Docstring"""
```

or

```
'''Docstring'''
```

---

## Function Docstring Example

```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): first number
    b (int): second number
    
    Returns:
    int: sum of numbers
    """
    
    return a + b

print(add(5, 3))
```

Output

```
8
```

---

## Accessing Docstrings

Python stores docstrings in `__doc__`.

Example:

```python
def greet():
    """This function greets the user"""
    print("Hello!")

print(greet.__doc__)
```

Output

```
This function greets the user
```

---

# 8. Module-Level Comments

Used at the **top of a file** to explain the entire program.

Example:

```python
"""
File: calculator.py
Author: Tarra
Description:
Basic calculator operations implemented in Python.
"""

def add(a, b):
    return a + b
```

---

# 9. Class Docstrings

Used to document classes.

Example:

```python
class Car:
    """
    Represents a car object.
    
    Attributes:
    brand : str
    speed : int
    """

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
```

---

# 10. Commenting Out Code (Debugging)

Developers often disable code temporarily.

Example:

```python
x = 10
y = 20

# print("Debug value:", x)

print(x + y)
```

---

# 11. Best Practices for Comments

### 1 Write meaningful comments

Bad:

```python
x = x + 1  # increment
```

Good:

```python
x = x + 1  # increment user login attempts
```

---

### 2 Don't over-comment obvious code

Bad:

```python
# print hello
print("Hello")
```

---

### 3 Explain WHY not WHAT

Bad:

```python
# multiply a and b
result = a * b
```

Better:

```python
# calculate price after quantity multiplication
result = price * quantity
```

---

### 4 Keep comments updated

Wrong comments create confusion.

Bad:

```python
# calculate sum
result = a * b
```

---

# 12. Real-World Example

Example of good commenting in production code.

```python
"""
User authentication module
Handles login validation and password verification
"""

def validate_user(username, password):
    """
    Validates user credentials.
    
    Returns True if credentials are correct.
    """

    # fetch user data from database
    stored_password = "12345"

    # compare passwords
    if password == stored_password:
        return True

    return False
```

---

# 13. Interview Questions

### 1. What are comments in Python?

Non-executable lines used to explain code.

---

### 2. Which symbol is used for comments?

```
#
```

---

### 3. Does Python support multi-line comments?

Not officially. We simulate them using:

- multiple `#`
- triple quotes

---

### 4. What are docstrings?

Documentation strings used to describe functions, classes, and modules.

---

### 5. How to access docstrings?

Using:

```python
function.__doc__
```

---

# 14. Quick Summary

| Type | Syntax | Use |
|-----|------|-----|
| Single-line | `# comment` | General comments |
| Inline | `code  # comment` | Short explanation |
| Multi-line | multiple `#` | Long explanations |
| Docstring | `""" text """` | Documentation |

---

# 15. Practice Questions

Try writing comments for the following:

### Question 1

```python
x = 10
y = 20
print(x + y)
```

Add meaningful comments.

---

### Question 2

Write a function with a docstring.

---

### Question 3

Document a class using docstrings.

---

### Question 4

Create a module-level docstring for a calculator program.

---

# End of Notes