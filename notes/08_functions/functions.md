# 🐍 Python Functions — The Complete Friendly Guide

> **Think of a function like a recipe card! 🍳**
> You write the steps once, and cook it as many times as you want!

---

## 📚 Table of Contents

1. [What is a Function?](#-what-is-a-function)
2. [Defining a Function](#-defining-a-function)
3. [Calling a Function](#-calling-a-function)
4. [Parameters & Arguments](#-parameters--arguments)
5. [Return Values](#-return-values)
6. [Default Parameters](#-default-parameters)
7. [Keyword Arguments](#-keyword-arguments)
8. [*args — Variable Arguments](#-args--variable-arguments)
9. [**kwargs — Keyword Variable Arguments](#-kwargs--keyword-variable-arguments)
10. [Lambda Functions](#-lambda-functions)
11. [Scope — Local vs Global](#-scope--local-vs-global)
12. [Docstrings](#-docstrings)
13. [Nested Functions](#-nested-functions)
14. [Recursion](#-recursion)
15. [Higher-Order Functions](#-higher-order-functions)
16. [Common Mistakes](#-common-mistakes)
17. [Quick Cheat Sheet](#-quick-cheat-sheet)

---

## 🤔 What is a Function?

A **function** is a reusable block of code that does ONE specific job.

```
Without functions 😫             With functions 😎
─────────────────                ─────────────────
print("Hello, Alice!")           greet("Alice")
print("Hello, Bob!")             greet("Bob")
print("Hello, Charlie!")         greet("Charlie")
(copy-paste nightmare!)          (clean & reusable!)
```

### 🧠 Why use functions?

| Benefit | Description |
|--------|-------------|
| ♻️ Reusability | Write once, use many times |
| 🧹 Clean code | Easier to read and understand |
| 🐛 Easy debugging | Fix in ONE place, works everywhere |
| 🧩 Modularity | Break big problems into small pieces |
| 🤝 Teamwork | Share functions with other developers |

---

## ✍️ Defining a Function

```python
#  Anatomy of a function 🏗️
#  ┌── keyword  ┌── name    ┌── parameters
   def  greet  (  name  )  :
       print(f"Hello, {name}! 👋")
#      └── body (indented with 4 spaces!)
```

```python
# 🔵 Simplest function — no parameters
def say_hello():
    print("Hello, World! 🌍")

# 🟢 Function with a parameter
def greet(name):
    print(f"Hey {name}! 😄 Nice to meet you!")

# 🟡 Function with multiple parameters
def add(a, b):
    print(f"{a} + {b} = {a + b} 🔢")
```

> ⚠️ **Remember:** The function body MUST be indented (4 spaces or 1 tab)!

---

## 📞 Calling a Function

Writing a function does NOTHING until you **call** it!

```python
def say_hello():
    print("Hello! 👋")

# Nothing happens yet... 😴

say_hello()   # NOW it runs! ✅
say_hello()   # Run it again! ✅
say_hello()   # And again! ✅
```

```python
# Output:
# Hello! 👋
# Hello! 👋
# Hello! 👋
```

---

## 🎛️ Parameters & Arguments

- **Parameter** = the variable in the function definition 📝
- **Argument** = the actual value you pass when calling 📦

```python
#           parameter ↓
def greet(  name  ):
    print(f"Hi, {name}!")

#         argument ↓
greet(  "Alice"  )   # Hi, Alice!
greet(  "Bob"    )   # Hi, Bob!
```

### Multiple Parameters

```python
def introduce(name, age, city):
    print(f"👤 Name: {name}")
    print(f"🎂 Age:  {age}")
    print(f"🏙️  City: {city}")

introduce("Alice", 25, "Mumbai")
# 👤 Name: Alice
# 🎂 Age:  25
# 🏙️  City: Mumbai
```

> 💡 **Order matters!** Arguments are assigned to parameters by position.

---

## 🎁 Return Values

Functions can **send back** a result using `return`!

```python
# ❌ Without return — just prints, can't reuse the result
def add(a, b):
    print(a + b)      # only prints, lost forever!

# ✅ With return — captures and reuses the result!
def add(a, b):
    return a + b      # sends the value back 📦

result = add(3, 5)
print(result)         # 8
print(add(10, 20))    # 30
print(add(2, 3) * 4)  # 20  ← can use it in expressions!
```

### Returning Multiple Values 🎉

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a TUPLE!

low, high = min_max([3, 1, 9, 5, 7])
print(f"Lowest: {low} 📉  Highest: {high} 📈")
# Lowest: 1 📉  Highest: 9 📈
```

> 💡 `return` also **exits** the function immediately. Anything after it doesn't run!

```python
def check(x):
    if x > 0:
        return "Positive ➕"   # exits here if x > 0
    return "Not positive ➖"   # only runs if x <= 0
```

---

## 🎯 Default Parameters

Give a parameter a **default value** so it's optional!

```python
#                  default ↓
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}! 👋")

greet("Alice")              # Hello, Alice! 👋   (uses default)
greet("Bob", "Hey")         # Hey, Bob! 👋       (overrides default)
greet("Charlie", "Howdy")   # Howdy, Charlie! 👋
```

```python
def make_coffee(size="medium", sugar=1, milk=True):
    print(f"☕ {size} coffee — sugar: {sugar}, milk: {milk}")

make_coffee()                      # ☕ medium coffee — sugar: 1, milk: True
make_coffee("large", 2)            # ☕ large coffee — sugar: 2, milk: True
make_coffee("small", 0, False)     # ☕ small coffee — sugar: 0, milk: False
```

> ⚠️ **Rule:** Parameters WITH defaults must come AFTER parameters WITHOUT defaults!
>
> ```python
> def bad(name="Bob", age):  # ❌ SyntaxError!
> def good(age, name="Bob"): # ✅ Correct!
> ```

---

## 🏷️ Keyword Arguments

Pass arguments **by name** — order doesn't matter!

```python
def profile(name, age, city):
    print(f"👤 {name} | 🎂 {age} | 🏙️ {city}")

# Positional (order matters)
profile("Alice", 25, "Delhi")

# Keyword (order doesn't matter!) 🎉
profile(age=25, city="Delhi", name="Alice")
profile(city="Mumbai", name="Bob", age=30)
```

---

## 📦 *args — Variable Arguments

Accept **any number** of positional arguments!

```python
# * collects extra arguments into a TUPLE
def add_all(*numbers):
    print(f"Numbers received: {numbers}")
    return sum(numbers)

add_all(1, 2)           # Numbers received: (1, 2)         → 3
add_all(1, 2, 3, 4, 5)  # Numbers received: (1, 2, 3, 4, 5) → 15
add_all(10)             # Numbers received: (10,)           → 10
```

```python
def shout(*words):
    for word in words:
        print(word.upper() + "! 📢")

shout("hello", "world", "python")
# HELLO! 📢
# WORLD! 📢
# PYTHON! 📢
```

> 💡 `*args` is just a convention — you can name it `*anything`, but `*args` is standard!

---

## 🗝️ **kwargs — Keyword Variable Arguments

Accept **any number** of keyword arguments as a **dictionary**!

```python
# ** collects extra keyword arguments into a DICT
def describe(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

describe(name="Alice", age=25, city="Bangalore", hobby="coding")
# name: Alice
# age: 25
# city: Bangalore
# hobby: coding
```

### Combining All Together! 🚀

```python
def super_func(required, *args, default="hi", **kwargs):
    print(f"Required: {required}")
    print(f"Extra args: {args}")
    print(f"Default: {default}")
    print(f"Keyword extras: {kwargs}")

super_func("must", 1, 2, 3, default="hello", x=10, y=20)
```

> 💡 **Order rule:** `normal` → `*args` → `default` → `**kwargs`

---

## ⚡ Lambda Functions

**Anonymous** (no-name) one-liner functions!

```python
# Normal function
def square(x):
    return x * x

# Lambda equivalent ⚡
square = lambda x: x * x

print(square(5))   # 25
```

```python
# Syntax:
# lambda arguments : expression
#         ↑               ↑
#     like parameters   like return value

double  = lambda x: x * 2
add     = lambda x, y: x + y
greet   = lambda name: f"Hello, {name}! 👋"

print(double(4))         # 8
print(add(3, 7))         # 10
print(greet("Bob"))      # Hello, Bob! 👋
```

### Best use: with `sorted()`, `map()`, `filter()`

```python
names = ["Charlie", "Alice", "Bob"]

# Sort by length 📏
sorted_names = sorted(names, key=lambda n: len(n))
print(sorted_names)   # ['Bob', 'Alice', 'Charlie']

# Sort alphabetically by last character
sorted_last = sorted(names, key=lambda n: n[-1])
print(sorted_last)    # ['Alice', 'Charlie', 'Bob']
```

> ⚠️ Lambda is for simple, short operations. Use `def` for anything complex!

---

## 🌍 Scope — Local vs Global

**Where** a variable is created decides where it can be used!

```python
x = "global 🌍"          # Global — accessible EVERYWHERE

def my_func():
    y = "local 🏠"        # Local — only inside this function
    print(x)              # ✅ Can see global
    print(y)              # ✅ Can see local

my_func()
print(x)                  # ✅ Can see global
print(y)                  # ❌ NameError! y doesn't exist here!
```

### Modifying a Global Variable

```python
count = 0   # 🌍 global

def increment():
    global count        # 📢 "I mean the global one!"
    count += 1

increment()
increment()
print(count)   # 2 ✅
```

> 💡 **Best practice:** Avoid using `global` whenever possible. Return values instead!

---

## 📖 Docstrings

Document your functions so others (and future-you!) understand them!

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI) 💪

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m  (float): Height in meters

    Returns:
        float: The BMI value

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return round(weight_kg / (height_m ** 2), 2)

# Access the docs anytime!
help(calculate_bmi)
print(calculate_bmi.__doc__)
```

> 💡 Good docstrings = 🎁 for your teammates and your future self!

---

## 🪆 Nested Functions

Functions **inside** functions!

```python
def outer():
    print("I'm the outer function 🏠")

    def inner():
        print("I'm the inner function 🛋️")

    inner()   # Call inner from inside outer

outer()
# I'm the outer function 🏠
# I'm the inner function 🛋️

# inner()   ← ❌ Can't call from outside!
```

### Closure — Inner function remembers outer variables!

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor   # 'factor' remembered! 🧠
    return multiply              # return the function itself!

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(double(9))   # 18
```

---

## 🔄 Recursion

A function that **calls itself**! 🪞

```python
# Factorial: 5! = 5 × 4 × 3 × 2 × 1 = 120
def factorial(n):
    if n == 0 or n == 1:     # 🛑 Base case — stops the recursion!
        return 1
    return n * factorial(n - 1)   # 🔄 Recursive call

print(factorial(5))   # 120
print(factorial(0))   # 1
```

```
factorial(5)
  └── 5 * factorial(4)
          └── 4 * factorial(3)
                  └── 3 * factorial(2)
                          └── 2 * factorial(1)
                                  └── 1  ← base case!
```

> ⚠️ **Always** have a base case, or you'll get infinite recursion! 💀

---

## 🏆 Higher-Order Functions

Functions that take **other functions** as arguments or return them!

### `map()` — Apply a function to every item 🗺️

```python
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
print(squared)   # [1, 4, 9, 16, 25] 🔢
```

### `filter()` — Keep only matching items 🔍

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10] ✅
```

### `sorted()` with key 🔀

```python
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob",   "grade": 95},
    {"name": "Carol", "grade": 72},
]

# Sort by grade (highest first)
top = sorted(students, key=lambda s: s["grade"], reverse=True)
for s in top:
    print(f"🎓 {s['name']}: {s['grade']}")
# 🎓 Bob: 95
# 🎓 Alice: 88
# 🎓 Carol: 72
```

---

## 🚨 Common Mistakes

### 1. Forgetting to call the function

```python
def greet():
    print("Hello!")

greet    # ❌ Does nothing — just references the function
greet()  # ✅ Actually calls it!
```

### 2. Not returning a value

```python
def add(a, b):
    a + b          # ❌ Calculates but throws it away!

def add(a, b):
    return a + b   # ✅ Sends the result back!
```

### 3. Returning inside a loop too early

```python
# ❌ Returns after first item only!
def find_evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n   # exits immediately!

# ✅ Collect all, then return
def find_evens(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens
```

### 4. Mutable default arguments 🐛

```python
# ❌ Bug! List is shared across ALL calls
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item("a"))   # ['a']
print(add_item("b"))   # ['a', 'b']  ← Unexpected!

# ✅ Use None as default
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

---

## 📝 Quick Cheat Sheet

```python
# 1️⃣ Basic function
def greet(name):
    return f"Hello, {name}!"

# 2️⃣ Default parameter
def greet(name, greeting="Hi"):
    return f"{greeting}, {name}!"

# 3️⃣ *args (variable positional)
def total(*nums):
    return sum(nums)

# 4️⃣ **kwargs (variable keyword)
def info(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

# 5️⃣ Lambda
square = lambda x: x**2

# 6️⃣ Returning multiple values
def stats(nums):
    return min(nums), max(nums), sum(nums)
lo, hi, total = stats([1,2,3,4,5])

# 7️⃣ map + filter
evens   = list(filter(lambda x: x%2==0, range(10)))
doubled = list(map(lambda x: x*2, range(10)))

# 8️⃣ Docstring
def func(x):
    """What this function does."""
    return x

# 9️⃣ Recursion
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)

# 🔟 Nested / Closure
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply
triple = multiplier(3)
```

---

## 🎓 Summary

| Concept | One-liner |
|---------|-----------|
| `def` | Define a reusable block of code |
| Parameters | Variables in function definition |
| Arguments | Values passed when calling |
| `return` | Send a value back to the caller |
| Default params | Optional parameters with preset values |
| `*args` | Accept unlimited positional arguments |
| `**kwargs` | Accept unlimited keyword arguments |
| `lambda` | Quick anonymous one-liner function |
| Scope | Where variables live (local vs global) |
| Docstring | Documentation string inside function |
| Recursion | Function calling itself with a base case |
| Higher-order | Functions taking/returning other functions |

---
