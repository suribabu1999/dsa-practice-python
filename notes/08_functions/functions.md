# 🐍 Python Functions — Zero to Hero
## Docstrings · Recursion · Lambda · Every Function Type · Advanced Mastery

> 🧠 **What is a Function?**
> A function is a **named, reusable block of code** that does ONE job.
> Think of it like a **coffee machine** ☕:
> - You don't rebuild it every time you want coffee
> - You press a button (call the function)
> - It does its job and gives you the result
> - You can use it **again and again**
>
> Without functions → copy-paste spaghetti 🍝
> With functions    → clean, reusable, testable code 🏗️

```python
# The cost of NOT using functions:
print("Hello, Alice!")     # 😩 copy
print("Hello, Bob!")       # 😩 paste
print("Hello, Charlie!")   # 😩 paste again

# The power of functions:
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # 😎 clean
greet("Bob")      # 😎 reusable
greet("Charlie")  # 😎 one place to change
```

---

## 📚 Table of Contents

1. [Defining & Calling Functions](#-defining--calling-functions)
2. [Parameters & Arguments — Every Type](#-parameters--arguments--every-type)
3. [Return Values](#-return-values)
4. [Docstrings — Complete Guide](#-docstrings--complete-guide)
5. [Lambda Functions](#-lambda-functions)
6. [Recursive Functions](#-recursive-functions)
7. [Higher-Order Functions](#-higher-order-functions)
8. [Nested Functions & Closures](#-nested-functions--closures)
9. [Decorators](#-decorators)
10. [Generator Functions](#-generator-functions)
11. [Variable Scope — LEGB Rule](#-variable-scope--legb-rule)
12. [Function Annotations & Type Hints](#-function-annotations--type-hints)
13. [Special Functions — __dunder__](#-special-functions--dunder)
14. [functools Module](#-functools-module)
15. [Real-World Projects](#-real-world-projects)
16. [Common Mistakes](#-common-mistakes)
17. [Cheat Sheet](#-cheat-sheet)

---

## 🏗️ Defining & Calling Functions

```python
# Anatomy of a function:
#
#   def   name   (parameters)  :
#   ↑      ↑          ↑         ↑
# keyword  name   inputs     colon
#
#       body (indented 4 spaces)
#       return value  (optional)
```

```python
# ─── Simplest possible function ───
def say_hello():
    print("Hello, World! 👋")

say_hello()     # Call it — MUST have ()
say_hello()     # Call it again — reusable!
say_hello()     # And again!
```

```python
# ─── Function is an OBJECT ───
def greet():
    print("Hi!")

print(type(greet))    # <class 'function'>
print(greet)          # <function greet at 0x...>
# greet   → the function object itself (no call)
# greet() → actually CALLS and runs it
```

```python
# ─── Functions must be DEFINED before CALLED ───

# ❌ This crashes:
say_hi()           # NameError — not defined yet!
def say_hi():
    print("Hi!")

# ✅ This works:
def say_hi():
    print("Hi!")
say_hi()           # defined first, called after ✅
```

```python
# ─── Empty function — use pass ───
def placeholder():
    pass    # "I'll implement this later"

def todo():
    ...     # Ellipsis also works as a placeholder!
```

---

## 🎛️ Parameters & Arguments — Every Type

> **Parameter** = variable in the function DEFINITION 📝
> **Argument**  = actual value you PASS when calling  📦

```python
#           parameter ↓↓↓↓
def greet(  name  ):
    print(f"Hello, {name}!")
#                argument ↓↓↓↓↓
greet(          "Alice"   )
```

---

### Type 1 — Positional Parameters

```python
# Order matters — arguments match by POSITION
def introduce(name, age, city):
    print(f"👤 {name}, {age} years old, from {city}")

introduce("Alice", 25, "Mumbai")    # ✅ correct order
# introduce(25, "Alice", "Mumbai")  # 😱 wrong — age goes to name!
```

---

### Type 2 — Keyword Arguments

```python
# Pass by NAME — order doesn't matter!
def introduce(name, age, city):
    print(f"👤 {name}, {age}, {city}")

introduce(age=25, city="Mumbai", name="Alice")   # ✅ any order!
introduce("Alice", city="Mumbai", age=25)        # ✅ mix positional+keyword
```

---

### Type 3 — Default Parameters

```python
# Give a parameter a DEFAULT value — makes it optional
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                         # Hello, Alice!
greet("Bob", "Hey")                    # Hey, Bob!
greet("Charlie", "Howdy", ".")         # Howdy, Charlie.
greet("Diana", punctuation="!!!")      # Hello, Diana!!!

# ⚠️ Rule: defaults must come AFTER non-defaults
# def bad(x=1, y):   ← SyntaxError!
# def good(y, x=1):  ← ✅
```

```python
# ⚠️ Mutable default argument BUG (very common mistake!)

# ❌ WRONG — list is shared across ALL calls!
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['a', 'b']  ← UNEXPECTED!
print(add_item("c"))    # ['a', 'b', 'c']  ← BUG!

# ✅ CORRECT — use None as default
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['b']    ← fresh list each time ✅
```

---

### Type 4 — *args (Variable Positional)

```python
# *args collects ALL extra positional arguments into a TUPLE
def add_all(*numbers):
    print(f"Received: {numbers}")   # it's a tuple!
    return sum(numbers)

add_all(1, 2)              # Received: (1, 2)        → 3
add_all(1, 2, 3, 4, 5)    # Received: (1, 2, 3, 4, 5) → 15
add_all(10)               # Received: (10,)           → 10
add_all()                 # Received: ()              → 0
```

```python
# ─── *args with required parameters ───
def log(level, *messages):
    for msg in messages:
        print(f"[{level}] {msg}")

log("INFO", "Server started")
log("ERROR", "Connection failed", "Retrying...", "Attempt 3")
# [INFO] Server started
# [ERROR] Connection failed
# [ERROR] Retrying...
# [ERROR] Attempt 3
```

```python
# ─── Unpacking into *args with * operator ───
def add(a, b, c):
    return a + b + c

nums   = [1, 2, 3]
result = add(*nums)      # unpacks → add(1, 2, 3)
print(result)   # 6

coords = (10, 20, 30)
result = add(*coords)
print(result)   # 60
```

---

### Type 5 — **kwargs (Variable Keyword)

```python
# **kwargs collects ALL extra keyword arguments into a DICT
def describe(**info):
    print(f"Received: {info}")   # it's a dict!
    for key, val in info.items():
        print(f"  {key}: {val}")

describe(name="Alice", age=25, city="Mumbai")
# Received: {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
#   name: Alice
#   age: 25
#   city: Mumbai
```

```python
# ─── **kwargs with required parameters ───
def create_user(username, **options):
    user = {"username": username}
    user.update(options)
    return user

u1 = create_user("alice")
u2 = create_user("bob", email="bob@x.com", role="admin", active=True)
print(u1)   # {'username': 'alice'}
print(u2)   # {'username': 'bob', 'email': 'bob@x.com', 'role': 'admin', 'active': True}
```

```python
# ─── Unpacking dict into **kwargs ───
def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")

options = {"greeting": "Hey", "punctuation": "!!!"}
greet("Alice", **options)    # → greet("Alice", greeting="Hey", punctuation="!!!")
# Hey, Alice!!!
```

---

### Type 6 — Positional-Only Parameters (Python 3.8+)

```python
# Parameters before / are positional-only (cannot use keyword syntax)
def add(x, y, /):
    return x + y

add(3, 5)         # ✅ positional
# add(x=3, y=5)  # ❌ TypeError — x and y are positional-only
```

---

### Type 7 — Keyword-Only Parameters

```python
# Parameters after * must be passed as keywords
def create(name, *, verbose=False, debug=False):
    if verbose: print(f"Creating {name}...")
    if debug:   print(f"Debug mode ON")
    return name

create("Alice")                          # ✅
create("Bob", verbose=True)              # ✅
# create("Charlie", True)               # ❌ TypeError
```

---

### The Complete Signature Order

```python
# Correct order of ALL parameter types:
# normal → *args → keyword-only → **kwargs

def everything(
    pos1, pos2,          # positional (required)
    /,                   # positional-ONLY before this
    normal,              # regular (positional or keyword)
    *args,               # extra positional → tuple
    kw_only,             # keyword-ONLY (after *)
    kw_default="hi",     # keyword-only with default
    **kwargs             # extra keyword → dict
):
    print(pos1, pos2, normal, args, kw_only, kw_default, kwargs)

everything(1, 2, 3, 4, 5, kw_only="must", extra="bonus")
# 1  2  3  (4, 5)  must  hi  {'extra': 'bonus'}
```

---

## 🎁 Return Values

```python
# return sends a value BACK to the caller
# return also EXITS the function immediately

def add(a, b):
    return a + b

result = add(3, 5)    # result = 8
print(result)         # 8
print(add(10, 20))    # 30  — use directly
print(add(2,3) * 4)   # 20  — use in expression
```

```python
# ─── No return = returns None ───
def say_hi():
    print("Hi!")

result = say_hi()
print(result)    # None

# ─── Bare return = returns None ───
def early_exit(x):
    if x < 0:
        return       # exit early, return None
    return x * 2

print(early_exit(-1))    # None
print(early_exit(5))     # 10
```

```python
# ─── Multiple return values (actually a tuple!) ───
def min_max_avg(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

lo, hi, avg = min_max_avg([3,1,4,1,5,9,2,6])
print(f"Min={lo}  Max={hi}  Avg={avg:.2f}")
# Min=1  Max=9  Avg=3.88
```

```python
# ─── Return different types based on condition ───
def safe_divide(a, b):
    if b == 0:
        return None   # signal failure
    return a / b

result = safe_divide(10, 2)
if result is not None:
    print(f"Result: {result}")   # 5.0

# ─── Return dict for named results ───
def analyze(data):
    return {
        "count"  : len(data),
        "total"  : sum(data),
        "mean"   : sum(data)/len(data),
        "minimum": min(data),
        "maximum": max(data),
    }

stats = analyze([4, 7, 2, 9, 1, 6])
print(f"Mean: {stats['mean']:.1f}  Range: {stats['minimum']}-{stats['maximum']}")
```

---

---

## 📖 Docstrings — Complete Guide

> A **docstring** is a string literal as the FIRST statement of a function.
> It's the function's **official documentation** — describes what it does,
> what it takes, and what it returns.

```python
def function_name(params):
    """This is the docstring — it goes RIGHT after def, before code."""
    # actual code here
```

---

### Style 1 — One-line Docstring

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def greet(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}!")
```

> 💡 Rules for one-liners:
> - Fits on a single line
> - Opening and closing `"""` on the same line
> - Ends with a period
> - Describes WHAT it does, not HOW

---

### Style 2 — Google Style Docstring ⭐ (Most Popular)

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms. Must be positive.
        height_m  (float): Height in meters. Must be positive.

    Returns:
        float: The BMI value rounded to 2 decimal places.

    Raises:
        ValueError: If weight or height is non-positive.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
        >>> calculate_bmi(50, 1.60)
        19.53
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return round(weight_kg / height_m**2, 2)
```

---

### Style 3 — NumPy Style Docstring

```python
def linear_regression(x, y):
    """
    Compute simple linear regression coefficients.

    Parameters
    ----------
    x : list of float
        Independent variable values.
    y : list of float
        Dependent variable values. Must be same length as x.

    Returns
    -------
    slope : float
        The slope of the regression line.
    intercept : float
        The y-intercept of the regression line.

    Notes
    -----
    Uses the least-squares method.

    Examples
    --------
    >>> slope, intercept = linear_regression([1,2,3], [2,4,6])
    >>> slope
    2.0
    >>> intercept
    0.0
    """
    n     = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    slope  = sum((xi-mean_x)*(yi-mean_y) for xi,yi in zip(x,y)) / \
             sum((xi-mean_x)**2 for xi in x)
    return slope, mean_y - slope * mean_x
```

---

### Style 4 — reStructuredText (reST) Style

```python
def send_email(to, subject, body, cc=None):
    """
    Send an email message.

    :param to:      Recipient email address.
    :type  to:      str
    :param subject: Email subject line.
    :type  subject: str
    :param body:    Email body content.
    :type  body:    str
    :param cc:      Carbon-copy addresses (optional).
    :type  cc:      list[str], optional
    :returns:       True if sent successfully.
    :rtype:         bool
    :raises:        ConnectionError if mail server unreachable.

    Example::

        send_email("alice@example.com", "Hello", "Hi Alice!")
    """
    pass
```

---

### Accessing Docstrings

```python
def greet(name):
    """Print a warm greeting to the given name."""
    print(f"Hello, {name}!")

# Access the docstring:
print(greet.__doc__)
# "Print a warm greeting to the given name."

# Pretty-printed with help():
help(greet)
# Help on function greet in module __main__:
# greet(name)
#     Print a warm greeting to the given name.
```

---

### Docstring for Classes and Modules

```python
"""
math_utils.py — Mathematical utility functions.

This module provides helper functions for common
mathematical operations used throughout the project.

Author: Alice
Version: 1.0.0
"""

class Calculator:
    """
    A simple calculator with memory.

    Supports basic arithmetic and stores the last result
    in memory for chained operations.

    Attributes:
        memory (float): The stored value in memory.

    Example:
        >>> calc = Calculator()
        >>> calc.add(5, 3)
        8
    """

    def __init__(self):
        """Initialize the calculator with memory set to 0."""
        self.memory = 0

    def add(self, a, b):
        """
        Add two numbers and store the result in memory.

        Args:
            a (float): First number.
            b (float): Second number.

        Returns:
            float: The sum of a and b.
        """
        self.memory = a + b
        return self.memory
```

---

### Doctest — Runnable Examples in Docstrings!

```python
def factorial(n):
    """
    Return n! (n factorial).

    Args:
        n (int): Non-negative integer.

    Returns:
        int: The factorial of n.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: n must be non-negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Run doctests:
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

---

---

## ⚡ Lambda Functions

> A **lambda** is an anonymous, one-expression function.
> Think of it as a **disposable mini-function** — write and use in place!

```python
# Regular function:
def square(x):
    return x**2

# Lambda equivalent:
square = lambda x: x**2

# Anatomy:
# lambda  parameters : expression
#   ↑         ↑            ↑
# keyword   inputs    what to return (implicit!)
```

```python
# ─── Basic lambdas ───
double     = lambda x: x * 2
add        = lambda x, y: x + y
greet      = lambda name: f"Hello, {name}!"
is_even    = lambda n: n % 2 == 0
clamp      = lambda x, lo, hi: max(lo, min(hi, x))
first_char = lambda s: s[0] if s else ""

print(double(5))           # 10
print(add(3, 4))           # 7
print(greet("Alice"))      # Hello, Alice!
print(is_even(7))          # False
print(clamp(15, 0, 10))    # 10
print(first_char("hello")) # h
```

---

### Lambda with sorted()

```python
# sorted(iterable, key=lambda) — sort by custom rule

words    = ["banana", "apple", "cherry", "kiwi", "mango"]

# Sort by length
by_len   = sorted(words, key=lambda w: len(w))
print(by_len)    # ['kiwi', 'apple', 'mango', 'banana', 'cherry']

# Sort by last character
by_last  = sorted(words, key=lambda w: w[-1])
print(by_last)   # ['banana', 'apple', 'mango', 'kiwi', 'cherry']

# Sort by length then alphabetically (tuple key!)
by_both  = sorted(words, key=lambda w: (len(w), w))
print(by_both)   # ['kiwi', 'apple', 'mango', 'banana', 'cherry']

# Sort list of dicts
students = [
    {"name": "Charlie", "score": 85, "age": 21},
    {"name": "Alice",   "score": 92, "age": 20},
    {"name": "Bob",     "score": 85, "age": 22},
]

# By score descending, then name ascending
ranked = sorted(students, key=lambda s: (-s["score"], s["name"]))
for s in ranked:
    print(f"  {s['name']:<10} {s['score']}")
# Alice      92
# Bob        85    ← Bob before Charlie alphabetically
# Charlie    85
```

---

### Lambda with map()

```python
# map(function, iterable) — apply function to every item

nums = [1, 2, 3, 4, 5]

# Double each
doubled   = list(map(lambda x: x * 2,    nums))
# Square each
squares   = list(map(lambda x: x**2,     nums))
# Convert to string
strings   = list(map(lambda x: f"#{x}",  nums))

print(doubled)   # [2, 4, 6, 8, 10]
print(squares)   # [1, 4, 9, 16, 25]
print(strings)   # ['#1', '#2', '#3', '#4', '#5']

# Map with two iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)      # [11, 22, 33]
```

---

### Lambda with filter()

```python
# filter(function, iterable) — keep items where function returns True

nums   = [1, -3, 4, -2, 0, 7, -1, 5, -6]

pos    = list(filter(lambda x: x > 0,        nums))
evens  = list(filter(lambda x: x % 2 == 0,   nums))
big    = list(filter(lambda x: abs(x) > 3,   nums))

print(pos)    # [4, 7, 5]
print(evens)  # [4, -2, 0, -6]
print(big)    # [4, 7, 5, -6]

# Filter strings
words  = ["python", "", "rocks", " ", "!!", "cool"]
valid  = list(filter(lambda w: w.strip() and w.isalpha(), words))
print(valid)  # ['python', 'rocks', 'cool']
```

---

### Lambda with reduce()

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# Sum (fold left: ((((1+2)+3)+4)+5))
total   = reduce(lambda acc, x: acc + x,  nums)
product = reduce(lambda acc, x: acc * x,  nums)
maximum = reduce(lambda a, b: a if a>b else b, nums)

print(total)    # 15
print(product)  # 120
print(maximum)  # 5

# Concatenate strings
words   = ["Python", "is", "awesome"]
sentence = reduce(lambda a, b: a + " " + b, words)
print(sentence)   # Python is awesome

# Flatten list of lists
nested  = [[1,2],[3,4],[5,6]]
flat    = reduce(lambda a, b: a + b, nested)
print(flat)       # [1, 2, 3, 4, 5, 6]
```

---

### Immediately Invoked Lambda (IIFE)

```python
# Define and call in one line!
result = (lambda x, y: x**2 + y**2)(3, 4)
print(result)    # 25

# Useful for quick one-off calculations
area = (lambda r: 3.14159 * r**2)(5)
print(f"Area: {area:.2f}")   # 78.54
```

---

### Lambda Limitations

```python
# ❌ Lambda can only have ONE expression — no statements!
# No assignments, no if-elif-else (multi-line), no loops, no try-except

# ❌ Cannot:
f = lambda x: x = x + 1      # SyntaxError — assignment!
f = lambda x: print(x); x+1  # only first expression

# ✅ Can use ternary:
f = lambda x: x+1 if x>0 else -x   # OK!

# ✅ Can call other functions:
f = lambda s: s.strip().upper()     # OK!

# ─── Lambda vs def — when to use which ───
# Use lambda: sort keys, map/filter/reduce, short callbacks, one-liners
# Use def:    anything longer than one expression, needs docstring, reused a lot
```

---

---

## 🔄 Recursive Functions

> A **recursive function** is one that **calls itself**.
> Every recursion MUST have:
> 1. ✅ **Base case** — the condition that STOPS recursion
> 2. ✅ **Recursive case** — the call to itself, moving TOWARD the base case

```python
# Structure of every recursive function:
def recursive(input):
    if base_condition:    # ← MUST exist!
        return base_value # ← stop here
    return recursive(smaller_input)  # ← move toward base
```

---

### Example 1 — Factorial n!

```python
# n! = n × (n-1) × (n-2) × ... × 1
# 5! = 5 × 4! = 5 × 4 × 3! = 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):
    """
    Return n factorial recursively.

    Args:
        n (int): Non-negative integer.

    Returns:
        int: n!

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Call stack visualization:
# factorial(5)
#   → 5 * factorial(4)
#         → 4 * factorial(3)
#               → 3 * factorial(2)
#                     → 2 * factorial(1)
#                           → 1  ← base case!
#                     → 2 * 1 = 2
#               → 3 * 2 = 6
#         → 4 * 6 = 24
#   → 5 * 24 = 120

print(factorial(5))    # 120
print(factorial(10))   # 3628800
```

---

### Example 2 — Fibonacci Sequence

```python
# F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)

def fibonacci(n):
    """
    Return the nth Fibonacci number.

    Args:
        n (int): Index (0-based). Must be >= 0.

    Returns:
        int: The nth Fibonacci number.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(10)
        55
    """
    if n <= 0: return 0       # base case 1
    if n == 1: return 1       # base case 2
    return fibonacci(n-1) + fibonacci(n-2)   # recursive

# Sequence: 0 1 1 2 3 5 8 13 21 34 55 ...
for i in range(12):
    print(f"  F({i:2}) = {fibonacci(i)}")
```

```python
# ⚠️ Naive recursion is SLOW for large n — it recalculates!
# fibonacci(30) makes 2.7 MILLION function calls!

# ✅ Fix with memoization:
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    """Memoized Fibonacci — fast!"""
    if n <= 1: return n
    return fib_fast(n-1) + fib_fast(n-2)

print(fib_fast(100))   # 354224848179261915075  — instant!
```

---

### Example 3 — Sum of List

```python
def sum_list(nums):
    """
    Recursively sum all elements of a list.

    Args:
        nums (list): List of numbers.

    Returns:
        int/float: The total sum.

    Examples:
        >>> sum_list([])
        0
        >>> sum_list([1,2,3,4,5])
        15
    """
    if not nums:                  # base: empty list
        return 0
    return nums[0] + sum_list(nums[1:])   # first + rest

print(sum_list([1,2,3,4,5]))     # 15
print(sum_list([]))              # 0
```

---

### Example 4 — Power Function

```python
def power(base, exp):
    """
    Compute base raised to exp recursively.

    Args:
        base (float): The base number.
        exp  (int):   The exponent (non-negative integer).

    Returns:
        float: base ** exp

    Examples:
        >>> power(2, 10)
        1024
        >>> power(3, 0)
        1
    """
    if exp == 0:            # any number^0 = 1
        return 1
    if exp % 2 == 0:        # even exponent — fast path!
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)

print(power(2, 10))    # 1024
print(power(3, 5))     # 243
```

---

### Example 5 — Binary Search

```python
def binary_search(arr, target, low=0, high=None):
    """
    Recursively search for target in a sorted array.

    Args:
        arr    (list): Sorted list to search.
        target: The value to find.
        low    (int):  Left boundary index.
        high   (int):  Right boundary index.

    Returns:
        int: Index of target, or -1 if not found.

    Examples:
        >>> binary_search([1,3,5,7,9,11], 7)
        3
        >>> binary_search([1,3,5,7,9,11], 4)
        -1
    """
    if high is None:
        high = len(arr) - 1

    if low > high:          # base case: not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:  # base case: found!
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)

data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(data, 7))    # 3
print(binary_search(data, 6))    # -1
```

---

### Example 6 — Flatten Nested List

```python
def flatten(nested):
    """
    Recursively flatten a deeply nested list.

    Args:
        nested (list): A potentially nested list of any depth.

    Returns:
        list: A flat list of all items.

    Examples:
        >>> flatten([1, [2, [3, [4]], 5]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))    # recurse into sub-list
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, [4, [5]]]]]))
# [1, 2, 3, 4, 5]
print(flatten([[1,2],[3,[4,5]],[[[6]]]]))
# [1, 2, 3, 4, 5, 6]
```

---

### Example 7 — Tower of Hanoi

```python
def hanoi(n, source="A", target="C", auxiliary="B"):
    """
    Solve Tower of Hanoi for n disks.

    Args:
        n         (int): Number of disks.
        source    (str): Starting peg name.
        target    (str): Destination peg name.
        auxiliary (str): Helper peg name.

    Returns:
        int: Number of moves made.

    Examples:
        >>> hanoi(2)
        Move disk 1: A → B
        Move disk 2: A → C
        Move disk 1: B → C
        3
    """
    if n == 1:
        print(f"  Move disk 1: {source} → {target}")
        return 1
    moves  = hanoi(n-1, source, auxiliary, target)
    print(f"  Move disk {n}: {source} → {target}")
    moves += 1
    moves += hanoi(n-1, auxiliary, target, source)
    return moves

total = hanoi(3)
print(f"  Total moves: {total}")   # 7 moves for 3 disks
```

---

### Example 8 — Merge Sort

```python
def merge_sort(arr):
    """
    Sort a list using recursive merge sort.

    Args:
        arr (list): List of comparable items.

    Returns:
        list: A new sorted list.

    Examples:
        >>> merge_sort([5, 2, 8, 1, 9, 3])
        [1, 2, 3, 5, 8, 9]
    """
    if len(arr) <= 1:       # base case
        return arr

    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])    # sort left half
    right = merge_sort(arr[mid:])    # sort right half

    return merge(left, right)

def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j  = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(merge_sort(data))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

### Example 9 — Directory Tree (Real-world!)

```python
import os

def print_tree(path, prefix="", is_last=True):
    """
    Recursively print a directory tree structure.

    Args:
        path    (str): Directory or file path.
        prefix  (str): Visual prefix string (for indentation).
        is_last (bool): Whether this is the last item in its directory.

    Example output:
        📁 project/
        ├── 📄 main.py
        ├── 📁 utils/
        │   ├── 📄 helpers.py
        │   └── 📄 config.py
        └── 📄 README.md
    """
    connector = "└── " if is_last else "├── "
    icon      = "📁 " if os.path.isdir(path) else "📄 "
    name      = os.path.basename(path)

    print(prefix + connector + icon + name)

    if os.path.isdir(path):
        children = sorted(os.listdir(path))
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            new_prefix    = prefix + ("    " if is_last else "│   ")
            print_tree(os.path.join(path, child), new_prefix, is_last_child)
```

---

### Recursion vs Iteration

```python
# Same problem — two approaches:

# ─── Factorial iteratively ───
def factorial_iter(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# ─── Factorial recursively ───
def factorial_rec(n):
    return 1 if n <= 1 else n * factorial_rec(n-1)

# When to choose:
# Recursion  → naturally recursive problems (trees, graphs, divide-and-conquer)
# Iteration  → simple loops, better performance, no stack overflow risk

# ─── Recursion limit ───
import sys
print(sys.getrecursionlimit())    # 1000 (default)
sys.setrecursionlimit(5000)       # increase if needed

# ─── Tail recursion optimization (manual) ───
# Python doesn't optimize tail calls, so convert deep recursions to iteration
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n-1, n * accumulator)
```

---

---

## 🏆 Higher-Order Functions

> A **higher-order function** is one that:
> - Takes a **function as an argument**, OR
> - **Returns a function**

---

### Functions as Arguments

```python
def apply(func, value):
    """Apply func to value and return the result."""
    return func(value)

def square(x):   return x**2
def double(x):   return x*2
def negate(x):   return -x

print(apply(square, 5))     # 25
print(apply(double, 5))     # 10
print(apply(negate, 5))     # -5
print(apply(abs, -42))      # 42  — built-in function too!
```

```python
# ─── Custom map / filter / reduce ───
def my_map(func, lst):
    """Apply func to every element, return new list."""
    return [func(x) for x in lst]

def my_filter(func, lst):
    """Keep elements where func returns True."""
    return [x for x in lst if func(x)]

def my_reduce(func, lst, initial=None):
    """Fold list into a single value using func."""
    result = initial if initial is not None else lst[0]
    start  = 0 if initial is not None else 1
    for item in lst[start:]:
        result = func(result, item)
    return result

nums = [1, 2, 3, 4, 5]
print(my_map(lambda x: x**2, nums))          # [1,4,9,16,25]
print(my_filter(lambda x: x%2==0, nums))     # [2,4]
print(my_reduce(lambda a,b: a+b, nums))      # 15
```

---

### Functions as Return Values

```python
def make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(x):
        return x * factor    # 'factor' is captured in closure!
    return multiply

double  = make_multiplier(2)
triple  = make_multiplier(3)
times10 = make_multiplier(10)

print(double(5))    # 10
print(triple(5))    # 15
print(times10(7))   # 70
```

```python
def make_validator(min_val, max_val):
    """Return a validator function for a given range."""
    def validate(value):
        if not (min_val <= value <= max_val):
            raise ValueError(f"{value} not in [{min_val}, {max_val}]")
        return True
    return validate

check_age    = make_validator(0, 150)
check_score  = make_validator(0, 100)
check_rating = make_validator(1, 5)

print(check_age(25))     # True
print(check_score(87))   # True
# check_rating(6)        # ValueError: 6 not in [1, 5]
```

```python
# ─── Function pipeline ───
def pipeline(*functions):
    """Create a function that applies functions left to right."""
    def apply(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return apply

process = pipeline(
    str.strip,
    str.lower,
    str.title,
    lambda s: f"Name: {s}"
)

print(process("  ALICE SMITH  "))   # Name: Alice Smith
print(process("  BOB JONES  "))     # Name: Bob Jones
```

---

---

## 🪆 Nested Functions & Closures

> A **nested function** is defined INSIDE another function.
> A **closure** is a nested function that **remembers** variables
> from its enclosing scope — even after the outer function has returned!

```python
def outer():
    message = "Hello from outer! 🌍"   # outer variable

    def inner():
        print(message)   # inner can SEE outer's variables!

    inner()   # call inner from within outer

outer()
# Hello from outer! 🌍
```

```python
# ─── Classic closure — counter ───
def make_counter(start=0, step=1):
    """
    Create a counter that remembers its state.

    Returns:
        function: A function that returns the next count each call.
    """
    count = [start]   # use list to allow mutation in closure

    def counter():
        value     = count[0]
        count[0] += step
        return value

    return counter

count_by_1 = make_counter()
count_by_2 = make_counter(step=2)
count_from_10 = make_counter(start=10)

print(count_by_1())    # 0
print(count_by_1())    # 1
print(count_by_1())    # 2
print(count_by_2())    # 0
print(count_by_2())    # 2
print(count_from_10()) # 10
```

```python
# ─── Closure for data privacy ───
def make_account(owner, initial_balance=0):
    """
    Create a bank account closure.

    Args:
        owner           (str): Account owner's name.
        initial_balance (float): Starting balance.

    Returns:
        dict: A dict of functions (deposit, withdraw, balance).
    """
    balance = [initial_balance]   # private — inaccessible from outside

    def deposit(amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        balance[0] += amount
        print(f"  ✅ Deposited ₹{amount:,}  |  Balance: ₹{balance[0]:,}")

    def withdraw(amount):
        if amount > balance[0]:
            print(f"  ❌ Insufficient funds (balance: ₹{balance[0]:,})")
            return False
        balance[0] -= amount
        print(f"  ✅ Withdrew ₹{amount:,}   |  Balance: ₹{balance[0]:,}")
        return True

    def get_balance():
        return balance[0]

    print(f"  🏦 Account created for {owner}")
    return {"deposit": deposit, "withdraw": withdraw, "balance": get_balance}

acc = make_account("Alice", 10000)
acc["deposit"](5000)      # ✅ Deposited ₹5,000  |  Balance: ₹15,000
acc["withdraw"](3000)     # ✅ Withdrew  ₹3,000  |  Balance: ₹12,000
acc["withdraw"](20000)    # ❌ Insufficient funds
print(acc["balance"]())   # 12000
# balance is completely private — can't access directly!
```

```python
# ─── nonlocal keyword — modify outer variable ───
def make_counter_v2():
    count = 0          # outer variable

    def increment():
        nonlocal count   # ← tell Python: "I mean the OUTER count"
        count += 1
        return count

    def reset():
        nonlocal count
        count = 0

    return increment, reset

inc, rst = make_counter_v2()
print(inc())   # 1
print(inc())   # 2
print(inc())   # 3
rst()
print(inc())   # 1  ← reset worked!
```

---

---

## 🎀 Decorators

> A **decorator** is a function that **wraps another function**
> to add behavior before and/or after, without modifying the original.

```python
# Basic decorator structure:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # code BEFORE
        result = func(*args, **kwargs)   # call original
        # code AFTER
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

# @my_decorator is exactly same as:
# greet = my_decorator(greet)
```

---

### Decorator 1 — Timer

```python
import time
import functools

def timer(func):
    """Measure and print how long a function takes to run."""
    @functools.wraps(func)   # preserves original function's metadata
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"  ⏱️  {func.__name__}() took {(end-start)*1000:.2f}ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum numbers from 0 to n."""
    return sum(range(n))

print(slow_sum(10_000_000))
# ⏱️  slow_sum() took 312.45ms
# 49999995000000
```

---

### Decorator 2 — Logger

```python
def logger(func):
    """Log every call with arguments and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kw_str   = ", ".join(f"{k}={v!r}" for k,v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kw_str]))
        print(f"  📋 CALL: {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"  📋 RETURN: {result!r}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("Alice", greeting="Hi")
# 📋 CALL: add(3, 5)
# 📋 RETURN: 8
# 📋 CALL: greet('Alice', greeting='Hi')
# 📋 RETURN: 'Hi, Alice!'
```

---

### Decorator 3 — Retry

```python
import random

def retry(max_attempts=3, delay=1.0):
    """Retry a function up to max_attempts times on failure."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"  ⚠️  Attempt {attempt} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unreliable_api_call():
    """Simulate an API call that sometimes fails."""
    if random.random() < 0.7:
        raise ConnectionError("Server unavailable")
    return {"status": "success", "data": [1,2,3]}
```

---

### Decorator 4 — Cache / Memoize

```python
def memoize(func):
    """Cache function results to avoid repeated computation."""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_fib(n):
    """Fibonacci without memoize would be VERY slow for large n."""
    if n <= 1: return n
    return expensive_fib(n-1) + expensive_fib(n-2)

print(expensive_fib(50))    # 12586269025 — instant!

# Python's built-in cache decorator (better!):
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

---

### Stacking Decorators

```python
# Decorators apply BOTTOM UP:
@timer
@logger
def add(a, b):
    return a + b

# Equivalent to: add = timer(logger(add))
# Logger runs first (inner), then timer wraps around it
```

---

---

## 🌿 Generator Functions

> A **generator function** uses `yield` instead of `return`.
> It produces values **one at a time** — lazy, memory-efficient!

```python
def count_up(start, end):
    """Yield numbers from start to end."""
    current = start
    while current <= end:
        yield current    # pause here, give value, resume later
        current += 1

gen = count_up(1, 5)
print(next(gen))   # 1
print(next(gen))   # 2
for n in count_up(1, 5):
    print(n, end=" ")   # 1 2 3 4 5
```

```python
# ─── Infinite generator ───
def fibonacci_gen():
    """Yield Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take first 10 Fibonacci numbers
gen  = fibonacci_gen()
fibs = [next(gen) for _ in range(10)]
print(fibs)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

```python
# ─── yield from — delegate to sub-generator ───
def chain(*iterables):
    """Yield items from each iterable in sequence."""
    for it in iterables:
        yield from it     # ← same as:  for item in it: yield item

result = list(chain([1,2,3], "ABC", range(4,7)))
print(result)   # [1, 2, 3, 'A', 'B', 'C', 4, 5, 6]
```

```python
# ─── Generator for large data processing ───
def read_csv_lazy(filename):
    """Read a huge CSV file line by line — memory safe!"""
    with open(filename) as f:
        header = next(f).strip().split(",")
        for line in f:
            values = line.strip().split(",")
            yield dict(zip(header, values))

# Process millions of rows with CONSTANT memory usage:
# for row in read_csv_lazy("huge_file.csv"):
#     process(row)
```

---

---

## 🌍 Variable Scope — LEGB Rule

> Python searches for names in this order: **L → E → G → B**

```
L — Local      : inside the current function
E — Enclosing  : inside any enclosing functions (closures)
G — Global     : module-level variables
B — Built-in   : Python's built-in names (len, print, ...)
```

```python
# ─── LEGB demonstration ───
x = "global 🌍"         # G: global

def outer():
    x = "enclosing 🏠"  # E: enclosing (for inner)

    def inner():
        x = "local 🪑"  # L: local (only inside inner)
        print(x)        # local 🪑

    inner()
    print(x)            # enclosing 🏠

outer()
print(x)                # global 🌍
```

```python
# ─── global keyword ───
count = 0

def increment():
    global count       # tell Python: use the GLOBAL count
    count += 1

increment()
increment()
print(count)   # 2

# ─── nonlocal keyword ───
def outer():
    total = 0
    def add(n):
        nonlocal total   # tell Python: use the ENCLOSING total
        total += n
    add(5)
    add(3)
    return total

print(outer())   # 8
```

---

---

## 📝 Function Annotations & Type Hints

```python
# Annotations — document expected types (not enforced at runtime!)

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def greet(name: str, times: int = 1) -> str:
    """Return a greeting string."""
    return f"Hello, {name}! " * times

def process(data: list[int]) -> dict[str, float]:
    """Return statistics for a list of integers."""
    return {
        "mean": sum(data)/len(data),
        "min":  float(min(data)),
        "max":  float(max(data)),
    }

# Access annotations
print(add.__annotations__)
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

```python
# ─── Advanced type hints ───
from typing import Optional, Union, Callable, Any

def find(items: list, predicate: Callable[[Any], bool]) -> Optional[Any]:
    """Return first item matching predicate, or None."""
    for item in items:
        if predicate(item):
            return item
    return None

def process(value: Union[int, float, str]) -> str:
    """Accept int, float, or str and return a string."""
    return str(value).strip()

result = find([1, 2, 3, 4, 5], lambda x: x > 3)
print(result)   # 4
```

---

---

## ⚙️ Special Functions — __dunder__

```python
class Vector:
    """A 2D vector with mathematical operations."""

    def __init__(self, x, y):
        """Initialize with x and y coordinates."""
        self.x = x
        self.y = y

    def __repr__(self):
        """Official string representation."""
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        """Friendly string representation."""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Add two vectors: v1 + v2."""
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """Scale vector: v * scalar."""
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        """Return dimension (always 2 for 2D)."""
        return 2

    def __eq__(self, other):
        """Check equality: v1 == v2."""
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        """Magnitude of vector: abs(v)."""
        return (self.x**2 + self.y**2) ** 0.5

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(repr(v1))       # Vector(3, 4)
print(str(v1))        # (3, 4)
print(v1 + v2)        # (4, 6)
print(v1 * 3)         # (9, 12)
print(abs(v1))        # 5.0
print(v1 == Vector(3,4))   # True
```

---

---

## 🔧 functools Module

```python
from functools import (
    lru_cache, cache, partial, reduce,
    wraps, total_ordering, singledispatch
)

# ─── lru_cache — Memoization ───
@lru_cache(maxsize=128)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

print(fib(50))   # fast!
print(fib.cache_info())   # CacheInfo(hits=48, misses=51, ...)

# ─── partial — Pre-fill arguments ───
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)   # fix exp=2
cube   = partial(power, exp=3)   # fix exp=3
double = partial(lambda x, y: x*y, y=2)

print(square(5))   # 25
print(cube(3))     # 27
print(double(7))   # 14

# ─── reduce ───
nums    = [1, 2, 3, 4, 5]
total   = reduce(lambda a, b: a + b, nums)
product = reduce(lambda a, b: a * b, nums, 1)
print(total)    # 15
print(product)  # 120

# ─── total_ordering — define < and == to get all comparisons ───
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, score):
        self.name  = name
        self.score = score
    def __eq__(self, other):
        return self.score == other.score
    def __lt__(self, other):
        return self.score < other.score

students = [Student("Alice",88), Student("Bob",95), Student("Charlie",72)]
ranked   = sorted(students, reverse=True)
for s in ranked:
    print(f"  {s.name}: {s.score}")
# Bob: 95  Alice: 88  Charlie: 72
```

---

---

## 🌍 Real-World Projects

---

### Project 1 — Function Pipeline Engine

```python
import functools

def compose(*functions):
    """
    Compose functions right-to-left: compose(f,g,h)(x) = f(g(h(x))).

    Args:
        *functions: Functions to compose.

    Returns:
        function: A single composed function.
    """
    def composed(x):
        return functools.reduce(lambda v, f: f(v), reversed(functions), x)
    return composed

def pipe(*functions):
    """
    Pipe functions left-to-right: pipe(f,g,h)(x) = h(g(f(x))).

    Args:
        *functions: Functions to pipe.

    Returns:
        function: A single piped function.
    """
    def piped(x):
        return functools.reduce(lambda v, f: f(v), functions, x)
    return piped

# Build a text processing pipeline
clean_text = pipe(
    str.strip,
    str.lower,
    lambda s: s.replace(",", ""),
    lambda s: s.replace(".", ""),
    str.split,
    lambda words: [w for w in words if len(w) > 2],
    lambda words: " ".join(words),
    str.title,
)

texts = [
    "  Hello, World. How are you today?  ",
    "  Python, is. the BEST language!  ",
]
for t in texts:
    print(f"  Before: {t!r}")
    print(f"  After:  {clean_text(t)!r}")
    print()
```

---

### Project 2 — Recursive JSON Processor

```python
def deep_transform(data, transform_fn, depth=0):
    """
    Recursively apply transform_fn to all leaf values in a nested structure.

    Args:
        data         : Any nested dict/list structure.
        transform_fn : Function to apply to each leaf value.
        depth   (int): Current recursion depth (for debugging).

    Returns:
        The transformed structure.

    Examples:
        >>> deep_transform({"a": 1, "b": [2, 3]}, lambda x: x * 2)
        {'a': 2, 'b': [4, 6]}
    """
    if isinstance(data, dict):
        return {k: deep_transform(v, transform_fn, depth+1) for k,v in data.items()}
    elif isinstance(data, list):
        return [deep_transform(item, transform_fn, depth+1) for item in data]
    else:
        return transform_fn(data)   # leaf value — apply transformation

# Example: double all numbers in a complex structure
config = {
    "server": {"port": 8080, "timeout": 30},
    "limits": {"rate": 100, "burst": 200},
    "retries": [1, 2, 4, 8, 16],
    "name": "my-service",   # strings should stay as-is
}

doubled = deep_transform(
    config,
    lambda x: x * 2 if isinstance(x, (int, float)) else x
)
print(doubled)
# {'server': {'port': 16160, 'timeout': 60},
#  'limits': {'rate': 200, 'burst': 400},
#  'retries': [2, 4, 8, 16, 32],
#  'name': 'my-service'}
```

---

### Project 3 — Decorator-Based Validator

```python
def validate(**rules):
    """
    Decorator factory that validates function arguments.

    Args:
        **rules: Keyword args where key=param name, value=validator function.

    Returns:
        Decorator that validates arguments before calling the function.

    Example:
        @validate(age=lambda x: 0 < x < 150, name=lambda x: bool(x.strip()))
        def create_user(name, age):
            ...
    """
    def decorator(func):
        import inspect
        sig    = inspect.signature(func)
        params = list(sig.parameters.keys())

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for param, value in bound.arguments.items():
                if param in rules:
                    if not rules[param](value):
                        raise ValueError(
                            f"Invalid value for '{param}': {value!r}"
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate(
    name  = lambda x: isinstance(x, str) and x.strip(),
    age   = lambda x: isinstance(x, int) and 0 < x < 150,
    email = lambda x: "@" in x and "." in x.split("@")[-1],
    score = lambda x: 0 <= x <= 100,
)
def register_student(name, age, email, score=0):
    """Register a new student."""
    return {"name": name.title(), "age": age, "email": email, "score": score}

try:
    s = register_student("Alice", 20, "alice@example.com", 88)
    print(f"  ✅ Registered: {s}")

    s = register_student("", 20, "bob@x.com")
    print(f"  ✅ Registered: {s}")
except ValueError as e:
    print(f"  ❌ {e}")
```

---

---

## 🚨 Common Mistakes

### 1. Calling vs Referencing a Function

```python
def greet(): print("Hello!")

greet    # ← does nothing — just references the object
greet()  # ← actually calls and runs it ✅
```

### 2. Mutable Default Argument

```python
# ❌ List persists between calls!
def bad(items=[]):
    items.append("x")
    return items

# ✅ Use None
def good(items=None):
    if items is None: items = []
    items.append("x")
    return items
```

### 3. Forgetting Return

```python
def add(a, b):
    a + b          # ❌ computed but lost!

def add(a, b):
    return a + b   # ✅
```

### 4. Recursion Without Base Case

```python
# ❌ Infinite recursion — RecursionError!
def bad_count(n):
    return bad_count(n-1)   # no base case!

# ✅ Always have a base case
def good_count(n):
    if n <= 0: return 0        # ← base case
    return 1 + good_count(n-1)
```

### 5. Variable Scope Confusion

```python
x = 10
def func():
    print(x)    # ❌ UnboundLocalError — Python sees assignment below!
    x = 20

# ✅ Option A: don't assign locally
def func():
    print(x)    # reads global x

# ✅ Option B: declare global
def func():
    global x
    print(x)
    x = 20
```

### 6. Lambda with Loop Variable

```python
# ❌ All lambdas capture the SAME variable 'i'
fns = [lambda x: x + i for i in range(5)]
print(fns[0](0))   # 4  ← NOT 0! (i=4 when loop ends)

# ✅ Capture by default argument
fns = [lambda x, i=i: x + i for i in range(5)]
print(fns[0](0))   # 0  ← correct!
```

---

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️  DEFINING FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def name():                          # no params
def name(a, b):                      # positional
def name(a, b=10):                   # with default
def name(*args):                     # variable positional → tuple
def name(**kwargs):                  # variable keyword → dict
def name(a, /, b, *, c):            # pos-only / regular / kw-only
def name(a, *args, kw, **kwargs):    # everything

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📖  DOCSTRINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def f(x):
    """One-liner description."""
    ...

def f(x):
    """
    Multi-line description.

    Args:
        x (int): Description of x.

    Returns:
        int: Description of return value.

    Raises:
        ValueError: When x is invalid.

    Examples:
        >>> f(5)
        25
    """
    ...

# Access: f.__doc__  or  help(f)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡  LAMBDA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

f   = lambda x: x**2
f   = lambda x, y: x + y
f   = lambda x: x if x>0 else -x    # ternary OK
f   = lambda *args: sum(args)
f   = lambda **kw: kw

# With built-ins:
sorted(lst, key=lambda x: x[1])
list(map(lambda x: x*2, lst))
list(filter(lambda x: x>0, lst))
reduce(lambda a,b: a+b, lst)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄  RECURSION TEMPLATE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def recursive(input):
    if base_case:              # MUST have this!
        return base_value
    return recursive(smaller) # must move toward base

# Memoize slow recursions:
from functools import lru_cache
@lru_cache(maxsize=None)
def f(n): ...

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏆  HIGHER-ORDER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def hof(func, data):           # accepts function
    return [func(x) for x in data]

def make_func(param):          # returns function
    def inner(x):
        return x * param
    return inner

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎀  DECORATOR TEMPLATE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper

@decorator
def my_func(): ...

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌿  GENERATOR FUNCTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def gen():
    yield value          # pause and give value
    yield from iterable  # delegate to sub-iterator

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔍  SCOPE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

global   x   # use the module-level x
nonlocal x   # use the enclosing function's x

# Search order: Local → Enclosing → Global → Built-in
```

---

## 🎓 Final Summary

```
Functions in Python:
─────────────────────────────────────────────────────────────
DEFINITION    def name(params): body

PARAMETERS    positional, keyword, default, *args, **kwargs,
              positional-only (/), keyword-only (*)

RETURN        single value, multiple values (tuple), None

DOCSTRING     """First statement, describes the function."""
              Styles: one-liner, Google, NumPy, reST
              Access: func.__doc__  |  help(func)

LAMBDA        lambda params: expression
              Best for: sort key, map, filter, reduce

RECURSION     Function calls itself, MUST have base case
              Use lru_cache for expensive recursive calls
              Limit: sys.getrecursionlimit() = 1000

HIGHER-ORDER  Takes function as arg OR returns a function

CLOSURES      Nested function remembers enclosing variables
              Use nonlocal to modify outer variable

DECORATORS    Wrap functions to add behavior (@ syntax)
              Always use @functools.wraps in wrapper

GENERATORS    Use yield instead of return → lazy, low memory

SCOPE (LEGB)  Local → Enclosing → Global → Built-in
─────────────────────────────────────────────────────────────
```

---

