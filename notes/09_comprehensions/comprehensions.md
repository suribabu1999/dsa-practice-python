# 🐍 Python Comprehensions — Zero to Hero
## Every Type · Every Concept · Every Trick · Advanced Mastery

> 🧠 **What is a Comprehension?**
> A comprehension is Python's elegant way of building a collection
> in a **single, readable line** — combining a loop and optionally
> a filter into one clean expression.
>
> ```python
> # Without comprehension (4 lines)  😴
> squares = []
> for x in range(10):
>     squares.append(x**2)
>
> # With comprehension (1 line)  🚀
> squares = [x**2 for x in range(10)]
> ```
>
> That's the magic. And it goes MUCH deeper. Let's go! 💪

---

## 📚 Table of Contents

1. [The Core Anatomy](#-the-core-anatomy)
2. [List Comprehensions](#-list-comprehensions)
   - Basic
   - With Filter (if)
   - if-else (ternary)
   - Nested loops
   - Nested comprehensions
   - With functions
   - String processing
   - Multiple filters
   - Walrus operator
3. [Dictionary Comprehensions](#-dictionary-comprehensions)
   - Basic
   - From two lists
   - Filtering dicts
   - Flipping keys/values
   - Nested dict comp
   - Grouping data
4. [Set Comprehensions](#-set-comprehensions)
   - Basic
   - Filtering
   - Set operations via comp
   - Deduplication patterns
5. [Generator Expressions](#-generator-expressions)
   - Basic
   - Memory comparison
   - Chaining generators
   - With any/all/sum/max/min
   - Infinite generators
6. [Tuple Comprehensions?](#-tuple-comprehensions--spoiler-theres-no-such-thing)
7. [Comprehension Internals — How Python Runs Them](#-comprehension-internals--how-python-runs-them)
8. [Nested Comprehensions — The Deep End](#-nested-comprehensions--the-deep-end)
   - 2D matrix operations
   - Flatten any depth
   - Cartesian products
   - Pascal's triangle
   - Spiral matrix
9. [Conditional Comprehensions — Every Pattern](#-conditional-comprehensions--every-pattern)
10. [Comprehensions with Functions](#-comprehensions-with-functions)
11. [Comprehension vs Loop — When to Use Which](#-comprehension-vs-loop--when-to-use-which)
12. [Real-World Advanced Projects](#-real-world-advanced-projects)
13. [Performance Deep Dive](#-performance-deep-dive)
14. [Common Mistakes](#-common-mistakes)
15. [Cheat Sheet](#-cheat-sheet)

---

## 🔬 The Core Anatomy

> Every comprehension shares the same DNA:

```
[ expression   for   variable   in   iterable   if   condition ]
     ↑               ↑               ↑               ↑
  WHAT to          NAME of        WHERE to       FILTER
  produce          each item      get items      (optional)
```

```python
# All four comprehension types — same structure, different wrapper:

[  expr for x in it if cond ]   # List       → [1, 4, 9, ...]
{  expr for x in it if cond }   # Set        → {1, 4, 9, ...}
(  expr for x in it if cond )   # Generator  → <generator object>
{ k: v for x in it if cond }   # Dict       → {'a': 1, 'b': 2, ...}
#   ↑
# dict needs KEY: VALUE expression
```

```python
# Reading a comprehension — say it in English!
# [x**2 for x in range(10) if x % 2 == 0]
# →  "Give me x-squared, for each x in 0-9, but only if x is even"
# →  [0, 4, 16, 36, 64]
```

---

## 📋 LIST Comprehensions

---

### 🟢 Basic — Expression + Loop

```python
# Syntax:  [expression  for  var  in  iterable]
```

```python
# ─── Squares ───
squares = [x**2 for x in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ─── Cubes ───
cubes = [x**3 for x in range(1, 6)]
print(cubes)
# [1, 8, 27, 64, 125]

# ─── Double each item ───
nums    = [3, 7, 2, 9, 1]
doubled = [n * 2 for n in nums]
print(doubled)
# [6, 14, 4, 18, 2]

# ─── Convert to uppercase ───
words  = ["hello", "world", "python", "rocks"]
upper  = [w.upper() for w in words]
print(upper)
# ['HELLO', 'WORLD', 'PYTHON', 'ROCKS']

# ─── Get lengths ───
lengths = [len(w) for w in words]
print(lengths)
# [5, 5, 6, 5]

# ─── From a string ───
chars = [c for c in "Python"]
print(chars)
# ['P', 'y', 't', 'h', 'o', 'n']

# ─── Celsius to Fahrenheit ───
celsius    = [0, 10, 20, 30, 37, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)
# [32.0, 50.0, 68.0, 86.0, 98.6, 212.0]

# ─── From range with math ───
harmonic = [1/n for n in range(1, 6)]
print(harmonic)
# [1.0, 0.5, 0.333..., 0.25, 0.2]
```

---

### 🟡 With Filter — if condition

```python
# Syntax:  [expression  for  var  in  iterable  if  condition]
```

```python
# ─── Even numbers ───
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ─── Positive numbers only ───
data     = [3, -1, 4, -1, 5, -9, 2, -6]
positive = [x for x in data if x > 0]
print(positive)
# [3, 4, 5, 2]

# ─── Long words only ───
words = ["cat", "elephant", "ox", "giraffe", "ant", "hippopotamus"]
long  = [w for w in words if len(w) > 5]
print(long)
# ['elephant', 'giraffe', 'hippopotamus']

# ─── Filter and transform together ───
nums    = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result  = [x**2 for x in nums if x % 3 == 0]   # square multiples of 3
print(result)
# [9, 36, 81]

# ─── Filter strings ───
data    = ["  alice  ", "", "  ", "BOB", "", "charlie  "]
cleaned = [s.strip().title() for s in data if s.strip()]
print(cleaned)
# ['Alice', 'Bob', 'Charlie']

# ─── Prime numbers ───
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

primes = [n for n in range(2, 50) if is_prime(n)]
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# ─── Filter by type ───
mixed  = [1, "hello", 3.14, True, None, [1,2], "world", 42]
strs   = [x for x in mixed if isinstance(x, str)]
nums   = [x for x in mixed if isinstance(x, (int, float)) and not isinstance(x, bool)]
print(strs)    # ['hello', 'world']
print(nums)    # [1, 3.14, 42]
```

---

### 🔵 if-else — Ternary in Comprehension

```python
# Syntax:  [value_if_true  if  condition  else  value_if_false  for  var  in  iterable]
#  Note:   ← ternary goes BEFORE the for, regular if goes AFTER! ←
```

```python
# ─── Label each number ───
nums   = [1, -3, 4, -2, 0, 7, -1]
labels = ["pos" if n > 0 else "neg" if n < 0 else "zero" for n in nums]
print(labels)
# ['pos', 'neg', 'pos', 'neg', 'zero', 'pos', 'neg']

# ─── Pass/Fail ───
scores  = [88, 45, 72, 91, 55, 63, 38]
results = ["✅ Pass" if s >= 60 else "❌ Fail" for s in scores]
for s, r in zip(scores, results):
    print(f"  {s:3}  →  {r}")

# ─── Replace negatives with 0 (clamp) ───
data   = [5, -2, 8, -1, 0, 3, -7]
clamped = [x if x >= 0 else 0 for x in data]
print(clamped)
# [5, 0, 8, 0, 0, 3, 0]

# ─── Classify temperatures ───
temps = [15, 28, 35, 8, 22, 40, -2, 30]
tags  = [
    "🥵 Hot"     if t >= 30 else
    "☀️ Warm"    if t >= 20 else
    "🌤 Pleasant" if t >= 10 else
    "❄️ Cold"
    for t in temps
]
for t, tag in zip(temps, tags):
    print(f"  {t:3}°C  {tag}")

# ─── Normalize: even → x/2, odd → x*3+1 ───
nums    = range(1, 11)
result  = [x // 2 if x % 2 == 0 else x * 3 + 1 for x in nums]
print(result)
# [4, 1, 10, 2, 16, 3, 22, 4, 28, 5]
```

---

### 🟣 Nested Loops in Comprehension

```python
# Syntax:  [expr  for  x  in  outer  for  y  in  inner]
# This is equivalent to:
#   for x in outer:
#       for y in inner:
#           result.append(expr)
```

```python
# ─── Cartesian product ───
colors = ["red", "blue", "green"]
sizes  = ["S", "M", "L", "XL"]

combos = [f"{color}-{size}" for color in colors for size in sizes]
print(combos)
# ['red-S','red-M','red-L','red-XL','blue-S','blue-M',...]
print(f"Total combos: {len(combos)}")   # 12 = 3 × 4

# ─── Pairs from two lists ───
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
pairs = [(a, b) for a in nums1 for b in nums2]
print(pairs)
# [(1,10),(1,20),(1,30),(2,10),(2,20),(2,30),(3,10),(3,20),(3,30)]

# ─── Filtered pairs ───
pairs_filtered = [(a, b) for a in range(1, 5) for b in range(1, 5) if a != b]
print(pairs_filtered)
# [(1,2),(1,3),(1,4),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3)]

# ─── Flatten a 2D list ───
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [n for row in matrix for n in row]
print(flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ─── All combinations of suits and ranks (Deck of cards!) ───
suits  = ["♠️", "♥️", "♦️", "♣️"]
ranks  = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
deck   = [f"{rank}{suit}" for suit in suits for rank in ranks]
print(f"Deck has {len(deck)} cards")     # 52
print(deck[:5])   # ['A♠️', '2♠️', '3♠️', '4♠️', '5♠️']

# ─── Multiplication table as flat list ───
table = [i * j for i in range(1, 6) for j in range(1, 6)]
print(table)
# [1,2,3,4,5, 2,4,6,8,10, 3,6,9,12,15, 4,8,12,16,20, 5,10,15,20,25]
```

---

### 🔴 Nested Comprehensions (List of Lists)

```python
# A comprehension INSIDE a comprehension
# Outer produces rows, inner produces items within each row
```

```python
# ─── 2D matrix of zeros ───
rows, cols = 3, 4
grid = [[0 for _ in range(cols)] for _ in range(rows)]
print(grid)
# [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# ─── Identity matrix ───
n        = 4
identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for row in identity:
    print(row)
# [1, 0, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]

# ─── Multiplication table (matrix) ───
size  = 5
table = [[i * j for j in range(1, size+1)] for i in range(1, size+1)]
for row in table:
    print("  " + "  ".join(f"{n:3}" for n in row))
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25

# ─── Transpose a matrix ───
matrix     = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
# [[1,4,7],[2,5,8],[3,6,9]]

# ─── Pascal's Triangle ───
def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row  = [1] + [prev[j]+prev[j+1] for j in range(len(prev)-1)] + [1]
        triangle.append(row)
    return triangle

for row in pascal(7):
    print("  " + "   ".join(f"{n:3}" for n in row).center(60))

# ─── Zigzag matrix ───
n      = 4
zigzag = [[i*n + j + 1 if i%2==0 else i*n + (n-j)
           for j in range(n)] for i in range(n)]
for row in zigzag:
    print(row)
# [1, 2, 3, 4]
# [8, 7, 6, 5]
# [9, 10, 11, 12]
# [16, 15, 14, 13]
```

---

### 🟠 With Functions

```python
# ─── Apply built-in functions ───
words = ["hello", "WORLD", "Python", "ROCKS"]

titles    = [w.title()     for w in words]
lowers    = [w.lower()     for w in words]
uppers    = [w.upper()     for w in words]
lengths   = [len(w)        for w in words]
reversed_ = [w[::-1]       for w in words]

print(titles)    # ['Hello', 'World', 'Python', 'Rocks']
print(reversed_) # ['olleh', 'DLROW', 'nohtyP', 'SKCOR']

# ─── Apply custom functions ───
def grade(score):
    if score >= 90: return "A+"
    if score >= 80: return "A"
    if score >= 70: return "B"
    if score >= 60: return "C"
    return "F"

scores = [92, 85, 67, 78, 55, 91, 73]
grades = [grade(s) for s in scores]
print(grades)
# ['A+', 'A', 'C', 'B', 'F', 'A+', 'B']

# ─── Apply lambda ───
transform = lambda x: x**2 - 2*x + 1   # (x-1)²
result    = [transform(x) for x in range(-3, 4)]
print(result)
# [16, 9, 4, 1, 0, 1, 4]

# ─── Map equivalent ───
nums      = [1, 2, 3, 4, 5]
# map() style:
mapped    = list(map(lambda x: x**2, nums))
# comprehension style (more readable!):
comp      = [x**2 for x in nums]
# both give [1, 4, 9, 16, 25]

# ─── Filter equivalent ───
# filter() style:
filtered  = list(filter(lambda x: x % 2 == 0, nums))
# comprehension style:
comp_filt = [x for x in nums if x % 2 == 0]
# both give [2, 4]
```

---

### 🔶 String Processing

```python
# ─── Extract digits from string ───
text   = "abc123def456ghi789"
digits = [c for c in text if c.isdigit()]
print(digits)       # ['1','2','3','4','5','6','7','8','9']
print("".join(digits))  # 123456789

# ─── Extract words longer than 4 chars ───
sentence = "The quick brown fox jumps over the lazy dog"
long_words = [w for w in sentence.split() if len(w) > 4]
print(long_words)
# ['quick', 'brown', 'jumps']

# ─── Vowels from text ───
text   = "Hello World"
vowels = [c for c in text.lower() if c in "aeiou"]
print(vowels)   # ['e', 'o', 'o']

# ─── Caesar cipher decode ───
encoded = "Khoor Zruog"
decoded = [
    chr((ord(c) - ord('A') - 3) % 26 + ord('A')) if c.isupper() else
    chr((ord(c) - ord('a') - 3) % 26 + ord('a')) if c.islower() else c
    for c in encoded
]
print("".join(decoded))   # Hello World

# ─── Clean and tokenize sentences ───
sentences = [
    "  Hello,  World!  ",
    "Python  is   awesome!!",
    "  Learn    comprehensions.  "
]

tokens = [
    word.strip(".,!?")
    for sentence in sentences
    for word in sentence.split()
    if word.strip(".,!? ")
]
print(tokens)
# ['Hello', 'World', 'Python', 'is', 'awesome', 'Learn', 'comprehensions']
```

---

### 🔷 Multiple Conditions

```python
# ─── Multiple if conditions (AND logic) ───
# All conditions must be True:
nums = range(1, 51)

# Divisible by both 3 AND 5
fizzbuzz_nums = [n for n in nums if n % 3 == 0 if n % 5 == 0]
print(fizzbuzz_nums)
# [15, 30, 45]
# (same as:  if n % 3 == 0 and n % 5 == 0)

# ─── FizzBuzz as labels ───
fb = [
    "FizzBuzz" if n % 15 == 0 else
    "Fizz"     if n % 3  == 0 else
    "Buzz"     if n % 5  == 0 else
    str(n)
    for n in range(1, 21)
]
print(fb)
# ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz',
#  '11','Fizz','13','14','FizzBuzz','16','17','Fizz','19','Buzz']

# ─── Filter with multiple criteria ───
products = [
    {"name": "Laptop",  "price": 75000, "stock": 5,   "category": "Electronics"},
    {"name": "Phone",   "price": 25000, "stock": 0,   "category": "Electronics"},
    {"name": "Shirt",   "price": 1500,  "stock": 20,  "category": "Clothing"},
    {"name": "Tablet",  "price": 35000, "stock": 8,   "category": "Electronics"},
    {"name": "Jeans",   "price": 2500,  "stock": 0,   "category": "Clothing"},
    {"name": "Headset", "price": 5000,  "stock": 15,  "category": "Electronics"},
]

# In-stock electronics under ₹40,000
available = [
    p["name"]
    for p in products
    if p["stock"] > 0
    if p["category"] == "Electronics"
    if p["price"] < 40000
]
print(available)
# ['Tablet', 'Headset']
```

---

### 🟤 Walrus Operator := (Python 3.8+)

> The walrus operator `:=` assigns AND uses a value in one step!
> Powerful for avoiding repeated computation inside comprehensions.

```python
# ─── Compute once, use in both expression and condition ───

# Without walrus — computing twice! 😩
results = [expensive(x) for x in data if expensive(x) > threshold]

# With walrus — compute ONCE! 😎
results = [y for x in data if (y := expensive(x)) > threshold]
```

```python
# ─── Real example: filter and keep computed results ───
import math

nums    = range(-5, 11)

# Keep only those where sqrt is valid AND > 2
valids  = [root
           for n in nums
           if n >= 0 and (root := round(math.sqrt(n), 2)) > 2]
print(valids)
# [2.24, 2.45, 2.65, 2.83, 3.0, 3.16, 3.32, 3.46, 3.61, 3.74]

# ─── Parse and filter in one pass ───
raw = ["42", "hello", "17", "world", "99", "3.14", "5"]

def try_int(s):
    try:    return int(s)
    except: return None

ints = [n for s in raw if (n := try_int(s)) is not None]
print(ints)
# [42, 17, 99, 5]

# ─── Fibonacci with walrus ───
a, b = 0, 1
fibs = [(a := b, b := a + b, a)[2]   # last item is new 'a' value
        for _ in range(10)]
# (Advanced — mostly for show; regular loop is clearer here!)
```

---

---

## 📖 DICTIONARY Comprehensions

```python
# Syntax:  {key_expr: value_expr  for  var  in  iterable  if  condition}
```

---

### 🟢 Basic Dict Comprehension

```python
# ─── Squares as dict ───
squares = {x: x**2 for x in range(1, 8)}
print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# ─── String lengths ───
words   = ["apple", "banana", "cherry", "kiwi"]
lengths = {word: len(word) for word in words}
print(lengths)
# {'apple': 5, 'banana': 6, 'cherry': 6, 'kiwi': 4}

# ─── Cube roots ───
cubes   = {x**3: x for x in range(1, 6)}
print(cubes)
# {1: 1, 8: 2, 27: 3, 64: 4, 125: 5}

# ─── ASCII codes ───
ascii_map = {c: ord(c) for c in "Python"}
print(ascii_map)
# {'P': 80, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}

# ─── Boolean map ───
items  = ["apple", "banana", "cherry"]
in_cart = {item: False for item in items}
print(in_cart)
# {'apple': False, 'banana': False, 'cherry': False}
```

---

### 🟡 From Two Lists (zip)

```python
# ─── Basic zip → dict ───
keys   = ["name", "age", "city"]
values = ["Alice", 25, "Mumbai"]
profile = {k: v for k, v in zip(keys, values)}
print(profile)
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# ─── Product price lookup ───
products = ["apple", "banana", "cherry", "mango"]
prices   = [40, 25, 80, 120]
catalog  = {product: price for product, price in zip(products, prices)}
print(catalog)
# {'apple': 40, 'banana': 25, 'cherry': 80, 'mango': 120}

# ─── Score lookup ───
names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [88, 92, 75, 95]
lookup = {name: score for name, score in zip(names, scores)}
print(lookup["Charlie"])   # 75

# ─── Enumerate → dict ───
items  = ["first", "second", "third", "fourth"]
indexed = {i: item for i, item in enumerate(items, start=1)}
print(indexed)
# {1: 'first', 2: 'second', 3: 'third', 4: 'fourth'}
```

---

### 🟠 Filtering Dicts

```python
# ─── Filter by value ───
inventory = {"apple": 50, "banana": 0, "cherry": 30, "mango": 0, "kiwi": 15}

in_stock  = {item: qty for item, qty in inventory.items() if qty > 0}
print(in_stock)
# {'apple': 50, 'cherry': 30, 'kiwi': 15}

low_stock = {item: qty for item, qty in inventory.items() if 0 < qty < 20}
print(low_stock)
# {'kiwi': 15}

# ─── Filter by key ───
data      = {"name": "Alice", "_id": 42, "age": 25, "_secret": "xyz", "city": "Mumbai"}
public    = {k: v for k, v in data.items() if not k.startswith("_")}
print(public)
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# ─── Filter by type ───
mixed     = {"a": 1, "b": "hello", "c": 3.14, "d": True, "e": [1,2], "f": 42}
nums_only = {k: v for k, v in mixed.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
print(nums_only)
# {'a': 1, 'c': 3.14, 'f': 42}

# ─── Conditional value transformation ───
prices   = {"apple": 40, "banana": 25, "mango": 120, "cherry": 80}
# Apply 20% discount on items above ₹50
discounted = {
    item: (price * 0.8 if price > 50 else price)
    for item, price in prices.items()
}
print(discounted)
# {'apple': 40, 'banana': 25, 'mango': 96.0, 'cherry': 64.0}
```

---

### 🔵 Flipping Keys and Values

```python
# ─── Basic flip ───
original = {"a": 1, "b": 2, "c": 3}
flipped  = {v: k for k, v in original.items()}
print(flipped)
# {1: 'a', 2: 'b', 3: 'c'}

# ─── Flip country capitals ───
capitals = {
    "India":   "New Delhi",
    "France":  "Paris",
    "Japan":   "Tokyo",
    "Brazil":  "Brasília",
}
by_capital = {city: country for country, city in capitals.items()}
print(by_capital["Paris"])   # France

# ─── Flip word index ───
words     = ["apple", "banana", "cherry"]
index     = {word: i for i, word in enumerate(words)}
reversed_ = {v: k for k, v in index.items()}
print(index)      # {'apple': 0, 'banana': 1, 'cherry': 2}
print(reversed_)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# ⚠️ Warning: flip only works cleanly if values are unique!
# If duplicates exist, some mappings will be lost (last one wins)
dup = {"a": 1, "b": 1, "c": 2}
print({v: k for k, v in dup.items()})   # {1: 'b', 2: 'c'}  ← 'a' is lost!
```

---

### 🟣 Nested Dict Comprehensions

```python
# ─── Dict of dicts ───
subjects  = ["Math", "Science", "English"]
students  = ["Alice", "Bob", "Charlie"]
import random
random.seed(42)

# Each student → each subject → random score
grades = {
    student: {subject: random.randint(60, 100) for subject in subjects}
    for student in students
}
for student, marks in grades.items():
    avg = sum(marks.values()) / len(marks)
    print(f"  {student}: {marks}  avg={avg:.1f}")

# ─── Transform nested dict ───
# Original: {student: {subject: score}}
# Target:   {student: {subject: grade}}
def to_grade(s):
    return "A" if s>=90 else "B" if s>=80 else "C" if s>=70 else "F"

letter_grades = {
    student: {subj: to_grade(score) for subj, score in marks.items()}
    for student, marks in grades.items()
}
print(letter_grades)

# ─── Nested comprehension to build a distance table ───
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai"]
import random; random.seed(1)

# Symmetric distance matrix
distances = {
    city1: {
        city2: (0 if city1 == city2 else random.randint(500, 2000))
        for city2 in cities
    }
    for city1 in cities
}

print(f"\n  {'':12}", end="")
for c in cities: print(f"{c[:6]:>10}", end="")
print()
for c1 in cities:
    print(f"  {c1[:12]:<12}", end="")
    for c2 in cities:
        print(f"{distances[c1][c2]:>10}", end="")
    print()
```

---

### 🔴 Grouping Data

```python
# ─── Group words by first letter ───
words = ["apple","avocado","banana","blueberry","cherry","coconut","date"]
grouped = {
    letter: [w for w in words if w.startswith(letter)]
    for letter in set(w[0] for w in words)
}
print(grouped)
# {'a': ['apple','avocado'], 'b': ['banana','blueberry'],
#  'c': ['cherry','coconut'], 'd': ['date']}

# ─── Group by length ───
words    = ["cat", "dog", "elephant", "ant", "owl", "lion", "bee"]
by_len   = {
    length: [w for w in words if len(w) == length]
    for length in sorted(set(len(w) for w in words))
}
print(by_len)
# {3: ['cat','dog','ant','owl','bee'], 4: ['lion'], 8: ['elephant']}

# ─── Group students by grade ───
students = [
    ("Alice", 92), ("Bob", 75), ("Charlie", 88),
    ("Diana", 91), ("Eve", 65), ("Frank", 55),
    ("Grace", 80), ("Heidi", 73),
]

def grade_band(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

grouped = {
    band: [name for name, score in students if grade_band(score) == band]
    for band in ["A", "B", "C", "D", "F"]
    if any(grade_band(score) == band for _, score in students)
}
print(grouped)
# {'A': ['Alice','Diana'], 'B': ['Charlie','Grace'],
#  'C': ['Bob','Heidi'], 'D': ['Eve'], 'F': ['Frank']}

# ─── Word frequency ───
text  = "the cat sat on the mat the cat wore a hat"
words = text.split()
freq  = {word: words.count(word) for word in set(words)}
# Sort by frequency
freq_sorted = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
print(freq_sorted)
# {'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, ...}
```

---

---

## 🎯 SET Comprehensions

```python
# Syntax:  {expression  for  var  in  iterable  if  condition}
# Returns a SET — unordered, unique items only!
```

---

### 🟢 Basic Set Comprehension

```python
# ─── Squares (duplicates removed automatically!) ───
nums    = [1, -1, 2, -2, 3, -3, 4]
squares = {x**2 for x in nums}
print(squares)
# {1, 4, 9, 16}   ← -1²=1²=1, -2²=2²=4, etc.

# ─── Unique lengths ───
words = ["cat", "dog", "elephant", "ant", "owl", "lion"]
lens  = {len(w) for w in words}
print(lens)
# {3, 4, 8}

# ─── Unique first letters ───
fruits  = ["apple", "avocado", "banana", "blueberry", "cherry"]
firsts  = {f[0] for f in fruits}
print(firsts)
# {'a', 'b', 'c'}

# ─── All factors of numbers 1-10 ───
factors = {factor for n in range(1, 11) for factor in range(1, n+1) if n % factor == 0}
print(sorted(factors))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

### 🟡 Filtering in Set Comprehensions

```python
# ─── Unique even squares ───
even_sq  = {x**2 for x in range(20) if x % 2 == 0}
print(sorted(even_sq))
# [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

# ─── Unique vowels in text ───
text   = "Hello Beautiful World of Python Programming"
vowels = {c.lower() for c in text if c.lower() in "aeiou"}
print(vowels)
# {'a', 'e', 'i', 'o', 'u'}

# ─── Unique domains from emails ───
emails  = [
    "alice@gmail.com", "bob@yahoo.com",
    "carol@gmail.com", "dave@outlook.com",
    "eve@yahoo.com",   "frank@gmail.com",
]
domains = {email.split("@")[1] for email in emails}
print(domains)
# {'gmail.com', 'yahoo.com', 'outlook.com'}

# ─── Unique words (case-insensitive) ───
sentence = "To be or not to Be that is the question To be"
unique   = {word.lower() for word in sentence.split()}
print(sorted(unique))
# ['be', 'is', 'not', 'or', 'question', 'that', 'the', 'to']
```

---

### 🟠 Set Operations via Comprehensions

```python
# ─── Simulate intersection ───
a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}

# Both ways work:
intersection = a & b
comp_intersect = {x for x in a if x in b}
print(intersection)     # {4, 5, 6}
print(comp_intersect)   # {4, 5, 6}

# ─── Common characters in two strings ───
str1 = "Hello Python"
str2 = "Hello World"
common = {c for c in str1 if c in str2 and c != " "}
print(common)
# {'H', 'e', 'l', 'o'}

# ─── Symmetric difference ───
all_but_common = {x for x in a | b if x not in a & b}
print(all_but_common)   # {1, 2, 3, 7, 8, 9}

# ─── Find duplicate values in a list ───
nums = [1, 2, 3, 2, 4, 3, 5, 1, 6]
seen     = set()
dupes    = {x for x in nums if x in seen or seen.add(x)}
print(dupes)
# {1, 2, 3}
```

---

### 🔵 Deduplication Patterns

```python
# ─── Remove duplicate words (case-insensitive) ───
words = ["Python", "python", "PYTHON", "Java", "java", "C++", "c++"]
unique_words = {w.lower() for w in words}
print(unique_words)
# {'python', 'java', 'c++'}

# ─── Unique tuples (order-independent) ───
pairs = [(1,2),(2,1),(3,4),(4,3),(1,2),(5,6)]
unique_pairs = {tuple(sorted(p)) for p in pairs}
print(unique_pairs)
# {(1,2), (3,4), (5,6)}   ← (1,2) and (2,1) treated as same!

# ─── Unique sentences (normalized) ───
sentences = [
    "  Hello World  ",
    "hello world",
    "HELLO WORLD",
    "Python is great",
    "python is great",
]
unique_sentences = {s.strip().lower() for s in sentences}
print(unique_sentences)
# {'hello world', 'python is great'}
```

---

---

## ⚡ GENERATOR Expressions

```python
# Syntax:  (expression  for  var  in  iterable  if  condition)
# Looks like a tuple comp — but it's a GENERATOR (lazy evaluation)!
# Creates items ONE AT A TIME — doesn't store everything in memory!
```

---

### 🟢 Basic Generator Expression

```python
# ─── Create a generator ───
gen = (x**2 for x in range(5))
print(gen)          # <generator object <genexpr> at 0x...>
print(type(gen))    # <class 'generator'>

# ─── Consume with next() ───
print(next(gen))    # 0    ← compute and yield one item
print(next(gen))    # 1
print(next(gen))    # 4
print(next(gen))    # 9
print(next(gen))    # 16
# next(gen)         # StopIteration — exhausted!

# ─── Consume with for loop ───
gen = (x**2 for x in range(5))
for val in gen:
    print(val, end=" ")   # 0 1 4 9 16
```

---

### 🟡 Memory Comparison — Generator vs List

```python
import sys

n = 1_000_000

# List comprehension — stores ALL values in memory
squares_list = [x**2 for x in range(n)]
print(f"List size: {sys.getsizeof(squares_list):>12,} bytes")
# List size:  8,697,464 bytes (~8.7 MB!)

# Generator expression — stores almost NOTHING
squares_gen  = (x**2 for x in range(n))
print(f"Gen  size: {sys.getsizeof(squares_gen):>12,} bytes")
# Gen  size:            104 bytes (just 104 bytes!)

# Same result for sum — but generator uses no extra memory!
total_list = sum(squares_list)   # sum of pre-computed list
total_gen  = sum(x**2 for x in range(n))   # compute on the fly
print(total_list == total_gen)   # True
```

---

### 🟠 With Aggregation Functions

```python
# Generators shine when used DIRECTLY inside built-in functions!
# No need to wrap in list() — they accept iterables directly.

data    = range(1, 1001)

total   = sum(x for x in data)
avg     = sum(x for x in data) / 1000
maximum = max(x**2 for x in data)
minimum = min(abs(x - 500) for x in data)

print(f"Sum:  {total}")      # 500500
print(f"Avg:  {avg}")        # 500.5
print(f"Max²: {maximum}")    # 1000000
print(f"Closest to 500: {minimum}")   # 0

# ─── any() and all() with generators (SHORT-CIRCUIT!) ───
nums = range(1, 100001)

# any() stops at FIRST True — very fast!
has_large = any(x > 99999 for x in nums)
print(has_large)    # True — stopped immediately at 100000

# all() stops at FIRST False — very fast!
all_pos   = all(x > 0 for x in nums)
print(all_pos)      # True

all_even  = all(x % 2 == 0 for x in nums)
print(all_even)     # False — stopped at first odd (x=1)!
```

---

### 🔵 Chaining Generators

```python
# ─── Generator pipeline ───
# Each generator feeds into the next — zero memory overhead!

raw_data  = range(1, 101)

# Step 1: filter evens
evens     = (x for x in raw_data if x % 2 == 0)

# Step 2: square them
squared   = (x**2 for x in evens)

# Step 3: keep only those > 1000
large     = (x for x in squared if x > 1000)

# Step 4: consume
result    = list(large)
print(result)
# [1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, ...]

# ─── Equivalent one-liner generator ───
result2 = list(x**2 for x in range(1,101) if x%2==0 if x**2>1000)
```

---

### 🟣 Generator with itertools

```python
from itertools import chain, islice, takewhile, dropwhile

# ─── chain: combine multiple iterables lazily ───
gen = chain(
    (x**2 for x in range(5)),
    (x**3 for x in range(5))
)
print(list(gen))
# [0, 1, 4, 9, 16, 0, 1, 8, 27, 64]

# ─── islice: take first N items from generator ───
squares_gen = (x**2 for x in range(10**9))   # "infinite" source
first_10    = list(islice(squares_gen, 10))
print(first_10)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ─── takewhile: take while condition is True ───
nums    = (x for x in range(1, 100))
small   = list(takewhile(lambda x: x < 10, nums))
print(small)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ─── dropwhile: skip while condition is True ───
nums    = (x for x in range(1, 10))
rest    = list(dropwhile(lambda x: x < 5, nums))
print(rest)
# [5, 6, 7, 8, 9]
```

---

---

## 🫙 Tuple Comprehensions? (Spoiler: There's No Such Thing!)

```python
# ⚠️ ( ) creates a GENERATOR, not a tuple!
gen  = (x**2 for x in range(5))
print(type(gen))    # <class 'generator'>  ← NOT a tuple!

# ✅ To get a tuple, wrap with tuple():
tup  = tuple(x**2 for x in range(5))
print(tup)          # (0, 1, 4, 9, 16)
print(type(tup))    # <class 'tuple'>

# ─── Why? ─── 
# (expr) is already used for grouping in Python
# (expr,) would be a one-item tuple
# So Python chose () for generators, not tuples

# ─── Practical tuple "comprehension" patterns ───
squares   = tuple(x**2 for x in range(10))
evens     = tuple(x for x in range(20) if x % 2 == 0)
processed = tuple(s.upper() for s in ["a","b","c"])

print(squares)    # (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
print(evens)      # (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
print(processed)  # ('A', 'B', 'C')
```

---

---

## 🔬 Comprehension Internals — How Python Runs Them

```python
# Python compiles comprehensions into their OWN scope (like a function!)
# This means variables inside don't leak out.

# In Python 2 (old — leaked!):
# [x for x in range(5)]
# print(x)   # worked! → 4

# In Python 3 (fixed — no leak!):
result = [x for x in range(5)]
# print(x)   # NameError — x doesn't exist outside!

# The variable ONLY exists inside the comprehension.
```

```python
# ─── Each comprehension has its own scope ───
x = 100   # outer x

result = [x**2 for x in range(5)]   # inner x: 0,1,2,3,4
print(result)   # [0, 1, 4, 9, 16]
print(x)        # 100   ← outer x untouched!
```

```python
# ─── Comprehensions vs loops — what Python actually does ───

# This comprehension:
result = [x**2 for x in range(5)]

# Is roughly equivalent to:
def _comp():
    _result = []
    for x in range(5):
        _result.append(x**2)
    return _result
result = _comp()

# That's why:
# 1. Comprehensions are slightly FASTER (optimized C loop internally)
# 2. Variables DON'T leak out
# 3. They have a closure (can access outer variables)
```

```python
# ─── Accessing outer variables (closure) ───
threshold = 5    # outer variable

filtered = [x for x in range(20) if x > threshold]   # uses outer 'threshold'
print(filtered)
# [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

---

---

## 🌊 Nested Comprehensions — The Deep End

---

### Matrix Operations

```python
# ─── Matrix addition ───
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
print(C)
# [[10,10,10],[10,10,10],[10,10,10]]

# ─── Matrix multiplication ───
def mat_mul(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B         = len(B[0])
    return [
        [sum(A[i][k] * B[k][j] for k in range(cols_A)) for j in range(cols_B)]
        for i in range(rows_A)
    ]

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(mat_mul(A, B))
# [[19, 22], [43, 50]]

# ─── Element-wise operations ───
matrix  = [[1,2,3],[4,5,6],[7,8,9]]

# All squared
squared = [[x**2 for x in row] for row in matrix]
# Row sums
row_sums = [sum(row) for row in matrix]
# Col sums
col_sums = [sum(matrix[r][c] for r in range(3)) for c in range(3)]

print(row_sums)   # [6, 15, 24]
print(col_sums)   # [12, 15, 18]
```

---

### Flatten Any Depth

```python
# ─── Flatten 2D ───
nested_2d = [[1,2,3],[4,5,6],[7,8,9]]
flat_2d   = [x for row in nested_2d for x in row]
print(flat_2d)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ─── Flatten 3D ───
nested_3d = [[[1,2],[3,4]],[[5,6],[7,8]]]
flat_3d   = [x for layer in nested_3d for row in layer for x in row]
print(flat_3d)
# [1, 2, 3, 4, 5, 6, 7, 8]

# ─── Recursive flatten (any depth) using generator ───
def flatten(item):
    if isinstance(item, (list, tuple)):
        for sub in item:
            yield from flatten(sub)
    else:
        yield item

deep   = [1, [2, [3, [4, [5]]]]]
result = list(flatten(deep))
print(result)   # [1, 2, 3, 4, 5]
```

---

### Advanced Patterns

```python
# ─── Sieve of Eratosthenes as comprehension ───
def sieve_comp(limit):
    is_composite = {j for i in range(2, int(limit**0.5)+1) for j in range(i*i, limit+1, i)}
    return [n for n in range(2, limit+1) if n not in is_composite]

print(sieve_comp(50))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# ─── All unique pairs that sum to a target ───
nums   = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
pairs  = [(a, b) for i, a in enumerate(nums) for b in nums[i+1:] if a + b == target]
print(pairs)
# [(1, 9), (2, 8), (3, 7), (4, 6)]

# ─── Power set (all subsets) ───
from itertools import combinations

def power_set(lst):
    return [list(combo)
            for r in range(len(lst) + 1)
            for combo in combinations(lst, r)]

print(power_set([1, 2, 3]))
# [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

# ─── Anagram groups ───
words = ["eat","tea","tan","ate","nat","bat","listen","silent","enlist"]
sorted_words = {word: "".join(sorted(word)) for word in words}
anagram_groups = {
    key: [w for w in words if "".join(sorted(w)) == key]
    for key in set(sorted_words.values())
    if [w for w in words if "".join(sorted(w)) == key].__len__() > 1
}
print(anagram_groups)
# {'aet': ['eat','tea','ate'], 'ant': ['tan','nat'], 'eilnst': ['listen','silent','enlist']}
```

---

---

## 🔀 Conditional Comprehensions — Every Pattern

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Pattern 1: FILTER only  (if at end)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
evens   = [x for x in range(10) if x % 2 == 0]

# Pattern 2: TRANSFORM only  (no if)
squares = [x**2 for x in range(10)]

# Pattern 3: FILTER + TRANSFORM  (both)
sq_evens = [x**2 for x in range(10) if x % 2 == 0]

# Pattern 4: TERNARY transform  (if-else before for)
labeled = ["even" if x%2==0 else "odd" for x in range(10)]

# Pattern 5: TERNARY + FILTER  (both positions)
result  = [x**2 if x>0 else 0 for x in range(-5,6) if x != -3]

# Pattern 6: MULTIPLE FILTERS  (chained ifs = AND)
result  = [x for x in range(100) if x%2==0 if x%3==0]   # multiples of 6

# Pattern 7: NESTED TERNARY  (3 outcomes)
classify = [
    "big"    if x > 100 else
    "medium" if x > 10  else
    "small"
    for x in [5, 15, 50, 200, 8, 150]
]
print(classify)
# ['small', 'medium', 'medium', 'big', 'small', 'big']

# Pattern 8: FILTER on outer AND inner loop
pairs = [
    (x, y)
    for x in range(1, 6)  if x % 2 != 0       # outer filter: odd x
    for y in range(1, 6)  if y > x             # inner filter: y > x
]
print(pairs)
# [(1,2),(1,3),(1,4),(1,5),(3,4),(3,5),(5, — nothing)]
```

---

---

## 🔧 Comprehensions with Functions

```python
# ─── Lambda ───
double    = lambda x: x * 2
result    = [double(x) for x in range(5)]
print(result)    # [0, 2, 4, 6, 8]

# ─── Custom function ───
def normalize(text):
    return text.strip().lower().replace(" ", "_")

fields = ["  First Name ", " Last Name", " EMAIL ADDRESS "]
keys   = [normalize(f) for f in fields]
print(keys)
# ['first_name', 'last_name', 'email_address']

# ─── Function that returns tuple — unpack in comprehension ───
def stats(lst):
    return min(lst), max(lst), sum(lst)/len(lst)

datasets = [[3,1,4,1,5], [9,2,6,5,3], [2,7,1,8,2]]
results  = [stats(d) for d in datasets]
for lo, hi, avg in results:
    print(f"  min={lo}  max={hi}  avg={avg:.1f}")

# ─── Applying multiple transformations with reduce-like pattern ───
from functools import reduce

pipeline = [str.strip, str.lower, str.title]
texts    = ["  HELLO ", " world  ", "  PYTHON ROCKS  "]
cleaned  = [
    reduce(lambda s, fn: fn(s), pipeline, text)
    for text in texts
]
print(cleaned)
# ['Hello', 'World', 'Python Rocks']
```

---

---

## 🏆 Real-World Advanced Projects

---

### Project 1 — Data Pipeline (ETL)

```python
# Extract, Transform, Load using comprehensions

raw_records = [
    "1,Alice,  Engineering ,95000,Active",
    "2,Bob,  MARKETING,72000,inactive",
    "3,Charlie,Engineering,88000,ACTIVE",
    "4,,HR,65000,active",          # missing name
    "5,Eve,Engineering,invalid,Active",  # invalid salary
    "6,Frank,Marketing,102000,Active",
]

def safe_int(s):
    try:    return int(s.strip())
    except: return None

# 1. Parse
parsed = [line.split(",") for line in raw_records]

# 2. Validate & clean
clean = [
    {
        "id"        : int(row[0]),
        "name"      : row[1].strip().title(),
        "dept"      : row[2].strip().title(),
        "salary"    : safe_int(row[3]),
        "active"    : row[4].strip().lower() == "active",
    }
    for row in parsed
    if len(row) == 5
    if row[1].strip()                      # name not empty
    if safe_int(row[3]) is not None        # salary valid
]

# 3. Transform: add grade, categorize salary
final = [
    {**emp,
     "salary_band": "Senior" if emp["salary"] >= 90000
                    else "Mid"    if emp["salary"] >= 70000
                    else "Junior"
    }
    for emp in clean
    if emp["active"]    # only active employees
]

# 4. Report
print(f"  {'ID'} {'Name':<12} {'Dept':<15} {'Salary':>8}  {'Band'}")
print("  " + "─" * 55)
for e in final:
    print(f"  {e['id']}  {e['name']:<12} {e['dept']:<15} ₹{e['salary']:>7,}  {e['salary_band']}")

# Summary by dept
depts = {e["dept"] for e in final}
print("\n  📊 Department Summary:")
for dept in sorted(depts):
    dept_emp = [e for e in final if e["dept"] == dept]
    avg_sal  = sum(e["salary"] for e in dept_emp) / len(dept_emp)
    print(f"     {dept:<15} {len(dept_emp)} staff  avg ₹{avg_sal:,.0f}")
```

---

### Project 2 — Text Analyzer

```python
import re
from collections import Counter

text = """
Python is an interpreted high-level general-purpose programming language.
Python's design philosophy emphasizes code readability.
Its language constructs and object-oriented approach aim to help programmers
write clear, logical code for small and large-scale projects.
Python is dynamically typed and garbage-collected.
"""

# All words, cleaned
words     = [w.lower() for w in re.findall(r'\b[a-zA-Z]+\b', text)]

# Unique words
unique    = {w for w in words}

# Word lengths frequency
len_freq  = {length: [w for w in unique if len(w) == length]
             for length in sorted({len(w) for w in unique})}

# Stop words removal
stopwords = {"is","an","and","to","its","for","the","a","of","in","aim"}
keywords  = [w for w in words if w not in stopwords and len(w) > 3]

# Frequency dict
freq      = {word: keywords.count(word) for word in set(keywords)}
top10     = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10])

# Bigrams (consecutive word pairs)
bigrams   = [(words[i], words[i+1]) for i in range(len(words)-1)]
bigram_freq = {bg: bigrams.count(bg) for bg in set(bigrams) if bigrams.count(bg) > 1}

print("📊 Text Analysis")
print("─" * 40)
print(f"  Total words:    {len(words)}")
print(f"  Unique words:   {len(unique)}")
print(f"  Avg word len:   {sum(len(w) for w in words)/len(words):.1f}")
print(f"\n  🔝 Top Keywords:")
for word, count in top10.items():
    print(f"     {word:<15} {count}x  {'█'*count}")
```

---

### Project 3 — Matrix Math Library

```python
# Pure comprehension-based matrix operations!

def zeros(r, c):
    return [[0]*c for _ in range(r)]

def identity(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def transpose(M):
    return [[M[r][c] for r in range(len(M))] for c in range(len(M[0]))]

def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(M, k):
    return [[x*k for x in row] for row in M]

def multiply(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]

def flatten(M):
    return [x for row in M for x in row]

def trace(M):
    return sum(M[i][i] for i in range(min(len(M), len(M[0]))))

def pretty(M, name=""):
    if name: print(f"  {name}:")
    for row in M:
        print("  [" + "  ".join(f"{x:4}" for x in row) + " ]")
    print()

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]

pretty(transpose(A),    "Transpose A")
pretty(add(A, B),       "A + B")
pretty(scale(A, 2),     "A × 2")
pretty(multiply(A, B),  "A × B")
print(f"  Trace of A: {trace(A)}")     # 1+5+9 = 15
print(f"  Flat A: {flatten(A)}")
```

---

---

## ⚡ Performance Deep Dive

```python
import timeit

data = list(range(10000))

# ─── List comp vs append loop ───
def with_loop():
    result = []
    for x in data:
        result.append(x**2)
    return result

def with_comp():
    return [x**2 for x in data]

loop_time = timeit.timeit(with_loop, number=1000)
comp_time = timeit.timeit(with_comp, number=1000)
print(f"Loop : {loop_time:.3f}s")
print(f"Comp : {comp_time:.3f}s")
print(f"Comp is {loop_time/comp_time:.1f}x faster!")
# Comp is ~1.5-2x faster!

# ─── Generator vs list for aggregation ───
def list_sum():
    return sum([x**2 for x in range(100000)])

def gen_sum():
    return sum(x**2 for x in range(100000))

# gen_sum uses ~0 extra memory, list_sum uses ~800KB
```

```python
# ─── When NOT to use comprehension ───

# ✅ Good: when logic is simple and readable
evens   = [x for x in range(100) if x%2==0]

# ❌ Bad: when logic is complex (use regular loop!)
# This is hard to read:
result = [
    f(x) if g(x) > threshold else h(x)
    for x in dataset
    if p(x) and q(x)
    for y in sub_data(x)
    if r(y)
]
# Use a regular loop with clear variable names instead!

# Rule of thumb:
# If comprehension doesn't fit on 1-2 lines clearly → use a loop!
```

---

---

## 🚨 Common Mistakes

```python
# ─── Mistake 1: if-else position ───

# ❌ Wrong — SyntaxError!
result = [x**2 for x in range(10) if x%2==0 else x]

# ✅ Correct — ternary goes BEFORE for, filter goes AFTER
result = [x**2 if x%2==0 else x for x in range(10)]   # ternary
result = [x**2 for x in range(10) if x%2==0]          # filter
```

```python
# ─── Mistake 2: Generators are EXHAUSTED after one use ───

gen  = (x**2 for x in range(5))
list1 = list(gen)   # [0, 1, 4, 9, 16]
list2 = list(gen)   # []  ← empty! generator is exhausted!

# ✅ Create fresh generator each time, or use a list
squares = [x**2 for x in range(5)]   # list: reusable!
```

```python
# ─── Mistake 3: Variable leaking (Python 3 fixed this, but know it!) ───

i = 100
result = [i for i in range(5)]
print(i)    # 100  ← i is still 100 (no leak in Python 3)
```

```python
# ─── Mistake 4: Nested comprehension loop ORDER ───

# Reading order = nesting order
# [expr for x in outer for y in inner]
# is the SAME as:
# for x in outer:
#     for y in inner:
#         result.append(expr)

# NOT the same as:
# [[item for item in row] for row in matrix]  ← this is nested comp (2D)
# [item for row in matrix for item in row]    ← this FLATTENS (1D)

matrix = [[1,2,3],[4,5,6]]
nested  = [[x for x in row] for row in matrix]   # [[1,2,3],[4,5,6]]
flat    = [x for row in matrix for x in row]      # [1,2,3,4,5,6]
```

```python
# ─── Mistake 5: Modifying the source while iterating ───

data   = [1, 2, 3, 4, 5]
# ❌ Don't do this — unpredictable behavior
result = [data.pop() for _ in range(3)]
# ✅ Use a copy or just comprehend the values
result = [x for x in data[-3:]]
```

```python
# ─── Mistake 6: dict comprehension duplicate keys ───
pairs  = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
d      = {k: v for k, v in pairs}
print(d)   # {'a': 3, 'b': 4}  ← last value wins!
# If you need all values, group them instead:
grouped = {k: [v for k2,v in pairs if k2==k] for k,_ in pairs}
print(grouped)   # {'a': [1,3], 'b': [2,4]}
```

---

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋  LIST COMPREHENSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[expr for x in it]                    # basic
[expr for x in it if cond]            # filter
[a if cond else b for x in it]        # ternary
[expr for x in it if c1 if c2]        # multiple filters (AND)
[expr for x in o for y in i]          # nested loops (flat)
[[expr for y in i] for x in o]        # nested comp (2D)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📖  DICT COMPREHENSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{k: v for x in it}                    # basic
{k: v for x in it if cond}            # with filter
{v: k for k, v in d.items()}          # flip dict
{k: v for k,v in zip(keys,vals)}      # from two lists
{k: [..] for k in keys}               # group into lists

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎯  SET COMPREHENSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{expr for x in it}                    # basic (unique!)
{expr for x in it if cond}            # with filter

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡  GENERATOR EXPRESSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(expr for x in it)                    # generator (lazy!)
(expr for x in it if cond)            # with filter
sum(expr for x in it)                 # use directly in func
tuple(expr for x in it)               # → tuple
list(expr for x in it)                # → list (same as [])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠  KEY RULES TO REMEMBER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ternary (if-else) goes BEFORE  the for
# filter  (if only) goes AFTER   the for
# nested loops read left-to-right like English
# variables DON'T leak out (Python 3)
# generators are LAZY and EXHAUST after one pass
# dict comp: duplicate keys → last value wins
# () alone = generator, tuple() needed for tuple

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏁  CHOOSE THE RIGHT TYPE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# [...]  → need to index, iterate many times, modify
# {...}  → need uniqueness (set) or key-value (dict)
# (...)  → huge data, use once, pass to sum/any/all
# tuple  → immutable collection from generator
```

---

## 🎓 Final Summary

```
Comprehension anatomy (same for all types):
──────────────────────────────────────────────────────────
[ WHAT   for   WHO   in   WHERE   if   FILTER ]
  ↑             ↑          ↑            ↑
expression    variable   iterable   condition
                                    (optional)

4 Types:
  [expr ...]        → List       ordered, indexed, mutable
  {expr ...}        → Set        unordered, unique, no index
  {k:v ...}         → Dict       key-value pairs
  (expr ...)        → Generator  lazy, one-pass, low memory

If-else positions:
  BEFORE for → transforms  [A if c else B  for x in it]
  AFTER  for → filters     [x              for x in it if c]

Nesting:
  Flat:  [x  for row in M  for x in row]   → 1D list
  2D:    [[x for x in row] for row in M]   → 2D list

Performance:
  Comprehension ≈ 1.5–2× faster than append loop
  Generator     ≈ 0 extra memory for huge datasets

Golden Rule:
  If it doesn't FIT in 2 clean lines → use a regular loop!
  Comprehensions exist for CLARITY, not cleverness.
──────────────────────────────────────────────────────────
```

