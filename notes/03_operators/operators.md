# ⚙️ Python Operators — Complete Notes

> **"Operators are the verbs of Python — they make things happen!"**

---

## 📌 Table of Contents

1. [What are Operators?](#what-are-operators)
2. [Arithmetic Operators](#arithmetic-operators)
3. [Assignment Operators](#assignment-operators)
4. [Comparison Operators](#comparison-operators)
5. [Logical Operators](#logical-operators)
6. [Bitwise Operators](#bitwise-operators)
7. [Identity Operators](#identity-operators)
8. [Membership Operators](#membership-operators)
9. [Operator Precedence](#operator-precedence)
10. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## 🤔 What are Operators?

**Operators** are special symbols or keywords that perform operations on **operands** (values/variables).

```python
result = 10 + 5
#        ^^   ^  ^
#    operand op operand
```

### 🗂️ Types of Operators in Python

| # | Type          | Purpose                              |
|---|---------------|--------------------------------------|
| 1 | ➕ Arithmetic  | Math operations                      |
| 2 | 📝 Assignment  | Assign values to variables           |
| 3 | ⚖️ Comparison  | Compare two values → returns bool    |
| 4 | 🔗 Logical     | Combine conditions                   |
| 5 | 🔢 Bitwise     | Operate on binary bits               |
| 6 | 🪪 Identity    | Check object identity (`is`)         |
| 7 | 🔍 Membership  | Check membership (`in`)              |

---

## ➕ 1. Arithmetic Operators

Used to perform **mathematical calculations**.

| Operator | Name           | Example      | Result  |
|----------|----------------|--------------|---------|
| `+`      | Addition       | `10 + 3`     | `13`    |
| `-`      | Subtraction    | `10 - 3`     | `7`     |
| `*`      | Multiplication | `10 * 3`     | `30`    |
| `/`      | Division       | `10 / 3`     | `3.333` |
| `//`     | Floor Division | `10 // 3`    | `3`     |
| `%`      | Modulus        | `10 % 3`     | `1`     |
| `**`     | Exponentiation | `2 ** 8`     | `256`   |

### 🧪 Examples

```python
a, b = 10, 3

print(a + b)   # 13   ← Addition
print(a - b)   # 7    ← Subtraction
print(a * b)   # 30   ← Multiplication
print(a / b)   # 3.3333... ← True division (always float)
print(a // b)  # 3    ← Floor division (drops decimal)
print(a % b)   # 1    ← Remainder
print(a ** b)  # 1000 ← 10 to the power of 3

# 🔥 Practical tricks
print(15 % 2)   # 1 → Odd/Even check (1 = odd, 0 = even)
print(100 // 10) # 10 → Remove last digit
print(2 ** 10)  # 1024 → Quick powers of 2
```

### 🧵 `+` and `*` with Strings & Lists

```python
# String repetition
print("Ha" * 3)       # HaHaHa
print("Hi" + " " + "there!")  # Hi there!

# List repetition
print([0] * 5)        # [0, 0, 0, 0, 0]
print([1, 2] + [3, 4]) # [1, 2, 3, 4]
```

---

## 📝 2. Assignment Operators

Used to **assign values** to variables. Compound operators combine arithmetic + assignment.

| Operator | Example    | Equivalent To  | Meaning               |
|----------|------------|----------------|-----------------------|
| `=`      | `x = 5`    | `x = 5`        | Assign                |
| `+=`     | `x += 3`   | `x = x + 3`    | Add and assign        |
| `-=`     | `x -= 3`   | `x = x - 3`    | Subtract and assign   |
| `*=`     | `x *= 3`   | `x = x * 3`    | Multiply and assign   |
| `/=`     | `x /= 3`   | `x = x / 3`    | Divide and assign     |
| `//=`    | `x //= 3`  | `x = x // 3`   | Floor divide & assign |
| `%=`     | `x %= 3`   | `x = x % 3`    | Modulus and assign    |
| `**=`    | `x **= 3`  | `x = x ** 3`   | Power and assign      |
| `&=`     | `x &= 3`   | `x = x & 3`    | Bitwise AND & assign  |
| `\|=`    | `x \|= 3`  | `x = x \| 3`   | Bitwise OR & assign   |
| `^=`     | `x ^= 3`   | `x = x ^ 3`    | Bitwise XOR & assign  |
| `>>=`    | `x >>= 1`  | `x = x >> 1`   | Right shift & assign  |
| `<<=`    | `x <<= 1`  | `x = x << 1`   | Left shift & assign   |

### 🧪 Examples

```python
x = 10
print(x)    # 10

x += 5;  print(x)   # 15
x -= 3;  print(x)   # 12
x *= 2;  print(x)   # 24
x /= 4;  print(x)   # 6.0
x //= 2; print(x)   # 3.0
x **= 3; print(x)   # 27.0
x %= 5;  print(x)   # 2.0
```

### 🔢 Multiple Assignment (Bonus!)

```python
# Assign same value
a = b = c = 0
print(a, b, c)  # 0 0 0

# Tuple unpacking
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Swap without temp variable 🔥
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# Walrus operator := (Python 3.8+) — assign & use in one step
if (n := len("hello")) > 3:
    print(f"String is long: {n} chars")  # String is long: 5 chars
```

---

## ⚖️ 3. Comparison Operators

Used to **compare two values** — always returns `True` or `False`.

| Operator | Name                  | Example   | Result  |
|----------|-----------------------|-----------|---------|
| `==`     | Equal to              | `5 == 5`  | `True`  |
| `!=`     | Not equal to          | `5 != 3`  | `True`  |
| `>`      | Greater than          | `5 > 3`   | `True`  |
| `<`      | Less than             | `5 < 3`   | `False` |
| `>=`     | Greater than or equal | `5 >= 5`  | `True`  |
| `<=`     | Less than or equal    | `5 <= 3`  | `False` |

### 🧪 Examples

```python
x, y = 10, 20

print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(x <= 9)   # False

# 🔥 Chained comparisons (Python superpower!)
age = 25
print(18 <= age < 60)   # True — adult working age
print(1 < 2 < 3 < 4)   # True — all in order

# Comparing strings (lexicographic order)
print("apple" < "banana")  # True
print("z" > "a")           # True

# Comparing lists
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2] < [1, 3])         # True (compares element by element)
```

> ⚠️ **Common Mistake:**
> ```python
> x = 5
> print(x == 5)   # ✅ True  — comparison
> print(x = 5)    # ❌ SyntaxError — assignment inside expression
> ```

---

## 🔗 4. Logical Operators

Used to **combine multiple conditions**.

| Operator | Description                        | Example              | Result  |
|----------|------------------------------------|----------------------|---------|
| `and`    | True if **both** are True          | `True and False`     | `False` |
| `or`     | True if **at least one** is True   | `True or False`      | `True`  |
| `not`    | **Reverses** the boolean value     | `not True`           | `False` |

### 🔲 Truth Tables

#### `and`
| A       | B       | A and B |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `False` |
| `False` | `True`  | `False` |
| `False` | `False` | `False` |

#### `or`
| A       | B       | A or B  |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `True`  |
| `False` | `True`  | `True`  |
| `False` | `False` | `False` |

### 🧪 Examples

```python
age = 25
income = 50000

# and — both must be true
if age >= 18 and income >= 30000:
    print("Loan approved ✅")

# or — at least one must be true
has_id = False
has_passport = True
if has_id or has_passport:
    print("Entry allowed ✅")

# not — reverse the condition
is_banned = False
if not is_banned:
    print("Welcome! 👋")

# Chained logical operators
x = 15
print(x > 10 and x < 20 and x % 3 == 0)  # True
```

### 🔥 Short-Circuit Evaluation

Python stops evaluating as soon as the result is determined!

```python
# 'and' stops at first False
print(False and (1/0))  # False — division never happens!

# 'or' stops at first True
print(True or (1/0))    # True — division never happens!

# Practical: safe default values
name = "" or "Anonymous"
print(name)  # Anonymous (because "" is falsy)

value = None or 0 or [] or "found!"
print(value)  # found!
```

### 🧠 Truthy & Falsy Values

```python
# Falsy values in Python:
False, None, 0, 0.0, "", [], {}, (), set()

# Everything else is Truthy!
bool(0)      # False
bool("")     # False
bool([])     # False
bool(1)      # True
bool("hi")   # True
bool([1])    # True
```

---

## 🔢 5. Bitwise Operators

Operate on **binary representations** of integers, bit by bit.

| Operator | Name         | Example    | Result | Binary               |
|----------|--------------|------------|--------|----------------------|
| `&`      | AND          | `5 & 3`    | `1`    | `0101 & 0011 = 0001` |
| `\|`     | OR           | `5 \| 3`   | `7`    | `0101 \| 0011 = 0111`|
| `^`      | XOR          | `5 ^ 3`    | `6`    | `0101 ^ 0011 = 0110` |
| `~`      | NOT          | `~5`       | `-6`   | flips all bits       |
| `<<`     | Left Shift   | `5 << 1`   | `10`   | `0101 → 1010`        |
| `>>`     | Right Shift  | `5 >> 1`   | `2`    | `0101 → 0010`        |

### 🧪 Examples

```python
a = 5   # binary: 0101
b = 3   # binary: 0011

print(a & b)   # 1  → 0001  (AND: both bits must be 1)
print(a | b)   # 7  → 0111  (OR: at least one bit is 1)
print(a ^ b)   # 6  → 0110  (XOR: bits differ)
print(~a)      # -6         (NOT: flips bits, -(n+1))
print(a << 1)  # 10 → 1010  (Left shift: multiply by 2)
print(a >> 1)  # 2  → 0010  (Right shift: divide by 2)

# 🔥 Practical uses
# Check if number is even/odd
print(7 & 1)   # 1 → Odd
print(8 & 1)   # 0 → Even

# Multiply/divide by powers of 2
print(3 << 3)  # 24  (3 × 2³)
print(64 >> 2) # 16  (64 ÷ 2²)
```

---

## 🪪 6. Identity Operators

Check whether two variables **point to the same object** in memory.

| Operator | Description                                    |
|----------|------------------------------------------------|
| `is`     | Returns `True` if both are the **same object** |
| `is not` | Returns `True` if they are **different objects**|

### 🧪 Examples

```python
# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  ← same value
print(a is b)    # False ← different objects in memory
print(a is c)    # True  ← c points to same object as a

# Check IDs
print(id(a))  # e.g. 140234567
print(id(b))  # different number
print(id(c))  # same as id(a) ✅

# Common use: check for None
x = None
print(x is None)      # ✅ Correct way
print(x is not None)  # False

# Small integers are cached (-5 to 256)
x = 100
y = 100
print(x is y)  # True  ← Python caches small ints

x = 1000
y = 1000
print(x is y)  # False ← Not cached
```

> ⚠️ **Rule:** Always use `==` to compare **values**, and `is` to compare **identity (memory location)**.

---

## 🔍 7. Membership Operators

Check whether a value **exists inside** a sequence (string, list, tuple, dict, set).

| Operator | Description                              |
|----------|------------------------------------------|
| `in`     | `True` if value is found in sequence     |
| `not in` | `True` if value is NOT found in sequence |

### 🧪 Examples

```python
# Lists
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)      # True
print("mango" not in fruits)  # True

# Strings
text = "Hello, Python!"
print("Python" in text)       # True
print("Java" in text)         # False

# Tuples
coords = (10, 20, 30)
print(20 in coords)           # True

# Dictionaries (checks KEYS by default)
person = {"name": "Alice", "age": 25}
print("name" in person)       # True
print("Alice" in person)      # False ← checks keys, not values!
print("Alice" in person.values())  # True ← check values explicitly

# Sets
vowels = {'a', 'e', 'i', 'o', 'u'}
print('e' in vowels)   # True
print('z' in vowels)   # False

# 🔥 Practical use in conditions
username = "admin"
banned = ["spammer", "hacker", "troll"]
if username not in banned:
    print("Access granted ✅")
```

---

## 📊 8. Operator Precedence

When multiple operators appear in one expression, Python follows this order (highest → lowest):

| Priority | Operator(s)                         | Description                  |
|----------|-------------------------------------|------------------------------|
| 1 🥇     | `()`                                | Parentheses                  |
| 2        | `**`                                | Exponentiation               |
| 3        | `+x`, `-x`, `~x`                   | Unary plus/minus/NOT         |
| 4        | `*`, `/`, `//`, `%`                 | Multiplication, Division      |
| 5        | `+`, `-`                            | Addition, Subtraction         |
| 6        | `<<`, `>>`                          | Bitwise Shifts               |
| 7        | `&`                                 | Bitwise AND                  |
| 8        | `^`                                 | Bitwise XOR                  |
| 9        | `\|`                                | Bitwise OR                   |
| 10       | `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons |
| 11       | `not`                               | Logical NOT                  |
| 12       | `and`                               | Logical AND                  |
| 13 🥉    | `or`                                | Logical OR                   |

### 🧪 Examples

```python
# Without parentheses — follows precedence
print(2 + 3 * 4)       # 14  (not 20! * before +)
print(2 ** 3 ** 2)     # 512 (** is right-associative: 3**2=9, 2**9=512)
print(10 - 2 + 3)      # 11  (left to right)
print(not True or True) # True  (not first, then or)

# With parentheses — override precedence
print((2 + 3) * 4)     # 20
print((10 - 2) + 3)    # 11 (same here)
print(not (True or True))  # False

# Complex expression
result = 3 + 4 * 2 ** 2 - 1
# Step 1: 2**2 = 4
# Step 2: 4*4  = 16
# Step 3: 3+16 = 19
# Step 4: 19-1 = 18
print(result)  # 18
```

> 💡 **Pro Tip:** When in doubt, **use parentheses** to make your intent clear — it's better than memorizing the full table!

---

## 📋 Quick Cheat Sheet

```python
# ── ARITHMETIC ────────────────────────────────────────────────
+    -    *    /     # Add, Sub, Mul, Div
//   %    **        # Floor Div, Modulus, Power

# ── ASSIGNMENT ────────────────────────────────────────────────
=    +=   -=   *=   /=   //=   %=   **=

# ── COMPARISON (returns bool) ─────────────────────────────────
==   !=   >    <    >=   <=

# ── LOGICAL ───────────────────────────────────────────────────
and    or    not

# ── BITWISE ───────────────────────────────────────────────────
&    |    ^    ~    <<    >>

# ── IDENTITY ──────────────────────────────────────────────────
is    is not

# ── MEMBERSHIP ────────────────────────────────────────────────
in    not in

# ── WALRUS (Python 3.8+) ──────────────────────────────────────
:=   # Assign and return value in one step
```

---

## 🧠 Memory Tips

```
A — Arithmetic   → Math magic ➕➖✖️➗
C — Comparison   → True/False battles ⚖️
L — Logical      → and / or / not 🔗
A — Assignment   → Store & update 📦
B — Bitwise      → Binary power 💻
I — Identity     → Same object? 🪪
M — Membership   → Found inside? 🔍

"A CLAIM" — All operators in Python!
```

---


