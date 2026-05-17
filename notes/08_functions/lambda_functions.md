# 🐍 Python Lambda Functions — Complete Notes

> **"Small but mighty — Lambda functions are Python's anonymous function powerhouse!"**

---

## 📌 Table of Contents

1. [What is a Lambda Function?](#what-is-a-lambda-function)
2. [Syntax](#syntax)
3. [Basic Examples](#basic-examples)
4. [Lambda vs Regular Function](#lambda-vs-regular-function)
5. [Lambda with Built-in Functions](#lambda-with-built-in-functions)
6. [Lambda with Conditionals](#lambda-with-conditionals)
7. [Lambda in Data Structures](#lambda-in-data-structures)
8. [Common Use Cases](#common-use-cases)
9. [Limitations](#limitations)
10. [Best Practices](#best-practices)
11. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## 🤔 What is a Lambda Function?

A **lambda function** is a small, **anonymous** (nameless) function defined using the `lambda` keyword.

- 📦 It can take **any number of arguments**
- ✅ But can only have **one expression** (single line)
- 🔄 It **returns** the result of the expression automatically (no `return` keyword needed)
- 🏷️ It has **no name** (anonymous) — but can be assigned to a variable

> 💡 **Think of it as:** A mini, throwaway function for quick tasks!

---

## 📐 Syntax

```python
lambda arguments : expression
```

| Part         | Description                              |
|--------------|------------------------------------------|
| `lambda`     | Keyword to define the function           |
| `arguments`  | One or more inputs (comma-separated)     |
| `:`          | Separator between arguments & expression |
| `expression` | Single operation that gets returned      |

---

## 🧪 Basic Examples

### ✅ No Arguments
```python
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!
```

### ✅ One Argument
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

### ✅ Two Arguments
```python
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10
```

### ✅ Three Arguments
```python
volume = lambda l, w, h: l * w * h
print(volume(2, 3, 4))  # Output: 24
```

### ✅ With Default Arguments
```python
power = lambda base, exp=2: base ** exp
print(power(3))     # Output: 9
print(power(3, 3))  # Output: 27
```

### ✅ With *args
```python
total = lambda *nums: sum(nums)
print(total(1, 2, 3, 4))  # Output: 10
```

---

## ⚖️ Lambda vs Regular Function

| Feature            | `def` Function          | `lambda` Function         |
|--------------------|-------------------------|---------------------------|
| Name               | Has a name              | Anonymous (no name)       |
| Lines              | Multiple lines          | Single expression only    |
| `return` keyword   | Required                | Implicit (auto-returned)  |
| Statements         | Supports all            | Only expressions          |
| Docstrings         | ✅ Supported            | ❌ Not supported           |
| Reusability        | High                    | Usually one-time use      |

### 🔁 Equivalent Functions

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

print(double(5))  # Both output: 10
```

---

## 🔧 Lambda with Built-in Functions

This is where lambdas **really shine** ✨ — they work perfectly with `map()`, `filter()`, and `sorted()`.

### 🗺️ `map()` — Apply function to every item

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25]

# Convert to uppercase
words = ["hello", "world"]
upper = list(map(lambda w: w.upper(), words))
print(upper)  # Output: ['HELLO', 'WORLD']
```

### 🔍 `filter()` — Keep items that pass a condition

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Keep only positive numbers
data = [-3, -1, 0, 2, 5, -7, 8]
positives = list(filter(lambda x: x > 0, data))
print(positives)  # Output: [2, 5, 8]
```

### 🔢 `sorted()` — Sort using a custom key

```python
# Sort by second character
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words, key=lambda w: w[1])
print(sorted_words)  # Output: ['date', 'cherry', 'banana', 'apple']

# Sort by string length
sorted_by_len = sorted(words, key=lambda w: len(w))
print(sorted_by_len)  # Output: ['date', 'apple', 'banana', 'cherry']
```

### ➕ `reduce()` — Accumulate a result (from `functools`)

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Maximum of all numbers
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 5
```

---

## 🔀 Lambda with Conditionals

Lambda supports **ternary (inline if-else)** expressions:

```python
# Syntax
lambda x: value_if_true if condition else value_if_false
```

```python
# Check even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))   # Output: Even
print(check(7))   # Output: Odd

# Absolute value
absolute = lambda x: x if x >= 0 else -x
print(absolute(-5))  # Output: 5

# Max of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Output: 20

# Grade classifier
grade = lambda score: "A" if score >= 90 else ("B" if score >= 80 else ("C" if score >= 70 else "F"))
print(grade(85))  # Output: B
```

---

## 📊 Lambda in Data Structures

### 📋 Sorting a List of Dictionaries

```python
students = [
    {"name": "Alice", "age": 22, "gpa": 3.8},
    {"name": "Bob",   "age": 20, "gpa": 3.5},
    {"name": "Carol", "age": 23, "gpa": 3.9},
]

# Sort by age
by_age = sorted(students, key=lambda s: s["age"])
print([s["name"] for s in by_age])  # ['Bob', 'Alice', 'Carol']

# Sort by GPA descending
by_gpa = sorted(students, key=lambda s: s["gpa"], reverse=True)
print([s["name"] for s in by_gpa])  # ['Carol', 'Alice', 'Bob']
```

### 📦 Sorting List of Tuples

```python
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]

# Sort by second element
sorted_pairs = sorted(pairs, key=lambda p: p[1])
print(sorted_pairs)  # [(3, 'a'), (1, 'b'), (2, 'c')]
```

### 🗂️ Lambda as Dictionary Values

```python
operations = {
    "add":      lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide":   lambda x, y: x / y if y != 0 else "Error",
}

print(operations["add"](5, 3))       # 8
print(operations["multiply"](4, 6))  # 24
print(operations["divide"](10, 0))   # Error
```

---

## 💼 Common Use Cases

### 🖊️ 1. Quick One-off Transformations
```python
# Convert Celsius to Fahrenheit
to_f = lambda c: (c * 9/5) + 32
print(to_f(100))  # 212.0
```

### 🧹 2. Data Cleaning
```python
names = ["  Alice ", "BOB  ", "  carol"]
clean = list(map(lambda n: n.strip().title(), names))
print(clean)  # ['Alice', 'Bob', 'Carol']
```

### 🎯 3. Callbacks / Event Handlers (GUI, APIs)
```python
# Simulating a button click callback
def on_click(callback):
    callback()

on_click(lambda: print("Button clicked! 🖱️"))
```

### 🔗 4. Immediately Invoked Lambda (IIFE)
```python
# Define and call in one line
result = (lambda x, y: x + y)(10, 20)
print(result)  # 30
```

### 📈 5. Sorting Complex Data
```python
employees = [("Alice", 50000), ("Bob", 75000), ("Carol", 60000)]
top_earners = sorted(employees, key=lambda e: e[1], reverse=True)
print(top_earners)
# [('Bob', 75000), ('Carol', 60000), ('Alice', 50000)]
```

---

## ⚠️ Limitations

| ❌ Limitation                          | 📝 Explanation                                             |
|----------------------------------------|------------------------------------------------------------|
| Single expression only                 | Cannot contain `if/elif/else` blocks, loops, or statements |
| No `return` keyword                    | Expression is always implicitly returned                   |
| No docstrings                          | Cannot document a lambda                                   |
| No multi-line logic                    | Cannot span multiple lines                                 |
| Harder to debug                        | No function name in tracebacks                             |
| Can't use `assert`, `try/except`, etc. | Only expressions allowed, not statements                   |

### 🚫 Things you CANNOT do in Lambda:

```python
# ❌ Multiple statements
bad = lambda x: x = x + 1; return x  # SyntaxError

# ❌ While/for loops
bad = lambda x: for i in range(x): print(i)  # SyntaxError

# ❌ try/except
bad = lambda x: try: int(x) except: "error"  # SyntaxError
```

---

## ✅ Best Practices

### 👍 DO:
```python
# ✅ Use lambda for short, simple operations
square = lambda x: x ** 2

# ✅ Use lambda with map/filter/sorted
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# ✅ Use lambda as a quick key for sorting
data.sort(key=lambda item: item["score"])
```

### 👎 DON'T:
```python
# ❌ Don't use lambda for complex logic — use def instead
# Bad
compute = lambda x: x**2 if x > 0 else (-x)**2 if x < -10 else 0

# Better
def compute(x):
    if x > 0:
        return x ** 2
    elif x < -10:
        return (-x) ** 2
    return 0

# ❌ Don't assign lambda to a variable just to reuse it — use def
# Bad (PEP 8 discourages this)
double = lambda x: x * 2

# Better
def double(x):
    return x * 2
```

> 💡 **PEP 8 Tip:** If you need to assign a lambda to a variable, use `def` instead — it's more readable and Pythonic!

---

## 📋 Quick Reference Cheat Sheet

```python
# ── BASIC ──────────────────────────────────────────────────────
lambda: "hello"                        # No args
lambda x: x * 2                        # One arg
lambda x, y: x + y                     # Two args
lambda x, y=10: x + y                  # Default arg
lambda *args: sum(args)                 # Variable args

# ── CONDITIONAL ───────────────────────────────────────────────
lambda x: "yes" if x > 0 else "no"    # Ternary

# ── WITH BUILT-INS ────────────────────────────────────────────
map(lambda x: x**2, iterable)          # Transform
filter(lambda x: x > 0, iterable)     # Filter
sorted(iterable, key=lambda x: x[1])  # Sort by key
reduce(lambda x, y: x+y, iterable)    # Accumulate

# ── IMMEDIATELY INVOKED ───────────────────────────────────────
(lambda x: x * 3)(5)                   # Returns 15
```

---

## 🧠 Memory Tip

```
L — Lambda is lightweight
A — Anonymous (no name)
M — Makes code concise
B — Best with map/filter/sorted
D — Don't overuse it — readability matters!
A — Always returns one expression
```
