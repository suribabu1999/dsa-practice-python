# 🐍 Python Loops — Complete Guide
## From Zero to Patterns & Advanced Mastery

> 🧠 **What is a Loop?**
> A loop says: **"Do this thing again and again"** — until you say stop.
> Without loops, printing 100 lines means writing 100 `print()` statements.
> With loops? Just **3 lines**. That's the magic. 🪄

---

## 📚 Table of Contents

1. [for Loop](#-for-loop)
2. [while Loop](#-while-loop)
3. [break, continue, pass](#-break-continue-pass)
4. [else on Loops](#-else-on-loops)
5. [range() Deep Dive](#-range-deep-dive)
6. [enumerate()](#-enumerate)
7. [zip()](#-zip)
8. [Nested Loops](#-nested-loops)
9. [⭐ STAR PATTERNS](#-star-patterns)
10. [🔢 NUMBER PATTERNS](#-number-patterns)
11. [🔤 ALPHABET PATTERNS](#-alphabet-patterns)
12. [🎨 ADVANCED PATTERNS](#-advanced-patterns)
13. [List Comprehensions](#-list-comprehensions)
14. [Loop Tricks & Idioms](#-loop-tricks--idioms)
15. [Real-World Loop Examples](#-real-world-loop-examples)
16. [Performance Tips](#-performance-tips)
17. [Cheat Sheet](#-cheat-sheet)

---

## 🔁 for Loop

> **"For each item in this collection, do something."**
> Use when you know WHAT you're looping over.

```python
# Syntax
for variable in iterable:
    # body — runs once per item
```

```python
# ─── Loop over a list ───
fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(f"  🍎 {fruit}")

# 🍎 apple
# 🍎 banana
# 🍎 cherry
# 🍎 mango
```

```python
# ─── Loop over a string ───
for char in "Python":
    print(char, end=" → ")
# P → y → t → h → o → n →
```

```python
# ─── Loop over a dict ───
student = {"name": "Alice", "age": 20, "grade": "A"}

for key, value in student.items():
    print(f"  {key:>8} : {value}")
#     name : Alice
#      age : 20
#    grade : A
```

```python
# ─── Loop over a set ───
colors = {"red", "green", "blue", "yellow"}
for color in colors:
    print(f"  🎨 {color}")
# (order varies — sets are unordered)
```

```python
# ─── Loop over a range ───
for i in range(1, 6):
    print(f"  Step {i} ✅")
# Step 1 ✅  Step 2 ✅  Step 3 ✅  Step 4 ✅  Step 5 ✅
```

---

## ⏳ while Loop

> **"Keep going WHILE this condition is True."**
> Use when you DON'T know in advance how many times to loop.

```python
# Syntax
while condition:
    # body — runs as long as condition is True
    # MUST update something or it loops forever!
```

```python
# ─── Basic countdown ───
n = 5
while n > 0:
    print(f"  ⏳ {n}...")
    n -= 1
print("  🚀 Blastoff!")
```

```python
# ─── Input validation (very common!) ───
while True:
    age = input("Enter your age (1-120): ")
    if age.isdigit() and 1 <= int(age) <= 120:
        print(f"  ✅ Age accepted: {age}")
        break
    print("  ⚠️  Invalid! Try again.")
```

```python
# ─── Digit sum (keep dividing until 0) ───
number = 98765
total  = 0

while number > 0:
    total  += number % 10    # grab last digit
    number //= 10            # remove last digit

print(f"  🔢 Digit sum = {total}")   # 35
```

```python
# ─── Collatz Conjecture (loops unknown times) ───
n     = 27
steps = 0

print(n, end=" ")
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(n, end=" ")
    steps += 1

print(f"\n  ✅ Reached 1 in {steps} steps!")
```

---

## 💥 break, continue, pass

```python
# break  → EXIT the loop entirely        💥
# continue → SKIP this iteration, next   ⏭️
# pass   → DO NOTHING, placeholder       🤫
```

```python
# ─── break example ───
for i in range(10):
    if i == 5:
        print(f"  💥 Breaking at {i}")
        break
    print(f"  {i}", end=" ")
# 0 1 2 3 4
# 💥 Breaking at 5
```

```python
# ─── continue example ───
for i in range(10):
    if i % 2 == 0:
        continue    # skip evens
    print(f"  {i}", end=" ")
# 1 3 5 7 9
```

```python
# ─── pass example ───
for i in range(5):
    if i == 3:
        pass        # do nothing special
    print(i, end=" ")
# 0 1 2 3 4   (pass didn't skip anything)
```

```python
# ─── break in while — safe input loop ───
attempts = 3
while attempts > 0:
    pwd = input("🔐 Password: ")
    if pwd == "python123":
        print("  ✅ Correct!")
        break
    attempts -= 1
    print(f"  ❌ Wrong! {attempts} attempts left.")
else:
    print("  🔒 Locked out!")
```

---

## 🔁➕ else on Loops

> The `else` block runs **only if the loop completed without a `break`**.
> Python's unique and powerful feature! 🦄

```python
# ─── Search with for-else ───
primes = [2, 3, 5, 7, 11, 13]
target = 8

for p in primes:
    if p == target:
        print(f"  ✅ {target} is in the list!")
        break
else:
    print(f"  ❌ {target} not found.")
# ❌ 8 not found.
```

```python
# ─── Prime checker using for-else ───
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False   # not prime — break would skip else
    else:
        return True        # loop finished without break → prime!

for n in range(2, 20):
    tag = "🔢 Prime" if is_prime(n) else "      ."
    print(f"  {n:2}  {tag}")
```

---

## 🎰 range() Deep Dive

```python
# range(stop)
# range(start, stop)
# range(start, stop, step)
```

```python
# ─── All forms ───
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(0, 20, 4)))    # [0, 4, 8, 12, 16]
print(list(range(10, 0, -1)))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(0, -10, -2)))  # [0, -2, -4, -6, -8]
```

```python
# ─── Patterns using range ───

# Odd numbers 1–19
odds = list(range(1, 20, 2))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Multiples of 7
mult7 = list(range(7, 71, 7))
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Reverse countdown
for i in range(10, 0, -1):
    print(i, end=" ")
# 10 9 8 7 6 5 4 3 2 1
```

---

## 🏷️ enumerate()

> Loop with **automatic index counter** — clean and Pythonic!

```python
fruits = ["apple", "banana", "cherry"]

# ─── Default (starts at 0) ───
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")
# [0] apple  [1] banana  [2] cherry

# ─── Start from 1 ───
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")
# 1. apple  2. banana  3. cherry
```

```python
# ─── Find position of items ───
scores  = [78, 95, 62, 88, 95, 71]
highest = max(scores)

for i, score in enumerate(scores):
    marker = " ← 🏆 MAX" if score == highest else ""
    print(f"  Student {i+1}: {score}{marker}")

# Student 1: 78
# Student 2: 95 ← 🏆 MAX
# Student 3: 62
# Student 4: 88
# Student 5: 95 ← 🏆 MAX
# Student 6: 71
```

---

## 🤐 zip()

> Loop over **multiple iterables simultaneously**!

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"  👤 {name:<10} | Score: {score} | Grade: {grade}")

# 👤 Alice      | Score: 88 | Grade: B
# 👤 Bob        | Score: 95 | Grade: A
# 👤 Charlie    | Score: 72 | Grade: C
```

```python
# ─── zip to build dict ───
keys   = ["name", "age", "city"]
values = ["Alice", 25, "Mumbai"]

profile = dict(zip(keys, values))
print(profile)
# {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
```

```python
# ─── zip_longest (keep all items) ───
from itertools import zip_longest

a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

for x, y in zip_longest(a, b, fillvalue="—"):
    print(f"  {x}  {y}")
# 1  a
# 2  b
# 3  c
# 4  —
# 5  —
```

---

## 🪆 Nested Loops

> A loop **inside** a loop.
> Inner loop runs **completely** for every single iteration of the outer loop.

```python
# How many times does inner body run?
# outer_iterations × inner_iterations
for i in range(3):      # outer: 3 times
    for j in range(4):  # inner: 4 times each → total 3×4 = 12
        print(f"({i},{j})", end=" ")
    print()

# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
```

---

---

# ⭐ STAR PATTERNS

> Every pattern below uses `end=""` to print on same line,
> and nested loops (or single loops) to control rows and columns.

---

### Pattern 1 — Right Triangle (increasing) ⭐

```python
rows = 6
for i in range(1, rows + 1):
    print("* " * i)

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
```

---

### Pattern 2 — Right Triangle (decreasing) ⭐

```python
rows = 6
for i in range(rows, 0, -1):
    print("* " * i)

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
```

---

### Pattern 3 — Right-Aligned Triangle ⭐

```python
rows = 6
for i in range(1, rows + 1):
    spaces = " " * (rows - i) * 2   # shrinking left padding
    stars  = "* " * i
    print(spaces + stars)

#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * *
```

---

### Pattern 4 — Full Pyramid ⭐

```python
rows = 6
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars  = "* " * i
    print(spaces + stars)

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
```

---

### Pattern 5 — Inverted Pyramid ⭐

```python
rows = 6
for i in range(rows, 0, -1):
    spaces = " " * (rows - i)
    stars  = "* " * i
    print(spaces + stars)

# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
```

---

### Pattern 6 — Diamond ⭐

```python
rows = 6

# Upper half (including middle)
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
```

---

### Pattern 7 — Hollow Square ⭐

```python
rows = 6
for i in range(rows):
    for j in range(rows):
        # print star on border, space inside
        if i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *
```

---

### Pattern 8 — Hollow Triangle ⭐

```python
rows = 7
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *
# * *
# *   *
# *     *
# *       *
# *         *
# * * * * * * *
```

---

### Pattern 9 — Hourglass ⭐

```python
rows = 6

# Upper (decreasing)
for i in range(rows, 0, -1):
    spaces = " " * (rows - i)
    stars  = "* " * i
    print(spaces + stars)

# Lower (increasing)
for i in range(2, rows + 1):
    spaces = " " * (rows - i)
    stars  = "* " * i
    print(spaces + stars)

# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
```

---

### Pattern 10 — Checkerboard ⭐

```python
rows = 6
cols = 10
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *   *   *   *   *
#   *   *   *   *
# *   *   *   *   *
#   *   *   *   *
# *   *   *   *   *
#   *   *   *   *
```

---

### Pattern 11 — Butterfly ⭐

```python
rows = 5

# Upper half
for i in range(1, rows + 1):
    stars  = "*" * i
    spaces = " " * (2 * (rows - i))
    print(stars + spaces + stars)

# Lower half
for i in range(rows, 0, -1):
    stars  = "*" * i
    spaces = " " * (2 * (rows - i))
    print(stars + spaces + stars)

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *
```

---

### Pattern 12 — Spiral Frame ⭐

```python
def spiral_frame(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1:
                print("*", end=" ")
            elif j == 0 or j == n-1:
                print("*", end=" ")
            elif i == 1 or i == n-2:
                if j >= 1 and j <= n-2:
                    print("*" if (j == 1 or j == n-2) else " ", end=" ")
            else:
                print("*" if (j == 1 or j == n-2) else " ", end=" ")
        print()

spiral_frame(7)

# * * * * * * *
# * *       * *
# * * * * * * *
# * *       * *
# * * * * * * *
# * *       * *
# * * * * * * *
```

---

---

# 🔢 NUMBER PATTERNS

---

### Pattern 13 — Number Triangle

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
```

---

### Pattern 14 — Same Number Triangle

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
```

---

### Pattern 15 — Continuous Numbers

```python
rows = 5
num  = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
```

---

### Pattern 16 — Floyd's Triangle

```python
rows = 6
num  = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(f"{num:3}", end="")
        num += 1
    print()

#   1
#   2  3
#   4  5  6
#   7  8  9 10
#  11 12 13 14 15
#  16 17 18 19 20 21
```

---

### Pattern 17 — Pascal's Triangle

```python
rows = 7

def pascal_row(n):
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row

for i in range(rows):
    row    = pascal_row(i)
    spaces = " " * (rows - i - 1) * 2
    nums   = "   ".join(f"{x:3}" for x in row)
    print(spaces + nums)

#                   1
#                1     1
#             1     2     1
#          1     3     3     1
#       1     4     6     4     1
#    1     5    10    10     5     1
# 1     6    15    20    15     6     1
```

---

### Pattern 18 — Number Diamond

```python
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print(j if j <= i else 2 * i - j, end=" ")
    print()

#     1
#    1 2 1
#   1 2 3 2 1
#  1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
#  1 2 3 4 3 2 1
#   1 2 3 2 1
#    1 2 1
#     1
```

---

### Pattern 19 — Multiplication Table Grid

```python
cols = 10

# Header
print("    ", end="")
for j in range(1, cols + 1):
    print(f"{j:4}", end="")
print()
print("    " + "─" * (cols * 4))

for i in range(1, cols + 1):
    print(f"{i:2} |", end="")
    for j in range(1, cols + 1):
        print(f"{i*j:4}", end="")
    print()

#       1   2   3   4   5   6   7   8   9  10
#     ────────────────────────────────────────
#  1 |   1   2   3   4   5   6   7   8   9  10
#  2 |   2   4   6   8  10  12  14  16  18  20
#  ...
```

---

### Pattern 20 — Fibonacci Triangle

```python
def fib_row(n):
    a, b = 0, 1
    row  = []
    for _ in range(n):
        row.append(a)
        a, b = b, a + b
    return row

rows = 7
for i in range(1, rows + 1):
    print(" ".join(f"{x:3}" for x in fib_row(i)))

#   0
#   0   1
#   0   1   1
#   0   1   1   2
#   0   1   1   2   3
#   0   1   1   2   3   5
#   0   1   1   2   3   5   8
```

---

---

# 🔤 ALPHABET PATTERNS

---

### Pattern 21 — Alphabet Triangle (A B C...)

```python
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")   # chr(65)='A'
    print()

# A
# A B
# A B C
# A B C D
# A B C D E
```

---

### Pattern 22 — Same Letter Triangle

```python
rows = 5
for i in range(rows):
    letter = chr(65 + i)
    print((letter + " ") * (i + 1))

# A
# B B
# C C C
# D D D D
# E E E E E
```

---

### Pattern 23 — Alphabet Pyramid

```python
rows = 6
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    letters = ""
    # left side A→current
    for j in range(i):
        letters += chr(65 + j) + " "
    # right side (current-1)→A
    for j in range(i - 2, -1, -1):
        letters += chr(65 + j) + " "
    print(spaces + letters)

#      A
#     A B A
#    A B C B A
#   A B C D C B A
#  A B C D E D C B A
# A B C D E F E D C B A
```

---

### Pattern 24 — Alphabet Diamond

```python
rows = 5

# Upper
for i in range(rows):
    spaces  = " " * (rows - i - 1)
    letters = ""
    for j in range(i + 1):
        letters += chr(65 + j) + " "
    for j in range(i - 1, -1, -1):
        letters += chr(65 + j) + " "
    print(spaces + letters)

# Lower
for i in range(rows - 2, -1, -1):
    spaces  = " " * (rows - i - 1)
    letters = ""
    for j in range(i + 1):
        letters += chr(65 + j) + " "
    for j in range(i - 1, -1, -1):
        letters += chr(65 + j) + " "
    print(spaces + letters)

#     A
#    A B A
#   A B C B A
#  A B C D C B A
# A B C D E D C B A
#  A B C D C B A
#   A B C B A
#    A B A
#     A
```

---

### Pattern 25 — Alphabet Box

```python
rows = 5
for i in range(rows):
    for j in range(rows):
        ch = chr(65 + min(i, j, rows-1-i, rows-1-j))
        print(ch, end=" ")
    print()

# A A A A A
# A B B B A
# A B C B A
# A B B B A
# A A A A A
```

---

---

# 🎨 ADVANCED PATTERNS

---

### Pattern 26 — Sine Wave (ASCII Art)

```python
import math

width  = 60
height = 12

for row in range(height):
    line = ""
    for col in range(width):
        y = math.sin(col * 0.2) * (height / 2 - 1)
        if abs(y - (height / 2 - 1 - row)) < 0.6:
            line += "*"
        else:
            line += " "
    print(line)

#           ***       ***       ***       ***       ***
#         **   **   **   **   **   **   **   **   **   **
#        *       * *       * *       * *       * *
#       *         *         *         *         *
#      *                                         ...
# (smooth sine wave across terminal!)
```

---

### Pattern 27 — Spiral Number Matrix

```python
def spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num; num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num; num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num; num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num; num += 1
        left += 1

    return matrix

n = 5
for row in spiral_matrix(n):
    print("  " + "  ".join(f"{x:2}" for x in row))

#    1  2  3  4  5
#   16 17 18 19  6
#   15 24 25 20  7
#   14 23 22 21  8
#   13 12 11 10  9
```

---

### Pattern 28 — Number Border with Hollow Inside

```python
n = 6
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print(f"{i*j:3}", end="")
        else:
            print("   ", end="")
    print()

#   1  2  3  4  5  6
#   2              12
#   3              18
#   4              24
#   5              30
#   6 12 18 24 30 36
```

---

### Pattern 29 — Zigzag Pattern

```python
rows = 3
cols = 20

for i in range(rows):
    for j in range(cols):
        cond1 = (i == 0 or i == rows - 1) and j % 4 != 0
        cond2 = (0 < i < rows - 1) and j % 4 == (rows - 1 - i) % 4 * (1 if j % 8 < 4 else -1) + 2
        # Simplified clean zigzag:
        zigzag_row = (j % 4) if (j // 4) % 2 == 0 else (3 - j % 4)
        if zigzag_row == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *       *       *       *       *
#   *   *   *   *   *   *   *   *
#     *       *       *       *
```

---

### Pattern 30 — Concentric Squares (Layers)

```python
n = 7    # must be odd for clean center

for i in range(n):
    for j in range(n):
        layer = min(i, j, n-1-i, n-1-j)
        val   = layer + 1
        print(val, end=" ")
    print()

# 1 1 1 1 1 1 1
# 1 2 2 2 2 2 1
# 1 2 3 3 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 3 3 2 1
# 1 2 2 2 2 2 1
# 1 1 1 1 1 1 1
```

---

### Pattern 31 — Cross / Plus Shape

```python
n    = 9     # must be odd
mid  = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#         *
#         *
#         *
#         *
# * * * * * * * * *
#         *
#         *
#         *
#         *
```

---

### Pattern 32 — X Shape

```python
n = 9

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# *               *
#   *           *
#     *       *
#       *   *
#         *
#       *   *
#     *       *
#   *           *
# *               *
```

---

### Pattern 33 — Heart Shape ❤️

```python
def print_heart(size=6):
    for i in range(size // 2, size):
        count = i * 2 - (size // 2 * 2 - 2)
        space = (size * 2 - count) // 2
        print(" " * space + "* " * count)

    for i in range(size, 0, -1):
        count = i * 2 - 1
        space = (size * 2 - count) // 2
        print(" " * space + "* " * count)

print_heart(6)

#       * * * *     * * * *
#     * * * * * * * * * * *
#   * * * * * * * * * * * * *
#     * * * * * * * * * * *
#       * * * * * * * * *
#         * * * * * * *
#           * * * * *
#             * * *
#               *
```

---

### Pattern 34 — Growing and Shrinking (Rhombus)

```python
rows = 5

# Expanding
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * (2 * i - 1))

# Shrinking
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * (2 * i - 1))

#     *
#    * * *
#   * * * * *
#  * * * * * * *
# * * * * * * * * *
#  * * * * * * *
#   * * * * *
#    * * *
#     *
```

---

---

## 💎 List Comprehensions

> Build lists in **one elegant line** — loop + optional filter combined!

```python
# [ expression  for  var  in  iterable  if  condition ]

# Basic
squares   = [x**2 for x in range(1, 11)]
evens     = [x for x in range(20) if x % 2 == 0]
uppercase = [w.upper() for w in ["hello", "world"]]

# With condition on both sides
grades = [85, 40, 92, 55, 78, 61]
result = ["Pass ✅" if g >= 60 else "Fail ❌" for g in grades]

# Nested comprehension (flatten matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat   = [n for row in matrix for n in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Generate multiplication table as dict
table = {(i,j): i*j for i in range(1,4) for j in range(1,4)}
# {(1,1):1, (1,2):2, (1,3):3, (2,1):2 ... (3,3):9}
```

---

## 🪄 Loop Tricks & Idioms

```python
# ─── 1. Reverse a list ───
items = [1, 2, 3, 4, 5]
for item in reversed(items):
    print(item, end=" ")
# 5 4 3 2 1

# ─── 2. sorted() on the fly ───
names = ["Charlie", "Alice", "Bob"]
for name in sorted(names):
    print(name)
# Alice  Bob  Charlie

# ─── 3. Unique items in order ───
data   = [3, 1, 4, 1, 5, 9, 2, 6, 5]
seen   = set()
unique = []
for x in data:
    if x not in seen:
        unique.append(x)
        seen.add(x)
# [3, 1, 4, 5, 9, 2, 6]

# ─── 4. Swap in-place ───
a, b = 10, 20
a, b = b, a
# a=20, b=10

# ─── 5. Unpack in loop ───
pairs = [(1,"a"), (2,"b"), (3,"c")]
for num, letter in pairs:
    print(f"  {num} → {letter}")

# ─── 6. _ for throwaway ───
for _ in range(5):
    print("Hello!")   # don't need the index

# ─── 7. any() / all() with generators ───
nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))   # True — all even
print(any(n > 9      for n in nums))   # True — at least one > 9

# ─── 8. walrus operator := (Python 3.8+) ───
import random
results = []
while (val := random.randint(1, 10)) != 7:
    results.append(val)
print(f"Rolled before 7: {results}")
```

---

## 🌍 Real-World Loop Examples

### Example 1 — Student Report Card

```python
students = [
    {"name": "Alice",   "marks": [88, 92, 76, 95, 83]},
    {"name": "Bob",     "marks": [72, 68, 80, 74, 70]},
    {"name": "Charlie", "marks": [55, 60, 48, 65, 58]},
    {"name": "Diana",   "marks": [98, 95, 99, 97, 100]},
]

def get_grade(avg):
    if avg >= 90: return "A+ 🌟"
    elif avg >= 80: return "A  ⭐"
    elif avg >= 70: return "B  👍"
    elif avg >= 60: return "C  🙂"
    else:           return "F  📚"

print("=" * 55)
print(f"  {'Name':<12} {'Avg':>6}  {'Grade'}  {'Subject Scores'}")
print("=" * 55)

for student in students:
    name   = student["name"]
    marks  = student["marks"]
    avg    = sum(marks) / len(marks)
    grade  = get_grade(avg)
    scores = "  ".join(f"{m:3}" for m in marks)
    print(f"  {name:<12} {avg:>6.1f}  {grade}    {scores}")

print("=" * 55)
```

---

### Example 2 — Caesar Cipher (Encrypt/Decrypt)

```python
def caesar(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base   = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message   = "Hello, Python World!"
encrypted = caesar(message, shift=13)
decrypted = caesar(encrypted, shift=13, decrypt=True)

print(f"  Original  : {message}")
print(f"  Encrypted : {encrypted}")
print(f"  Decrypted : {decrypted}")

# Original  : Hello, Python World!
# Encrypted : Uryyb, Clguba Jbeyq!
# Decrypted : Hello, Python World!
```

---

### Example 3 — Word Frequency Counter

```python
text = """
to be or not to be that is the question
whether tis nobler in the mind to suffer
the slings and arrows of outrageous fortune
"""

words     = text.lower().split()
freq      = {}

for word in words:
    word = word.strip(".,!?;:")
    if word:
        freq[word] = freq.get(word, 0) + 1

# Sort by frequency
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("  📊 Word Frequency (Top 10):")
print("  " + "─" * 30)
for word, count in sorted_freq[:10]:
    bar = "█" * count
    print(f"  {word:<12} {count:2}  {bar}")

# 📊 Word Frequency (Top 10):
# the          3  ███
# to           3  ███
# be           2  ██
# or           1  █
# ...
```

---

### Example 4 — Prime Sieve (Sieve of Eratosthenes)

```python
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False

    return [n for n in range(2, limit+1) if is_prime[n]]

primes = sieve(100)
print(f"  🔢 Primes up to 100 ({len(primes)} found):")

for i, p in enumerate(primes):
    print(f"{p:4}", end="")
    if (i + 1) % 10 == 0:
        print()

#    2   3   5   7  11  13  17  19  23  29
#   31  37  41  43  47  53  59  61  67  71
#   73  79  83  89  97
```

---

### Example 5 — Inventory Stock Manager

```python
inventory = {
    "apple":  {"price": 40,  "stock": 150},
    "banana": {"price": 20,  "stock": 0  },
    "mango":  {"price": 120, "stock": 30 },
    "grape":  {"price": 80,  "stock": 5  },
    "orange": {"price": 50,  "stock": 200},
}

low_stock_threshold = 10

print("  🏪 INVENTORY REPORT")
print("  " + "═" * 45)
print(f"  {'Item':<10} {'Price':>7} {'Stock':>7}  Status")
print("  " + "─" * 45)

out_of_stock = []
low_stock    = []

for item, details in inventory.items():
    price = details["price"]
    stock = details["stock"]

    if stock == 0:
        status = "❌ Out of Stock"
        out_of_stock.append(item)
    elif stock <= low_stock_threshold:
        status = "⚠️  Low Stock"
        low_stock.append(item)
    else:
        status = "✅ Available"

    print(f"  {item.title():<10} ₹{price:>5}  {stock:>6}   {status}")

print("  " + "═" * 45)
if out_of_stock:
    print(f"  🚨 Reorder needed: {', '.join(out_of_stock)}")
if low_stock:
    print(f"  ⚠️  Running low:   {', '.join(low_stock)}")
```

---

## ⚡ Performance Tips

```python
# ─── 1. Use list comp over append loop ───
# Slower ❌
squares = []
for i in range(10000):
    squares.append(i**2)

# Faster ✅
squares = [i**2 for i in range(10000)]


# ─── 2. Use generators for large data ───
# Uses lots of memory ❌
total = sum([i**2 for i in range(10_000_000)])

# Memory-efficient ✅
total = sum(i**2 for i in range(10_000_000))


# ─── 3. Don't call len() every iteration ───
# Calls len() 1000 times ❌
for i in range(len(my_list)):
    ...

# Call once ✅
n = len(my_list)
for i in range(n):
    ...


# ─── 4. enumerate > manual counter ───
# ❌
i = 0
for item in items:
    print(i, item)
    i += 1

# ✅
for i, item in enumerate(items):
    print(i, item)


# ─── 5. 'in' on set is O(1), on list is O(n) ───
# Slow for large lists ❌
bad_words_list = ["spam", "junk", "advert", ...]
if word in bad_words_list:    # O(n) search!
    ...

# Fast always ✅
bad_words_set = {"spam", "junk", "advert", ...}
if word in bad_words_set:     # O(1) search!
    ...
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔁 LOOP TYPES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

for x in iterable:           # iterate items
for i in range(n):           # repeat n times
for i in range(a, b, step):  # custom range
for i, x in enumerate(lst):  # with index
for a, b in zip(l1, l2):     # parallel loop
while condition:              # until false
while True: ... break         # manual exit

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎛️ LOOP CONTROLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

break       # exit loop now
continue    # skip to next iteration
pass        # do nothing (placeholder)
for..else   # else runs if no break
while..else # else runs if no break

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💎 COMPREHENSIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[x**2 for x in range(10)]              # list
[x for x in lst if x > 0]             # filtered list
{k: v for k, v in pairs}              # dict
{x**2 for x in range(5)}              # set
(x**2 for x in range(10**6))          # generator

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⭐ PATTERN BUILDING BLOCKS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"* " * i                # repeat i stars
" " * (rows - i)        # padding spaces
chr(65 + j)             # A, B, C... (65=A)
min(i, j, n-1-i, n-1-j) # concentric layer
i == 0 or i == n-1      # border check
i == j                  # main diagonal
i + j == n - 1          # anti-diagonal
abs(mid - i)            # distance from center
```

---

## 🎓 Final Summary

```
Loops in Python:
─────────────────────────────────────────────────────
for loop      → iterate over known sequence
while loop    → repeat while condition is True

break         → exit loop immediately
continue      → skip current iteration
pass          → empty placeholder
else on loop  → runs only if no break occurred

range()       → generate number sequences
enumerate()   → loop with index
zip()         → loop multiple iterables together

List comp     → [expr for x in it if cond]
Dict comp     → {k:v for x in it if cond}
Set comp      → {expr for x in it if cond}
Generator     → (expr for x in it if cond)

Patterns key ingredients:
  rows, cols       → control grid size
  i (outer loop)   → current row
  j (inner loop)   → current column
  print(end="")    → stay on same line
  print()          → move to next line
─────────────────────────────────────────────────────
```

---
