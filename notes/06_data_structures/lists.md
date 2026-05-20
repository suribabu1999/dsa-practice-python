# 📋 Python Lists — Zero to Advanced (Complete Notes)

> **"Lists are Python's most versatile data structure — master them and you master Python!"**

---

## 📌 Table of Contents

1. [What is a List?](#what-is-a-list)
2. [Creating Lists](#creating-lists)
3. [Accessing Elements](#accessing-elements)
4. [Slicing](#slicing)
5. [Modifying Lists](#modifying-lists)
6. [All List Methods](#all-list-methods)
7. [Looping Through Lists](#looping-through-lists)
8. [List Comprehensions](#list-comprehensions)
9. [Nested Lists](#nested-lists)
10. [List Operations](#list-operations)
11. [Copying Lists](#copying-lists)
12. [Sorting & Reversing](#sorting--reversing)
13. [Advanced Techniques](#advanced-techniques)
14. [Lists vs Other Data Structures](#lists-vs-other-data-structures)
15. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## 🤔 What is a List?

A **list** is an **ordered**, **mutable**, **indexed** collection that can hold **any data type** — including mixed types.

```python
my_list = [1, "hello", 3.14, True, None, [1, 2]]
#          ^    ^        ^     ^     ^      ^
#         int  str    float  bool  None   list  ← mixed types allowed!
```

### ✅ Key Properties

| Property    | Meaning                                   |
|-------------|-------------------------------------------|
| ✅ Ordered   | Items maintain insertion order            |
| ✅ Mutable   | Can be changed after creation             |
| ✅ Indexed   | Access items by position (starts at 0)    |
| ✅ Duplicates| Same value can appear multiple times      |
| ✅ Mixed     | Any combination of data types             |

---

## 🏗️ Creating Lists

### Basic Creation
```python
# Empty list
empty = []
empty2 = list()

# With values
numbers = [1, 2, 3, 4, 5]
names   = ["Alice", "Bob", "Carol"]
mixed   = [1, "two", 3.0, True, None]

# Single item (not a tuple!)
single = [42]
```

### From Other Data Types
```python
# From string → list of characters
chars = list("Python")
print(chars)  # ['P', 'y', 't', 'h', 'o', 'n']

# From range
nums = list(range(1, 11))
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(range(0, 20, 2))
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# From tuple
t = (1, 2, 3)
lst = list(t)  # [1, 2, 3]

# From set (order not guaranteed)
s = {3, 1, 2}
lst = list(s)  # [1, 2, 3] or any order

# From dictionary keys
d = {"a": 1, "b": 2, "c": 3}
keys   = list(d)          # ['a', 'b', 'c']
values = list(d.values()) # [1, 2, 3]
items  = list(d.items())  # [('a', 1), ('b', 2), ('c', 3)]
```

### Pre-filled Lists
```python
# Repeat a value
zeros    = [0] * 5      # [0, 0, 0, 0, 0]
defaults = [None] * 3   # [None, None, None]

# Using list comprehension (covered later)
squares  = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
```

---

## 🎯 Accessing Elements

### Positive Indexing (left → right, starts at 0)
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#           0         1         2        3          4

print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[4])   # elderberry
```

### Negative Indexing (right → left, starts at -1)
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#           -5        -4        -3       -2         -1

print(fruits[-1])  # elderberry  ← last element
print(fruits[-2])  # date
print(fruits[-5])  # apple       ← same as fruits[0]
```

### Index Diagram
```
 fruits = ["apple", "banana", "cherry", "date", "elderberry"]
            +idx:      0         1         2       3        4
            -idx:     -5        -4        -3      -2       -1
```

### Safe Access
```python
fruits = ["apple", "banana", "cherry"]

# ❌ Index out of range
# print(fruits[10])  # IndexError!

# ✅ Safe way
index = 10
if index < len(fruits):
    print(fruits[index])
else:
    print("Index out of range")

# ✅ Using try/except
try:
    print(fruits[10])
except IndexError:
    print("No such index!")
```

---

## ✂️ Slicing

Extract a **sub-list** using `list[start:stop:step]`

```
list[start : stop : step]
      ^        ^      ^
   include  exclude  jump
```

### Basic Slicing
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])    # [2, 3, 4, 5]     ← index 2 to 5
print(nums[:4])     # [0, 1, 2, 3]     ← from start to 3
print(nums[6:])     # [6, 7, 8, 9]     ← from 6 to end
print(nums[:])      # [0,1,2,3,4,5,6,7,8,9] ← full copy
```

### With Step
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[::2])    # [0, 2, 4, 6, 8]  ← every 2nd item
print(nums[1::2])   # [1, 3, 5, 7, 9]  ← odd indices
print(nums[::3])    # [0, 3, 6, 9]     ← every 3rd item
print(nums[::-1])   # [9,8,7,6,5,4,3,2,1,0] ← REVERSED! 🔥
print(nums[8:2:-1]) # [8, 7, 6, 5, 4, 3] ← reverse slice
```

### Negative Slicing
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[-3:])    # [7, 8, 9]   ← last 3
print(nums[:-3])    # [0,1,2,3,4,5,6] ← everything except last 3
print(nums[-5:-2])  # [5, 6, 7]
```

### Slice to Modify
```python
nums = [0, 1, 2, 3, 4, 5]

nums[1:4] = [10, 20, 30]
print(nums)  # [0, 10, 20, 30, 4, 5]

nums[1:4] = []  # delete a slice
print(nums)  # [0, 4, 5]
```

---

## ✏️ Modifying Lists

```python
fruits = ["apple", "banana", "cherry"]

# Change a single item
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Change multiple items via slice
fruits[0:2] = ["avocado", "blackberry"]
print(fruits)  # ['avocado', 'blackberry', 'cherry']

# Delete an item
del fruits[0]
print(fruits)  # ['blackberry', 'cherry']

# Delete a slice
nums = [1, 2, 3, 4, 5]
del nums[1:3]
print(nums)  # [1, 4, 5]
```

---

## 🔧 All List Methods

Python lists have **11 built-in methods**. Here's every single one:

---

### 1️⃣ `append(item)` — Add to End

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Append any type
fruits.append(42)
fruits.append([1, 2])   # Adds the list as ONE element
print(fruits)  # ['apple', 'banana', 'cherry', 42, [1, 2]]
```

---

### 2️⃣ `insert(index, item)` — Add at Specific Position

```python
fruits = ["apple", "banana", "cherry"]

fruits.insert(1, "avocado")   # Insert at index 1
print(fruits)  # ['apple', 'avocado', 'banana', 'cherry']

fruits.insert(0, "FIRST")     # Insert at beginning
print(fruits)  # ['FIRST', 'apple', 'avocado', 'banana', 'cherry']

fruits.insert(100, "LAST")    # Large index → goes to end
print(fruits)  # [..., 'LAST']
```

---

### 3️⃣ `extend(iterable)` — Add Multiple Items

```python
fruits = ["apple", "banana"]

fruits.extend(["cherry", "date"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# Extend with any iterable
fruits.extend("kiwi")          # Adds each character!
print(fruits)  # [..., 'k', 'i', 'w', 'i']

fruits.extend(range(3))        # Adds 0, 1, 2
print(fruits)  # [..., 0, 1, 2]

# 🆚 append vs extend
a = [1, 2]
b = [1, 2]

a.append([3, 4])   # [[3, 4]] added as ONE item → [1, 2, [3, 4]]
b.extend([3, 4])   # each item added separately → [1, 2, 3, 4]
```

---

### 4️⃣ `remove(item)` — Remove First Occurrence

```python
nums = [1, 2, 3, 2, 4, 2]

nums.remove(2)      # Removes FIRST occurrence of 2
print(nums)  # [1, 3, 2, 4, 2]

# ❌ ValueError if item not found
# nums.remove(99)   # ValueError!

# ✅ Safe removal
item = 99
if item in nums:
    nums.remove(item)
else:
    print(f"{item} not found")
```

---

### 5️⃣ `pop(index=-1)` — Remove and Return Item

```python
fruits = ["apple", "banana", "cherry", "date"]

last = fruits.pop()       # Remove & return LAST item
print(last)    # date
print(fruits)  # ['apple', 'banana', 'cherry']

second = fruits.pop(1)    # Remove & return index 1
print(second)  # banana
print(fruits)  # ['apple', 'cherry']

# ❌ IndexError if empty or bad index
# [].pop()  # IndexError!
```

---

### 6️⃣ `clear()` — Remove All Items

```python
nums = [1, 2, 3, 4, 5]

nums.clear()
print(nums)   # []
print(len(nums))  # 0

# 🆚 clear() vs reassign
a = [1, 2, 3]
b = a           # b points to same list

a.clear()       # Clears in-place — b also becomes []
print(b)        # []

a = [1, 2, 3]
b = a
a = []          # Reassign — b still has [1, 2, 3]
print(b)        # [1, 2, 3]
```

---

### 7️⃣ `index(item, start, end)` — Find Position

```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

print(fruits.index("banana"))        # 1 (first occurrence)
print(fruits.index("banana", 2))     # 3 (search from index 2)
print(fruits.index("banana", 2, 5))  # 3 (search in range 2-4)

# ❌ ValueError if not found
# fruits.index("mango")  # ValueError!

# ✅ Safe lookup
item = "mango"
if item in fruits:
    print(fruits.index(item))
else:
    print(f"'{item}' not found")
```

---

### 8️⃣ `count(item)` — Count Occurrences

```python
nums = [1, 2, 3, 2, 4, 2, 5, 2]

print(nums.count(2))   # 4
print(nums.count(9))   # 0 (no error if not found)
print(nums.count(1))   # 1

# Count in nested structures
data = [[1, 2], [3, 4], [1, 2]]
print(data.count([1, 2]))  # 2

# Find most frequent element
from collections import Counter
nums = [1, 2, 2, 3, 3, 3, 4]
most_common = max(set(nums), key=nums.count)
print(most_common)  # 3
```

---

### 9️⃣ `sort(key=None, reverse=False)` — Sort In-Place

```python
# Sort numbers
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort descending
nums.sort(reverse=True)
print(nums)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort strings (alphabetical)
words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']

# Sort by length
words.sort(key=len)
print(words)  # ['date', 'apple', 'banana', 'cherry']

# Sort by last character
words.sort(key=lambda w: w[-1])
print(words)  # sorted by last char

# Sort list of dicts
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob",   "gpa": 3.5},
    {"name": "Carol", "gpa": 3.9},
]
students.sort(key=lambda s: s["gpa"], reverse=True)
print([s["name"] for s in students])  # ['Carol', 'Alice', 'Bob']

# Sort by multiple keys
data = [(2, "b"), (1, "c"), (1, "a")]
data.sort(key=lambda x: (x[0], x[1]))
print(data)  # [(1, 'a'), (1, 'c'), (2, 'b')]
```

---

### 🔟 `reverse()` — Reverse In-Place

```python
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)  # [5, 4, 3, 2, 1]

words = ["hello", "world"]
words.reverse()
print(words)  # ['world', 'hello']

# 🆚 reverse() vs [::-1]
a = [1, 2, 3]
a.reverse()         # Modifies in-place, returns None
b = [1, 2, 3][::-1] # Returns new reversed list
```

---

### 1️⃣1️⃣ `copy()` — Shallow Copy

```python
original = [1, 2, 3, 4, 5]

copy1 = original.copy()
copy1.append(99)

print(original)  # [1, 2, 3, 4, 5] ← unchanged!
print(copy1)     # [1, 2, 3, 4, 5, 99]

# ⚠️ Shallow copy — nested lists still linked!
original = [1, [2, 3], 4]
copy1 = original.copy()
copy1[1].append(99)

print(original)  # [1, [2, 3, 99], 4] ← inner list CHANGED!
print(copy1)     # [1, [2, 3, 99], 4]
```

---

## 🔁 Looping Through Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic for loop
for fruit in fruits:
    print(fruit)

# With index — enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry

# While loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Loop with zip (two lists together)
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 95
# Bob: 87
# Carol: 92

# Reverse loop
for fruit in reversed(fruits):
    print(fruit)

# Loop with index (reversed)
for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])
```

---

## 💡 List Comprehensions

A concise way to create lists — **one of Python's most powerful features!**

```
[expression  for  item  in  iterable  if  condition]
      ^        ^    ^         ^              ^
   what to   loop  var    loop over       filter
   produce
```

### Basic Comprehensions
```python
# Squares of 0-9
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Double each number
nums    = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]
print(doubled)  # [2, 4, 6, 8, 10]

# Uppercase all words
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)  # ['HELLO', 'WORLD', 'PYTHON']

# Length of each word
lengths = [len(w) for w in words]
print(lengths)  # [5, 5, 6]
```

### With Conditions (Filtering)
```python
# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Words longer than 4 chars
words = ["hi", "hello", "hey", "howdy", "yo"]
long_words = [w for w in words if len(w) > 3]
print(long_words)  # ['hello', 'howdy']

# Filter and transform together
nums = [-3, -2, -1, 0, 1, 2, 3]
positive_squares = [x**2 for x in nums if x > 0]
print(positive_squares)  # [1, 4, 9]
```

### With if-else (No Filtering, Just Transformation)
```python
# Label numbers as even/odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# Absolute values
nums = [-3, -1, 0, 2, -5]
abs_vals = [x if x >= 0 else -x for x in nums]
print(abs_vals)  # [3, 1, 0, 2, 5]
```

### Nested Comprehensions
```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplication table (list of lists)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# [3, 6, 9, 12, 15]
# ...

# Cartesian product
colors = ["red", "blue"]
sizes  = ["S", "M", "L"]
combos = [(c, s) for c in colors for s in sizes]
print(combos)
# [('red', 'S'), ('red', 'M'), ..., ('blue', 'L')]
```

---

## 🗂️ Nested Lists (2D Lists / Matrices)

```python
# Creating a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements → matrix[row][col]
print(matrix[0][0])  # 1  (top-left)
print(matrix[1][2])  # 6  (row 1, col 2)
print(matrix[2][2])  # 9  (bottom-right)

# Iterating
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9

# Get a full row
print(matrix[1])      # [4, 5, 6]

# Get a full column
col = [row[1] for row in matrix]
print(col)  # [2, 5, 8]

# Transpose a matrix
transpose = [[matrix[j][i] for j in range(len(matrix))]
             for i in range(len(matrix[0]))]
print(transpose)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Modify an element
matrix[1][1] = 99
print(matrix[1])  # [4, 99, 6]
```

---

## ⚙️ List Operations

```python
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation
print(a + b)        # [1, 2, 3, 4, 5, 6]

# Repetition
print(a * 3)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Length
print(len(a))       # 3

# Membership
print(2 in a)       # True
print(9 not in a)   # True

# Min, Max, Sum
nums = [3, 1, 4, 1, 5, 9]
print(min(nums))    # 1
print(max(nums))    # 9
print(sum(nums))    # 23

# Comparison
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2] < [1, 3])         # True (element-by-element)

# Check if empty
lst = []
if not lst:
    print("List is empty!")

# Unpack into variables
a, b, c = [1, 2, 3]

# Extended unpacking (Python 3+)
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*init, last = [1, 2, 3, 4, 5]
print(init)   # [1, 2, 3, 4]
print(last)   # 5

first, *mid, last = [1, 2, 3, 4, 5]
print(first, mid, last)  # 1 [2, 3, 4] 5
```

---

## 🧬 Copying Lists

```python
original = [1, 2, 3]

# ❌ Wrong — just creates another reference
ref = original
ref.append(99)
print(original)  # [1, 2, 3, 99]  ← also changed!

# ✅ Shallow copy methods (3 ways — all equivalent)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1.append(100)
print(original)  # unchanged

# ⚠️ Shallow copy pitfall with nested lists
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)   # [[1, 2, 99], [3, 4]] ← inner list shared!

# ✅ Deep copy — fully independent copy
import copy
nested   = [[1, 2], [3, 4]]
deep     = copy.deepcopy(nested)
deep[0].append(99)
print(nested)   # [[1, 2], [3, 4]] ← untouched ✅
print(deep)     # [[1, 2, 99], [3, 4]]
```

---

## 🔤 Sorting & Reversing

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# --- sort() vs sorted() ---
# sort()   → modifies IN-PLACE, returns None
# sorted() → returns NEW list, original unchanged

nums.sort()                    # in-place
print(nums)  # [1, 1, 2, 3, 4, 5, 6, 9]

original = [3, 1, 4, 1, 5, 9]
new_sorted = sorted(original)  # new list
print(original)    # [3, 1, 4, 1, 5, 9] unchanged
print(new_sorted)  # [1, 1, 3, 4, 5, 9]

# Descending
print(sorted(original, reverse=True))  # [9, 5, 4, 3, 1, 1]

# Sort strings case-insensitively
words = ["Banana", "apple", "Cherry"]
words.sort(key=str.lower)
print(words)  # ['apple', 'Banana', 'Cherry']

# --- reverse() vs reversed() vs [::-1] ---
nums = [1, 2, 3, 4, 5]
nums.reverse()                      # In-place, returns None
rev1 = list(reversed([1,2,3,4,5]))  # Returns iterator → convert to list
rev2 = [1, 2, 3, 4, 5][::-1]       # New list via slice
```

---

## 🚀 Advanced Techniques

### 🔥 Zip & Unzip
```python
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
grades = ["A", "B", "A"]

# Zip
zipped = list(zip(names, scores, grades))
print(zipped)  # [('Alice', 95, 'A'), ('Bob', 87, 'B'), ('Carol', 92, 'A')]

# Unzip using * (splat)
n, s, g = zip(*zipped)
print(list(n))  # ['Alice', 'Bob', 'Carol']
print(list(s))  # [95, 87, 92]
```

### 🔥 Enumerate
```python
items = ["a", "b", "c"]
indexed = list(enumerate(items, start=1))
print(indexed)  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 🔥 Flatten a List
```python
# Shallow flatten (one level deep)
nested = [[1, 2], [3, 4], [5, 6]]
flat   = [x for sublist in nested for x in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# Using itertools for any depth
import itertools
flat2 = list(itertools.chain.from_iterable(nested))
print(flat2)  # [1, 2, 3, 4, 5, 6]
```

### 🔥 Remove Duplicates (Preserve Order)
```python
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Using dict.fromkeys (preserves order, Python 3.7+)
unique = list(dict.fromkeys(nums))
print(unique)  # [3, 1, 4, 5, 9, 2, 6]

# Using set (does NOT preserve order)
unique2 = list(set(nums))
print(unique2)  # unpredictable order
```

### 🔥 Find Index of All Occurrences
```python
nums = [1, 2, 3, 2, 4, 2, 5]

all_indices = [i for i, x in enumerate(nums) if x == 2]
print(all_indices)  # [1, 3, 5]
```

### 🔥 Rotate a List
```python
nums = [1, 2, 3, 4, 5]

# Rotate right by 2
n = 2
rotated = nums[-n:] + nums[:-n]
print(rotated)  # [4, 5, 1, 2, 3]

# Rotate left by 2
rotated_left = nums[n:] + nums[:n]
print(rotated_left)  # [3, 4, 5, 1, 2]
```

### 🔥 Chunk a List
```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3

chunks = [data[i:i+size] for i in range(0, len(data), size)]
print(chunks)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 🔥 Transpose with zip
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [list(row) for row in zip(*matrix)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### 🔥 Group Elements
```python
from itertools import groupby

data = [1, 1, 2, 2, 2, 3, 1, 1]
groups = [(k, list(v)) for k, v in groupby(data)]
print(groups)
# [(1, [1, 1]), (2, [2, 2, 2]), (3, [3]), (1, [1, 1])]
```

### 🔥 Most/Least Common Element
```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
c    = Counter(nums)

print(c.most_common(1))    # [(4, 4)] — most common: 4 appears 4 times
print(c.most_common())     # All, sorted by frequency
print(c.most_common()[:-2:-1])  # Least common
```

### 🔥 List to String
```python
words = ["Hello", "World", "Python"]

print(" ".join(words))      # Hello World Python
print("-".join(words))      # Hello-World-Python
print("".join(words))       # HelloWorldPython

# Numbers → must convert to string first
nums = [1, 2, 3, 4, 5]
print(", ".join(map(str, nums)))  # 1, 2, 3, 4, 5
```

### 🔥 Filter with filter()
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6, 8, 10]

# Remove None/falsy values
data = [1, None, 2, "", 3, False, 4, 0]
clean = list(filter(None, data))
print(clean)  # [1, 2, 3, 4]
```

### 🔥 Accumulative Operations
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
total   = reduce(lambda x, y: x + y, nums)  # 15
product = reduce(lambda x, y: x * y, nums)  # 120
print(total, product)

# Running sum
from itertools import accumulate
running = list(accumulate(nums))
print(running)  # [1, 3, 6, 10, 15]
```

---

## 📊 Lists vs Other Data Structures

| Feature         | List `[]`  | Tuple `()` | Set `{}`   | Dict `{k:v}` |
|-----------------|------------|------------|------------|--------------|
| Ordered         | ✅         | ✅         | ❌         | ✅ (3.7+)    |
| Mutable         | ✅         | ❌         | ✅         | ✅           |
| Duplicates      | ✅         | ✅         | ❌         | Keys: ❌     |
| Indexed         | ✅         | ✅         | ❌         | By key only  |
| Use when        | General    | Fixed data | Unique vals| Key-value    |

---

## 📋 Quick Cheat Sheet

```python
# ── CREATE ────────────────────────────────────────────────────
[]                      # Empty list
[1, 2, 3]               # With values
list(range(5))          # [0, 1, 2, 3, 4]
[0] * 5                 # [0, 0, 0, 0, 0]
[x**2 for x in range(5)] # List comprehension

# ── ACCESS ────────────────────────────────────────────────────
lst[0]      # First
lst[-1]     # Last
lst[1:4]    # Slice
lst[::-1]   # Reverse

# ── METHODS ───────────────────────────────────────────────────
lst.append(x)       # Add to end
lst.insert(i, x)    # Add at index
lst.extend(iter)    # Add many
lst.remove(x)       # Remove first x
lst.pop(i)          # Remove & return at i
lst.clear()         # Remove all
lst.index(x)        # Find position
lst.count(x)        # Count occurrences
lst.sort()          # Sort in-place
lst.reverse()       # Reverse in-place
lst.copy()          # Shallow copy

# ── OPERATIONS ────────────────────────────────────────────────
len(lst)            # Length
sum(lst)            # Sum
min(lst)            # Minimum
max(lst)            # Maximum
sorted(lst)         # New sorted list
reversed(lst)       # Reverse iterator
x in lst            # Membership check
lst1 + lst2         # Concatenate
lst * 3             # Repeat

# ── USEFUL PATTERNS ───────────────────────────────────────────
list(set(lst))                          # Remove duplicates
[x for x in lst if condition]           # Filter
[f(x) for x in lst]                    # Transform
[x for row in matrix for x in row]     # Flatten
lst[i:i+n] for i in range(0, len, n)  # Chunk
```

---

## 🧠 Memory Tip — All 11 Methods

```
A — append()   → Add one item to end
I — insert()   → Insert at position
E — extend()   → Extend with many items

R — remove()   → Remove first match
P — pop()      → Pop & return item
C — clear()    → Clear everything

I — index()    → Index of item
C — count()    → Count occurrences

S — sort()     → Sort in-place
R — reverse()  → Reverse in-place
C — copy()     → Copy the list

"AIE RPC ICSR C" → A I E | R P C | I C | S R C
```

