# 🐍 Python Variables & Data Types
## Zero to Hero — The Fun & Complete Guide

> 🧠 **Before we start:** Python is like a super-smart assistant.
> You tell it *"remember this!"* — and it does. That's a **variable**.
> You tell it *"this is a number"* or *"this is text"* — that's a **data type**.
> Together, they're the **foundation of ALL Python programs.**

---

## 📚 Table of Contents

1. [What is a Variable?](#-what-is-a-variable)
2. [Variable Naming Rules](#-variable-naming-rules)
3. [Data Types Overview](#-data-types-overview)
4. [int — Integers](#-int--integers)
5. [float — Decimals](#-float--decimals)
6. [str — Strings](#-str--strings)
7. [bool — Booleans](#-bool--booleans)
8. [list — Lists](#-list--lists)
9. [tuple — Tuples](#-tuple--tuples)
10. [set — Sets](#-set--sets)
11. [dict — Dictionaries](#-dict--dictionaries)
12. [NoneType — None](#-nonetype--none)
13. [Type Conversion](#-type-conversion)
14. [type() and isinstance()](#-type-and-isinstance)
15. [How Python Stores Variables (References!)](#-how-python-stores-variables-references)
16. [Mutable vs Immutable](#-mutable-vs-immutable)
17. [Multiple Assignment Tricks](#-multiple-assignment-tricks)
18. [Quick Reference Cheat Sheet](#-quick-reference-cheat-sheet)

---

## 📦 What is a Variable?

Imagine your computer's memory as a **giant set of lockers** 🗄️

A **variable** is:
- A **locker** where you store some data 📦
- The **variable name** is the label on the locker 🏷️
- The **value** is what's inside the locker 🎁

```python
# Syntax:  name  =  value
            age  =  25
#           ↑         ↑
#        (label)   (what's inside)
```

```python
# 🔵 Storing different kinds of information
name    = "Alice"        # 📦 Locker "name"   holds → "Alice"
age     = 25             # 📦 Locker "age"    holds → 25
height  = 5.6            # 📦 Locker "height" holds → 5.6
is_cool = True           # 📦 Locker "is_cool" holds → True

# Using them
print(name)     # Alice
print(age)      # 25
print(height)   # 5.6
print(is_cool)  # True
```

### 🔄 Variables can change! (That's why they're called VARI-ables)

```python
score = 0
print(score)   # 0   🎮 Game starts

score = 10
print(score)   # 10  🎯 Got a point!

score = score + 5
print(score)   # 15  🏆 Got another 5!

score += 20    # shortcut for score = score + 20
print(score)   # 35  🔥 On fire!
```

### 🪄 Python figures out the type automatically!

Unlike some languages, Python is **dynamically typed** — you don't say "this is an integer" — Python figures it out!

```python
# Java (boring 😴):   int age = 25;
# Python (cool 😎):
age = 25        # Python: "Got it! That's an integer 🔢"
name = "Alice"  # Python: "Got it! That's a string 📝"
pi = 3.14       # Python: "Got it! That's a float 💧"
```

---

## 🏷️ Variable Naming Rules

### ✅ Rules you MUST follow

```python
# ✅ Start with a letter or underscore
name    = "Alice"
_score  = 100
myVar   = 42

# ✅ Can contain letters, numbers, underscores
player1      = "Alice"
high_score   = 9999
my_variable  = "hello"

# ❌ CANNOT start with a number
1player = "Alice"    # SyntaxError 💥

# ❌ CANNOT have spaces
my name = "Alice"    # SyntaxError 💥

# ❌ CANNOT use special characters
my-var = 10          # SyntaxError 💥
my@var = 10          # SyntaxError 💥

# ❌ CANNOT use Python keywords
if     = 5           # SyntaxError 💥
for    = 10          # SyntaxError 💥
class  = "Math"      # SyntaxError 💥
```

### 🎨 Naming Styles (Conventions)

```python
# 🐍 snake_case — THE Python standard (recommended!)
first_name   = "Alice"
total_score  = 100
is_logged_in = True

# 🐫 camelCase — used in JavaScript, not preferred in Python
firstName   = "Alice"    # works, but not Pythonic

# 📢 UPPER_SNAKE_CASE — for constants (values that never change)
MAX_SPEED     = 300
PI            = 3.14159
DATABASE_URL  = "localhost:5432"

# 🏛️ PascalCase — for Class names only
class MyClassName:
    pass
```

### 🚫 Reserved Keywords — NEVER use these as names!

```
False    True     None     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

```python
# ✅ Good names
sum_total   = 100     # not 'sum' (built-in function name)
my_list     = []      # not 'list'
my_input    = "hi"    # not 'input'
my_id       = 42      # not 'id'
```

---

## 🗺️ Data Types Overview

```
Python Data Types
│
├── 📊 Numeric
│   ├── int       →  1, 42, -7, 0
│   ├── float     →  3.14, -0.5, 2.0
│   └── complex   →  3+4j   (advanced)
│
├── 📝 Text
│   └── str       →  "hello", 'world', """multiline"""
│
├── ✅ Boolean
│   └── bool      →  True, False
│
├── 📋 Sequences
│   ├── list      →  [1, 2, 3]          (ordered, changeable)
│   └── tuple     →  (1, 2, 3)          (ordered, unchangeable)
│
├── 🔑 Mapping
│   └── dict      →  {"key": "value"}   (key-value pairs)
│
├── 🎯 Sets
│   └── set       →  {1, 2, 3}          (unique items)
│
└── 🚫 Nothing
    └── NoneType  →  None
```

---

## 🔢 int — Integers

**Whole numbers** — no decimal point. Positive, negative, or zero.

```python
# 📌 Basic integers
age        = 25
score      = 0
floors     = -3       # underground! 🏗️
population = 1428600000  # India's population 🇮🇳

# 📌 Math operations
a = 10
b = 3

print(a + b)    # 13   ➕ addition
print(a - b)    # 7    ➖ subtraction
print(a * b)    # 30   ✖️ multiplication
print(a / b)    # 3.333...  ➗ division (always returns float!)
print(a // b)   # 3    ⬇️ floor division (no decimal)
print(a % b)    # 1    🔄 modulo (remainder)
print(a ** b)   # 1000 💪 power (10³)
```

```python
# 🔬 Fun: int has no size limit in Python!
huge = 99999999999999999999999999999999999999
print(huge + 1)   # works perfectly! 🤯 (unlike C/Java)
```

```python
# 🎨 Different ways to write ints
decimal = 255           # normal
binary  = 0b11111111   # binary (0b prefix)   → also 255
octal   = 0o377        # octal  (0o prefix)   → also 255
hex_val = 0xFF         # hex    (0x prefix)   → also 255

print(decimal == binary == octal == hex_val)   # True ✅

# Readable large numbers with underscores!
million    = 1_000_000
billion    = 1_000_000_000
phone_num  = 98_765_43210
print(million)   # 1000000 (underscores are ignored!)
```

### 🔗 Reference Example — int in action

```python
# 🎮 A simple score tracker
player_score = 0
bonus_points = 50
penalty      = 10
multiplier   = 2

player_score += bonus_points      # 0 + 50 = 50
player_score -= penalty           # 50 - 10 = 40
player_score *= multiplier        # 40 * 2 = 80
player_score += bonus_points // 2 # 80 + 25 = 105

print(f"🏆 Final Score: {player_score}")   # 🏆 Final Score: 105

# Is it a high score? (using modulo for fun)
print(f"Score is {'even' if player_score % 2 == 0 else 'odd'}")
# Score is odd
```

---

## 💧 float — Decimals

Numbers **with** a decimal point.

```python
# 📌 Basic floats
pi        = 3.14159
price     = 99.99
temp      = -12.5
gravity   = 9.81

# 📌 Scientific notation
speed_of_light  = 3e8       # 3 × 10⁸ = 300000000.0
electron_mass   = 9.11e-31  # tiny! 0.000...00000911
```

```python
# ⚠️ The famous float surprise!
print(0.1 + 0.2)           # 0.30000000000000004  😱
print(0.1 + 0.2 == 0.3)    # False  😨

# ✅ Fix it with round()
print(round(0.1 + 0.2, 2))          # 0.3  ✅
print(round(0.1 + 0.2, 2) == 0.3)   # True ✅

# ✅ Or use math.isclose() for comparisons
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True ✅
```

```python
# 📌 Useful float functions
print(round(3.14159, 2))    # 3.14   (round to 2 decimal places)
print(int(3.9))             # 3      (cuts decimal, doesn't round!)
print(abs(-4.5))            # 4.5    (absolute value)

import math
print(math.floor(3.9))     # 3      (round DOWN always)
print(math.ceil(3.1))      # 4      (round UP always)
print(math.sqrt(16))       # 4.0    (square root)
```

### 🔗 Reference Example — float in action

```python
# 🛒 Shopping Cart Calculator
item1_price  = 299.99
item2_price  = 149.50
item3_price  = 49.99

subtotal     = item1_price + item2_price + item3_price
discount     = subtotal * 0.10   # 10% off 🏷️
tax          = (subtotal - discount) * 0.18   # 18% GST
total        = subtotal - discount + tax

print(f"🛍️  Subtotal:  ₹{subtotal:.2f}")
print(f"🏷️  Discount:  ₹{discount:.2f}")
print(f"📋  GST (18%): ₹{tax:.2f}")
print(f"💰  Total:     ₹{total:.2f}")

# Output:
# 🛍️  Subtotal:  ₹499.48
# 🏷️  Discount:  ₹49.95
# 📋  GST (18%): ₹80.91
# 💰  Total:     ₹530.44
```

---

## 📝 str — Strings

**Text data** — any characters wrapped in quotes.

```python
# 📌 Three ways to create strings
single   = 'Hello'           # single quotes
double   = "Hello"           # double quotes (same thing!)
multi    = """
Hello,
I am a
multiline string! 📝
"""

# Why both quotes exist — use the other to avoid escaping!
quote1 = "It's a great day!"        # ✅ apostrophe inside double quotes
quote2 = 'He said "Hello!"'         # ✅ speech marks inside single quotes
quote3 = "She said \"Wow!\""        # ✅ escaped with backslash
```

### 🧮 String Operations

```python
first = "Hello"
last  = "World"

# ➕ Concatenation (joining)
full = first + " " + last
print(full)             # Hello World

# ✖️ Repetition
line = "-" * 20
print(line)             # --------------------

# 📏 Length
print(len("Python"))    # 6

# 🔢 Indexing — each character has a position
word = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5   ← forward index
#      -6 -5 -4 -3 -2 -1   ← backward index

print(word[0])    # P   (first character)
print(word[3])    # h
print(word[-1])   # n   (LAST character)
print(word[-2])   # o   (second from last)

# ✂️ Slicing — grab a chunk!
# word[start : stop : step]
print(word[0:3])    # Pyt   (index 0,1,2 — stop is excluded!)
print(word[2:])     # thon  (from index 2 to end)
print(word[:4])     # Pyth  (from start to index 3)
print(word[::2])    # Pto   (every 2nd character)
print(word[::-1])   # nohtyP (REVERSED! 🔄)
```

### 🎨 String Formatting (3 ways!)

```python
name  = "Alice"
age   = 25
score = 98.6

# 1️⃣ f-strings (BEST — modern, readable) ⭐
print(f"Name: {name}, Age: {age}, Score: {score:.1f}")

# 2️⃣ .format() method
print("Name: {}, Age: {}, Score: {:.1f}".format(name, age, score))

# 3️⃣ % formatting (old style)
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# f-string superpowers! 🦸
num = 1234567.89
print(f"Formatted: {num:,.2f}")    # 1,234,567.89
print(f"Padded:    {name:>10}")    #      Alice (right-align in 10 chars)
print(f"Padded:    {name:<10}|")   # Alice      (left-align)
print(f"Padded:    {name:^10}|")   #   Alice    (center-align)
print(f"Binary:    {42:b}")        # 101010
print(f"Hex:       {255:x}")       # ff
```

### 🔧 Essential String Methods

```python
text = "  Hello, Python World!  "

# 🧹 Cleaning
print(text.strip())             # "Hello, Python World!"  (removes spaces)
print(text.lstrip())            # "Hello, Python World!  "
print(text.rstrip())            # "  Hello, Python World!"

# 🔡 Case changing
print("hello".upper())         # HELLO
print("HELLO".lower())         # hello
print("hello world".title())   # Hello World
print("Hello".swapcase())      # hELLO

# 🔍 Searching
msg = "I love Python and Python loves me"
print(msg.find("Python"))       # 7   (index of first match)
print(msg.count("Python"))      # 2   (how many times?)
print(msg.startswith("I"))      # True
print(msg.endswith("me"))       # True
print("Python" in msg)          # True ← easiest way!

# ✂️ Splitting & Joining
csv_line = "Alice,25,Engineer,Mumbai"
parts = csv_line.split(",")
print(parts)    # ['Alice', '25', 'Engineer', 'Mumbai']

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)   # Python is awesome

# 🔄 Replacing
dirty = "I hate Mondays"
clean = dirty.replace("hate", "love")
print(clean)      # I love Mondays ❤️
```

### 🔗 Reference Example — str in action

```python
# 🪪 ID Card Generator
first_name  = "  alice  "
last_name   = "SHARMA"
email       = "alice.sharma@example.com"
department  = "engineering"
employee_id = 42

# Clean and format
first_name  = first_name.strip().title()    # "Alice"
last_name   = last_name.title()             # "Sharma"
full_name   = f"{first_name} {last_name}"   # "Alice Sharma"
department  = department.title()            # "Engineering"
emp_id_str  = f"EMP{employee_id:04d}"      # "EMP0042"

# Username from email
username    = email.split("@")[0]           # "alice.sharma"

print("=" * 35)
print("🪪  EMPLOYEE ID CARD")
print("=" * 35)
print(f"  Name       : {full_name}")
print(f"  Employee ID: {emp_id_str}")
print(f"  Department : {department}")
print(f"  Username   : {username}")
print(f"  Email      : {email.lower()}")
print("=" * 35)
```

**Output:**
```
===================================
🪪  EMPLOYEE ID CARD
===================================
  Name       : Alice Sharma
  Employee ID: EMP0042
  Department : Engineering
  Username   : alice.sharma
  Email      : alice.sharma@example.com
===================================
```

---

## ✅ bool — Booleans

Only **two** possible values: `True` or `False` (capital T and F!)

```python
# 📌 Basic booleans
is_raining   = True
has_umbrella = False
is_logged_in = True
is_admin     = False

# 📌 Booleans from comparisons
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True  (== checks equality)
print(5 != 3)    # True  (!= checks NOT equal)
print(5 >= 5)    # True
print(5 <= 4)    # False
```

### 🔗 Logical Operators: and, or, not

```python
# and → BOTH must be True
print(True and True)    # True  ✅
print(True and False)   # False ❌
print(False and True)   # False ❌
print(False and False)  # False ❌

# or → at LEAST ONE must be True
print(True or True)     # True  ✅
print(True or False)    # True  ✅
print(False or True)    # True  ✅
print(False or False)   # False ❌

# not → FLIPS the boolean
print(not True)    # False
print(not False)   # True
```

### 🪄 Truthy and Falsy — Every value has a boolean nature!

```python
# 🔴 FALSY — these all act like False
print(bool(0))         # False (zero)
print(bool(0.0))       # False (zero float)
print(bool(""))        # False (empty string)
print(bool([]))        # False (empty list)
print(bool({}))        # False (empty dict)
print(bool(None))      # False (nothing)

# 🟢 TRUTHY — these all act like True
print(bool(1))         # True  (any non-zero number)
print(bool(-42))       # True  (negative too!)
print(bool("hello"))   # True  (non-empty string)
print(bool([1,2,3]))   # True  (non-empty list)
print(bool({"a":1}))   # True  (non-empty dict)
```

```python
# 🔗 This lets you write clean conditions!
username = ""
password = "secret123"

# Without truthy/falsy (verbose) 😴
if len(username) == 0:
    print("Username empty!")

# With truthy/falsy (Pythonic) 😎
if not username:
    print("Username empty!")

# Practical example
cart_items = []
if not cart_items:
    print("🛒 Your cart is empty! Start shopping.")
```

### 🔗 Reference Example — bool in action

```python
# 🎢 Amusement Park Ride Checker
height_cm   = 145
age         = 14
has_ticket  = True
feels_sick  = False

# 📏 Rules: height > 140cm AND age >= 12 AND has ticket AND not sick
meets_height  = height_cm > 140        # True
meets_age     = age >= 12              # True
can_ride      = (meets_height
                 and meets_age
                 and has_ticket
                 and not feels_sick)

print(f"Height OK  : {meets_height}")   # True
print(f"Age OK     : {meets_age}")      # True
print(f"Has Ticket : {has_ticket}")     # True
print(f"Feels Sick : {feels_sick}")     # False

print()
if can_ride:
    print("✅ Enjoy the ride! 🎢")
else:
    print("❌ Sorry, you can't ride this one.")

# Output: ✅ Enjoy the ride! 🎢
```

---

## 📋 list — Lists

An **ordered, changeable** collection of items. Can hold **mixed types**!

```python
# 📌 Creating lists
fruits     = ["apple", "banana", "cherry"]
numbers    = [1, 2, 3, 4, 5]
mixed      = [1, "hello", 3.14, True, None]   # mix of types!
empty      = []
nested     = [[1,2,3], [4,5,6], [7,8,9]]      # list inside list!

# 📌 Accessing items (same as strings — indexing + slicing)
print(fruits[0])     # apple
print(fruits[-1])    # cherry
print(fruits[1:])    # ['banana', 'cherry']
```

### ✏️ Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# ➕ Adding
fruits.append("mango")            # add to END
fruits.insert(1, "orange")        # insert at index 1
fruits.extend(["kiwi", "grape"])  # add multiple

print(fruits)
# ['apple', 'orange', 'banana', 'cherry', 'mango', 'kiwi', 'grape']

# ✏️ Changing
fruits[0] = "pineapple"    # change first item
print(fruits[0])           # pineapple

# ➖ Removing
fruits.remove("banana")    # remove by VALUE (first match)
popped = fruits.pop()      # remove & return LAST item
popped2 = fruits.pop(1)    # remove & return item at index 1
del fruits[0]              # delete by index

# 🔄 Other operations
fruits.sort()              # sort alphabetically (in-place)
fruits.reverse()           # reverse order (in-place)
print(fruits.index("kiwi")) # find index of value
print(fruits.count("kiwi")) # count occurrences
copy = fruits.copy()        # make a copy
fruits.clear()              # remove all items
```

### 🔗 Reference Example — list in action

```python
# 📚 Student Grade Book
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores   = [88, 92, 75, 95, 83]

# Find stats
highest   = max(scores)
lowest    = min(scores)
average   = sum(scores) / len(scores)
top_index = scores.index(highest)
top_name  = students[top_index]

print(f"📊 Class Report")
print(f"{'─'*30}")

# Print each student with score
for i in range(len(students)):
    grade = "⭐" if scores[i] >= 90 else "✅" if scores[i] >= 80 else "📚"
    print(f"  {grade} {students[i]:<10} : {scores[i]}")

print(f"{'─'*30}")
print(f"  🏆 Top Scorer : {top_name} ({highest})")
print(f"  📉 Lowest     : {lowest}")
print(f"  📊 Average    : {average:.1f}")

# Sort students by score
paired   = list(zip(students, scores))         # [("Alice",88), ...]
ranked   = sorted(paired, key=lambda x: x[1], reverse=True)
print(f"\n🥇 Rankings:")
for rank, (name, score) in enumerate(ranked, 1):
    print(f"  {rank}. {name} — {score}")
```

---

## 🔒 tuple — Tuples

Like a list but **immutable** (can't be changed after creation).
Use `()` instead of `[]`.

```python
# 📌 Creating tuples
point      = (3, 7)                          # x, y coordinates
rgb        = (255, 128, 0)                   # color (red, green, blue)
dimensions = (1920, 1080)                    # screen size
person     = ("Alice", 25, "Engineer")       # name, age, job
single     = (42,)                           # ⚠️ single item needs trailing comma!
empty      = ()

# 📌 Accessing (same as list)
print(point[0])     # 3
print(rgb[-1])      # 0
print(person[1:])   # (25, 'Engineer')

# ❌ Cannot modify!
rgb[0] = 100    # TypeError: 'tuple' object does not support item assignment

# ✅ But you can create a NEW tuple
rgb = rgb[:2] + (100,)   # (255, 128, 100)
```

### 🎁 Tuple Unpacking — super useful!

```python
# 📌 Unpack values into variables
point = (3, 7)
x, y  = point           # x=3, y=7

rgb = (255, 128, 0)
red, green, blue = rgb  # red=255, green=128, blue=0

person = ("Alice", 25, "Mumbai")
name, age, city = person

# 🔄 Swap variables (Python magic!)
a = 10
b = 20
a, b = b, a     # Swap!
print(a, b)     # 20 10 ✅

# 🌟 Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*start, last = (1, 2, 3, 4, 5)
print(start)   # [1, 2, 3, 4]
print(last)    # 5
```

### 🔗 Reference Example — tuple in action

```python
# 📍 GPS Location Tracker
locations = [
    ("Eiffel Tower",    48.8584,  2.2945),
    ("Colosseum",       41.8902, 12.4922),
    ("Taj Mahal",       27.1751, 78.0421),
    ("Great Wall",      40.4319, 116.5704),
]

# Tuples = safe coordinates (shouldn't change!)
print("🗺️  World Landmarks:")
print(f"{'─'*50}")

for name, lat, lon in locations:    # tuple unpacking in for loop!
    direction_ns = "N" if lat >= 0 else "S"
    direction_ew = "E" if lon >= 0 else "W"
    print(f"  📍 {name:<18} {abs(lat):.4f}°{direction_ns}, {abs(lon):.4f}°{direction_ew}")
```

---

## 🎯 set — Sets

**Unordered** collection of **unique** items. No duplicates!

```python
# 📌 Creating sets
fruits  = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed   = {1, "hello", 3.14}
empty   = set()          # ⚠️ NOT {} — that's an empty dict!

# 🔑 Key feature: DUPLICATES removed automatically!
nums = {1, 2, 2, 3, 3, 3, 4}
print(nums)   # {1, 2, 3, 4}  ← duplicates gone! 🪄

# Use case: remove duplicates from a list!
my_list   = [1, 2, 2, 3, 3, 3, 4, 4]
no_dupes  = list(set(my_list))
print(no_dupes)   # [1, 2, 3, 4]
```

### 🔧 Set Operations (like Math sets!)

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# 🔗 Union — all items from both
print(a | b)          # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))     # same thing

# 🔀 Intersection — only items in BOTH
print(a & b)               # {4, 5}
print(a.intersection(b))   # same thing

# ➖ Difference — in a but NOT in b
print(a - b)              # {1, 2, 3}
print(a.difference(b))    # same thing

# △ Symmetric Difference — in one but NOT both
print(a ^ b)                        # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))    # same thing

# 🔍 Subset and Superset
small = {1, 2}
print(small.issubset(a))     # True  (small ⊆ a)
print(a.issuperset(small))   # True  (a ⊇ small)
```

### 🔗 Reference Example — set in action

```python
# 🎬 Movie Recommendation System
alice_watched   = {"Inception", "Interstellar", "The Matrix", "Avatar", "Dune"}
bob_watched     = {"Dune", "The Matrix", "Parasite", "1917", "Inception"}
new_releases    = {"Dune 2", "Oppenheimer", "Interstellar", "Avatar 2", "1917"}

# What have both watched? (common movies)
both_watched    = alice_watched & bob_watched
print(f"🎬 Both watched: {both_watched}")

# What's new that Alice hasn't seen yet?
alice_new_picks = new_releases - alice_watched
print(f"🍿 New for Alice: {alice_new_picks}")

# All unique movies combined (no repeats)
all_movies = alice_watched | bob_watched | new_releases
print(f"🎥 Total unique movies: {len(all_movies)}")
```

---

## 🔑 dict — Dictionaries

**Key-value pairs** — like a real dictionary (word → definition)!

```python
# 📌 Creating dicts
person = {
    "name"      : "Alice",
    "age"       : 25,
    "city"      : "Mumbai",
    "is_student": False
}

# 📌 Keys can be strings, numbers, or tuples (must be immutable)
phone_book = {
    "Alice" : "9876543210",
    "Bob"   : "9123456789",
    "Carol" : "9988776655",
}

# 📌 Accessing values
print(person["name"])               # Alice
print(person.get("age"))            # 25
print(person.get("salary", 0))      # 0  ← default if key missing (safe!)

# ❌ person["salary"] → KeyError! (key doesn't exist)
# ✅ person.get("salary", 0) → 0    (safe!)
```

### ✏️ Modifying Dicts

```python
person = {"name": "Alice", "age": 25}

# ➕ Adding / Updating
person["city"]  = "Mumbai"    # add new key
person["age"]   = 26          # update existing key

# 🔄 Update multiple at once
person.update({"email": "alice@example.com", "age": 27})

# ➖ Removing
removed   = person.pop("city")          # remove & return value
last_item = person.popitem()            # remove & return last (key,value)
del person["email"]                     # delete by key
person.clear()                          # remove everything

# 📋 Useful methods
info = {"name": "Alice", "age": 25, "city": "Mumbai"}
print(info.keys())     # dict_keys(['name', 'age', 'city'])
print(info.values())   # dict_values(['Alice', 25, 'Mumbai'])
print(info.items())    # dict_items([('name','Alice'),('age',25),...])

# 🔍 Checking existence
print("name" in info)   # True  (checks KEYS by default)
print("Alice" in info.values())   # True (check values)
```

### 🔗 Reference Example — dict in action

```python
# 🏪 Inventory Management System
inventory = {
    "apple"    : {"price": 40,  "stock": 150, "unit": "kg"},
    "banana"   : {"price": 30,  "stock": 80,  "unit": "dozen"},
    "mango"    : {"price": 120, "stock": 25,  "unit": "kg"},
    "orange"   : {"price": 60,  "stock": 0,   "unit": "kg"},
}

print(f"{'─'*50}")
print(f"🏪  STORE INVENTORY")
print(f"{'─'*50}")
print(f"  {'Item':<12} {'Price':>8} {'Stock':>8} {'Status'}")
print(f"{'─'*50}")

for item, details in inventory.items():
    price  = details["price"]
    stock  = details["stock"]
    unit   = details["unit"]
    status = "✅ In Stock" if stock > 0 else "❌ Out of Stock"
    print(f"  {item.title():<12} ₹{price:>6}/{unit}  {stock:>4}   {status}")

# Total inventory value
total_value = sum(
    details["price"] * details["stock"]
    for details in inventory.values()
)
print(f"{'─'*50}")
print(f"  💰 Total Inventory Value: ₹{total_value:,}")
```

---

## 🚫 NoneType — None

`None` means **nothing, empty, no value**. It's Python's way of saying "absent".

```python
# 📌 None is NOT zero, NOT False, NOT empty string
result   = None    # explicitly nothing
x        = 0       # the number zero
y        = False   # boolean false
z        = ""      # empty string

print(result == x)     # False (None ≠ 0)
print(result == y)     # False (None ≠ False)
print(result is None)  # True  ← always use 'is' to check None!

# 📌 Functions return None by default
def do_nothing():
    pass           # no return statement

output = do_nothing()
print(output)           # None
print(type(output))     # <class 'NoneType'>
```

```python
# 📌 Common use: "not found yet" placeholder
user_input  = None
search_result = None

# later...
user_input = input("Enter name: ")

# Check before using
if search_result is None:
    print("No result found 🔍")
else:
    print(f"Found: {search_result}")
```

```python
# 📌 None as default argument (best practice!)
def add_to_list(item, my_list=None):    # ✅ Safe!
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

---

## 🔄 Type Conversion

Convert one data type to another!

```python
# 📌 str → int / float
age_str  = "25"
age_int  = int(age_str)      # "25" → 25
pi_str   = "3.14"
pi_float = float(pi_str)     # "3.14" → 3.14

# 📌 int / float → str
num = 42
text = str(num)              # 42 → "42"
print("Number: " + text)     # ✅ works now (can't add int to string)

# 📌 int ↔ float
print(int(3.9))      # 3     (truncates, doesn't round!)
print(int(-3.9))     # -3    (towards zero)
print(float(5))      # 5.0

# 📌 → bool
print(bool(1))       # True
print(bool(0))       # False
print(bool("hi"))    # True
print(bool(""))      # False

# 📌 → list / tuple / set
print(list("hello"))         # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))       # [1, 2, 3]
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(set([1, 2, 2, 3, 3]))  # {1, 2, 3}
```

### ⚠️ Conversion Errors — Handle Them!

```python
# ❌ These will crash!
int("hello")    # ValueError: invalid literal
int("3.14")     # ValueError: "3.14" is not an integer
float("abc")    # ValueError

# ✅ Safe conversion with try-except
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"⚠️ Can't convert '{value}' to int!")
        return None

print(safe_int("42"))      # 42
print(safe_int("hello"))   # ⚠️ Can't convert 'hello' to int!  → None
```

### 🔗 Reference Example — Type Conversion in action

```python
# 📊 CSV Data Processor
# Imagine this came from a file — everything is a string!
raw_data = [
    "Alice,25,88.5,True",
    "Bob,30,92.0,False",
    "Charlie,22,75.5,True",
]

students = []
for row in raw_data:
    parts = row.split(",")
    student = {
        "name"    : parts[0],                    # str → stays str
        "age"     : int(parts[1]),               # str → int
        "score"   : float(parts[2]),             # str → float
        "active"  : parts[3] == "True"           # str → bool
    }
    students.append(student)

for s in students:
    status = "✅ Active" if s["active"] else "❌ Inactive"
    print(f"👤 {s['name']:<10} Age:{s['age']:>3}  Score:{s['score']:>5.1f}  {status}")
```

---

## 🔬 type() and isinstance()

```python
# type() → tells exact type
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type([1,2,3]))     # <class 'list'>
print(type(None))        # <class 'NoneType'>

# Compare types
x = 42
print(type(x) == int)    # True
print(type(x) == str)    # False

# isinstance() → checks if it's that type (or a subtype)
print(isinstance(42, int))         # True ✅
print(isinstance(42, (int, float))) # True ✅ (checks both!)
print(isinstance(True, int))       # True 😲 (bool IS a subclass of int!)
print(isinstance(True, bool))      # True

# 💡 isinstance() is preferred over type() ==
def process(value):
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, (int, float)):
        return value * 2
    else:
        return f"Unknown type: {type(value)}"

print(process("hello"))    # HELLO
print(process(21))         # 42
print(process(3.14))       # 6.28
```

---

## 🧠 How Python Stores Variables (References!)

This is the **deep understanding** part. 🧠

In Python, variables don't hold values directly. They hold **references** (like a pointer to where the value lives in memory).

```python
# 🏷️ Think of it like this:
x = [1, 2, 3]
# Python creates a list object in memory: [1, 2, 3]  📦
# x is a NAME TAG attached to that object            🏷️ → 📦
```

### 🔍 id() — See the memory address

```python
x = [1, 2, 3]
y = x            # y points to the SAME list!

print(id(x))     # e.g., 140234567890
print(id(y))     # SAME number! Same object!
print(x is y)    # True — same object in memory

# Modifying through y also changes x! 😱
y.append(4)
print(x)         # [1, 2, 3, 4]   ← x changed too!
print(y)         # [1, 2, 3, 4]
```

```
Memory:
  x ──→ 📦 [1, 2, 3, 4]
  y ──↗
```

```python
# ✅ To make an INDEPENDENT copy:
x = [1, 2, 3]
y = x.copy()       # or: y = list(x) or y = x[:]

y.append(4)
print(x)    # [1, 2, 3]    ← x unchanged ✅
print(y)    # [1, 2, 3, 4]
```

### 🔒 Integers and Strings are safe (immutable)

```python
a = 10
b = a       # b points to same 10

b = 20      # b now points to a NEW 20, a is untouched
print(a)    # 10  ← safe! ✅
print(b)    # 20
```

```
Before b = 20:    After b = 20:
  a → 📦 10         a → 📦 10
  b → 📦 10         b → 📦 20  (new object)
```

### 🧠 Python caches small integers! (Fun fact)

```python
# Python pre-creates objects for -5 to 256 (implementation detail)
a = 100
b = 100
print(a is b)    # True  (same cached object)

a = 1000
b = 1000
print(a is b)    # False (new objects created)

# ⚠️ Always use == to compare values, 'is' for identity
print(a == b)    # True  ✅ (same VALUE)
print(a is b)    # False ❌ (different objects)
```

---

## 🏗️ Mutable vs Immutable

| Type | Mutable? | Can Change? |
|------|----------|-------------|
| `int` | ❌ Immutable | No |
| `float` | ❌ Immutable | No |
| `str` | ❌ Immutable | No |
| `bool` | ❌ Immutable | No |
| `tuple` | ❌ Immutable | No |
| `list` | ✅ Mutable | Yes |
| `dict` | ✅ Mutable | Yes |
| `set` | ✅ Mutable | Yes |

```python
# ❌ String is immutable — can't change characters in place
name = "Alice"
name[0] = "B"    # TypeError: 'str' object does not support item assignment

# ✅ But you CAN reassign the whole variable
name = "B" + name[1:]   # creates a new string "Blice"
print(name)             # Blice

# ✅ List is mutable — change in place!
items = [1, 2, 3]
items[0] = 99    # works!
print(items)     # [99, 2, 3]
```

---

## 🎩 Multiple Assignment Tricks

```python
# 📌 Assign same value to multiple variables
x = y = z = 0
print(x, y, z)     # 0 0 0

# 📌 Assign multiple values in one line
a, b, c = 1, 2, 3
print(a, b, c)     # 1 2 3

# 📌 Swap values (no temp variable needed!)
a, b = 10, 20
a, b = b, a
print(a, b)        # 20 10

# 📌 Unpack from a list/tuple
coords = [10, 20, 30]
x, y, z = coords
print(x, y, z)     # 10 20 30

# 📌 Ignore values with _
_, important, _ = (1, 42, 3)
print(important)   # 42

# 📌 Augmented assignment (shorthand)
n = 10
n += 5    # n = n + 5   → 15
n -= 3    # n = n - 3   → 12
n *= 2    # n = n * 2   → 24
n //= 5   # n = n // 5  → 4
n **= 3   # n = n ** 3  → 64
n %= 10   # n = n % 10  → 4
```

---

## 📝 Quick Reference Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢 int
age    = 25
x      = age ** 2       # power
y      = age // 7       # floor divide
z      = age % 7        # remainder

# 💧 float
pi     = 3.14159
r      = round(pi, 2)   # 3.14
import math
s      = math.sqrt(16)  # 4.0

# 📝 str
name   = "Alice"
upper  = name.upper()           # ALICE
words  = "a,b,c".split(",")     # ['a','b','c']
joined = "-".join(words)        # a-b-c
found  = "py" in "python"       # True
msg    = f"Hi {name}!"          # Hi Alice!

# ✅ bool
flag   = True
flip   = not flag               # False
check  = 5 > 3 and 2 < 4       # True

# 📋 list
nums   = [3, 1, 4, 1, 5]
nums.append(9)
nums.sort()
total  = sum(nums)
unique = list(set(nums))

# 🔒 tuple
point  = (3, 7)
x, y   = point                  # unpack

# 🎯 set
s1     = {1, 2, 3}
s2     = {3, 4, 5}
common = s1 & s2                # {3}
all_   = s1 | s2                # {1,2,3,4,5}

# 🔑 dict
data   = {"key": "value"}
data["new_key"] = 99
val    = data.get("missing", 0) # safe get
for k, v in data.items():
    print(k, v)

# 🚫 None
x      = None
if x is None:
    print("empty!")

# 🔄 Type conversion
int("42")        # 42
float("3.14")    # 3.14
str(100)         # "100"
bool(0)          # False
list("abc")      # ['a','b','c']
set([1,1,2,2])   # {1,2}

# 🔬 Type checking
type(42)                         # <class 'int'>
isinstance(42, (int, float))     # True
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎓 Final Summary

```
Variable = a name that points to a value in memory 🏷️ → 📦

int     → whole numbers            42, -7, 0
float   → decimal numbers          3.14, -0.5
str     → text                     "Hello", 'World'
bool    → true or false            True, False
list    → ordered, changeable      [1, 2, 3]
tuple   → ordered, fixed           (1, 2, 3)
set     → unique items             {1, 2, 3}
dict    → key-value pairs          {"name": "Alice"}
None    → nothing / absent         None

Mutable   → list, dict, set    (can change in place)
Immutable → int, float, str,
            bool, tuple        (creates new object)
```

---