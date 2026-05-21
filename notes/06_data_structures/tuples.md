# 🐍 Python Tuples — Zero to Hero
## The Complete Guide — Every Method, Every Trick, Every Pattern

> 🧠 **What is a Tuple?**
> A tuple is like a list's **strict, reliable older sibling** 🧑‍💼
> It holds an **ordered collection of items** — but once created,
> it **CANNOT be changed**. No adding, no removing, no modifying.
> That's not a weakness — that's a **superpower**! 💪
>
> Think of a tuple like a **sealed envelope** 📨:
> You put things in, seal it, and the contents are **guaranteed forever**.

```python
# List  → changeable  📝  uses [ ]
# Tuple → unchangeable 🔒  uses ( )

my_list  = [1, 2, 3]   # can change
my_tuple = (1, 2, 3)   # sealed forever
```

---

## 📚 Table of Contents

1. [Creating Tuples](#-creating-tuples)
2. [Indexing — Grabbing Items](#-indexing--grabbing-items)
3. [Slicing — Grabbing Chunks](#-slicing--grabbing-chunks)
4. [Tuple Methods — count() and index()](#-tuple-methods)
5. [Built-in Functions on Tuples](#-built-in-functions-on-tuples)
6. [Tuple Unpacking — The Star Feature ⭐](#-tuple-unpacking--the-star-feature)
7. [Tuple as Return Value](#-tuple-as-return-value)
8. [Named Tuples](#-named-tuples)
9. [Tuple vs List — When to Use Which](#-tuple-vs-list--when-to-use-which)
10. [Immutability — Deep Understanding](#-immutability--deep-understanding)
11. [Tuples as Dictionary Keys](#-tuples-as-dictionary-keys)
12. [Iterating Tuples](#-iterating-tuples)
13. [Nested Tuples](#-nested-tuples)
14. [Tuple Tricks & Patterns](#-tuple-tricks--patterns)
15. [Real-World Examples](#-real-world-examples)
16. [Common Mistakes](#-common-mistakes)
17. [Cheat Sheet](#-cheat-sheet)

---

## 🏗️ Creating Tuples

```python
# ─── Empty tuple ───
empty = ()
empty = tuple()

# ─── Single type ───
numbers  = (1, 2, 3, 4, 5)
names    = ("Alice", "Bob", "Charlie")
floats   = (1.1, 2.2, 3.3)

# ─── Mixed types (totally fine!) ───
person   = ("Alice", 25, "Mumbai", True)
#            str    int    str     bool

# ─── WITHOUT parentheses — still a tuple! ───
coords   = 10, 20           # (10, 20)  ← tuple packing!
rgb      = 255, 128, 0      # (255, 128, 0)
print(type(coords))         # <class 'tuple'>

# ─── Single-item tuple — THE TRICKY ONE ⚠️ ───
not_tuple = (42)        # ❌ This is just int 42!
is_tuple  = (42,)       # ✅ This IS a tuple — trailing comma!
also_tuple = 42,        # ✅ Also a tuple — no parens needed!

print(type(not_tuple))  # <class 'int'>
print(type(is_tuple))   # <class 'tuple'>
print(is_tuple)         # (42,)
```

```python
# ─── Using tuple() constructor ───
from_list   = tuple([1, 2, 3])        # (1, 2, 3)
from_string = tuple("Python")         # ('P','y','t','h','o','n')
from_range  = tuple(range(1, 6))      # (1, 2, 3, 4, 5)
from_set    = tuple({3, 1, 2})        # (1, 2, 3) order may vary

# ─── Nested tuples ───
matrix   = ((1,2,3), (4,5,6), (7,8,9))
address  = ("Alice", ("MG Road", "Bangalore", 560001))
```

```python
# ─── Tuple from comprehension? No — use generator then convert ───
squares  = tuple(x**2 for x in range(1, 6))
print(squares)    # (1, 4, 9, 16, 25)

evens    = tuple(x for x in range(10) if x % 2 == 0)
print(evens)      # (0, 2, 4, 6, 8)
```

---

## 🔢 Indexing — Grabbing Items

> Same rules as lists — starts at **0**, negative indices count from end!

```python
fruits = ("apple", "banana", "cherry", "mango", "kiwi")
#            0         1          2         3       4     ← positive
#           -5        -4         -3        -2      -1     ← negative

# ─── Positive indexing ───
print(fruits[0])    # apple      ← first
print(fruits[2])    # cherry
print(fruits[4])    # kiwi       ← last

# ─── Negative indexing ───
print(fruits[-1])   # kiwi       ← last
print(fruits[-2])   # mango
print(fruits[-5])   # apple      ← same as [0]

# ─── IndexError — out of range ───
# print(fruits[10])  → IndexError: tuple index out of range

# ─── Trying to modify → TypeError! ───
# fruits[0] = "pineapple"  → TypeError: 'tuple' object does not support item assignment
```

---

## ✂️ Slicing — Grabbing Chunks

> Slicing returns a **new tuple** — original untouched!

```python
# Syntax: tuple[start : stop : step]
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# ─── Basic slices ───
print(nums[2:6])     # (2, 3, 4, 5)
print(nums[:4])      # (0, 1, 2, 3)
print(nums[6:])      # (6, 7, 8, 9)
print(nums[:])       # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)   full copy

# ─── With step ───
print(nums[::2])     # (0, 2, 4, 6, 8)    every 2nd
print(nums[1::2])    # (1, 3, 5, 7, 9)    odd indices
print(nums[::-1])    # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)   REVERSED!

# ─── Negative indices ───
print(nums[-3:])     # (7, 8, 9)           last 3
print(nums[:-3])     # (0, 1, 2, 3, 4, 5, 6)
```

```python
# ─── Real use: split a tuple ───
data = ("Alice", 25, "Mumbai", "Engineer", 85000)

name, age = data[:2]         # first 2
location  = data[2]          # single value
job_info  = data[3:]         # rest

print(name)       # Alice
print(age)        # 25
print(location)   # Mumbai
print(job_info)   # ('Engineer', 85000)
```

---

## 🛠️ Tuple Methods

> Tuples only have **2 methods** — because they can't be changed!
> But what they do, they do perfectly. 🎯

---

### 1. count()

> **Count how many times a value appears.**

```python
# Syntax: tuple.count(value)
# Returns: int
```

```python
# ─── Basic count ───
nums = (1, 2, 3, 2, 4, 2, 5, 2)
print(nums.count(2))    # 4   ← appears 4 times
print(nums.count(9))    # 0   ← not found, returns 0 (no error!)
print(nums.count(1))    # 1

letters = ('a', 'b', 'a', 'c', 'a', 'd')
print(letters.count('a'))   # 3
print(letters.count('z'))   # 0
```

```python
# ─── Real example — dice roll statistics ───
rolls = (4, 6, 2, 6, 1, 6, 3, 5, 6, 2, 4, 6)

print("🎲 Dice Roll Analysis:")
print("─" * 30)
for face in range(1, 7):
    times = rolls.count(face)
    pct   = times / len(rolls) * 100
    bar   = "█" * times
    print(f"  Face {face}: {times:2}x ({pct:.0f}%)  {bar}")

most_common = max(range(1, 7), key=lambda f: rolls.count(f))
print(f"\n  🏆 Most rolled: {most_common}")

# Output:
# 🎲 Dice Roll Analysis:
# ──────────────────────────────
#   Face 1:  1x (8%)   █
#   Face 2:  2x (17%)  ██
#   Face 3:  1x (8%)   █
#   Face 4:  2x (17%)  ██
#   Face 5:  1x (8%)   █
#   Face 6:  5x (42%)  █████
#
#   🏆 Most rolled: 6
```

```python
# ─── Count in a tuple of tuples ───
student_grades = (
    ("Alice",   "A"),
    ("Bob",     "B"),
    ("Charlie", "A"),
    ("Diana",   "A"),
    ("Eve",     "C"),
    ("Frank",   "B"),
)

# Count how many got grade "A"
grades_only = tuple(g for _, g in student_grades)
print(f"  Grade A: {grades_only.count('A')} students")   # 3
print(f"  Grade B: {grades_only.count('B')} students")   # 2
print(f"  Grade C: {grades_only.count('C')} students")   # 1
```

---

### 2. index()

> **Find the INDEX (position) of the FIRST matching value.**

```python
# Syntax: tuple.index(value, start=0, stop=len(tuple))
# Returns: int (index)
# Raises:  ValueError if not found
```

```python
# ─── Basic index ───
colors = ("red", "green", "blue", "green", "yellow")

print(colors.index("green"))         # 1   ← first occurrence
print(colors.index("blue"))          # 2
print(colors.index("yellow"))        # 4
```

```python
# ─── With start and stop (search range) ───
nums = (10, 20, 30, 20, 40, 20, 50)
#         0   1   2   3   4   5   6

print(nums.index(20))        # 1   ← first match overall
print(nums.index(20, 2))     # 3   ← search from index 2
print(nums.index(20, 4))     # 5   ← search from index 4
print(nums.index(20, 2, 5))  # 3   ← search in range [2, 5)
```

```python
# ─── ValueError if not found ───
try:
    pos = colors.index("purple")
except ValueError:
    print("  ❌ 'purple' not in tuple")

# ─── Safe index ───
def tuple_find(tup, value, default=-1):
    try:
        return tup.index(value)
    except ValueError:
        return default

data = (5, 10, 15, 20)
print(tuple_find(data, 15))    # 2
print(tuple_find(data, 99))    # -1  ← safe default
```

```python
# ─── Find ALL positions of a value ───
data    = (3, 1, 4, 1, 5, 9, 2, 6, 1, 7, 1)
target  = 1

# Using enumerate for all positions
all_pos = tuple(i for i, x in enumerate(data) if x == target)
print(f"  Value {target} found at: {all_pos}")
# Value 1 found at: (1, 3, 8, 10)
```

```python
# ─── Real example — leaderboard position ───
leaderboard = ("Alice", "Bob", "Charlie", "Diana", "Eve")

def get_rank(board, player):
    try:
        rank = board.index(player) + 1   # +1 because 0-indexed
        return f"🏆 #{rank}"
    except ValueError:
        return "❌ Not ranked"

print(get_rank(leaderboard, "Charlie"))  # 🏆 #3
print(get_rank(leaderboard, "Frank"))    # ❌ Not ranked
```

---

## 🧰 Built-in Functions on Tuples

> These built-ins work perfectly on tuples!

```python
nums = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# ─── len() ───
print(len(nums))          # 11

# ─── min() / max() ───
print(min(nums))          # 1
print(max(nums))          # 9

# ─── sum() ───
print(sum(nums))          # 44

# ─── Average ───
print(sum(nums)/len(nums))  # 4.0

# ─── sorted() — returns a LIST, not tuple! ───
print(sorted(nums))           # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(sorted(nums, reverse=True))  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# ─── sorted back to tuple ───
sorted_tuple = tuple(sorted(nums))
print(sorted_tuple)       # (1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9)

# ─── reversed() ───
for n in reversed(nums):
    print(n, end=" ")     # 5 3 5 6 2 9 5 1 4 1 3

# ─── enumerate() ───
words = ("apple", "banana", "cherry")
for i, word in enumerate(words, start=1):
    print(f"  {i}. {word}")

# ─── zip() ───
names  = ("Alice", "Bob", "Charlie")
scores = (88, 95, 72)
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# ─── any() / all() ───
flags = (True, False, True, True)
print(any(flags))    # True   (at least one True)
print(all(flags))    # False  (not all True)

nums2 = (2, 4, 6, 8)
print(all(n % 2 == 0 for n in nums2))   # True  (all even)
print(any(n > 7      for n in nums2))   # True  (8 > 7)

# ─── in / not in ───
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)       # True
print("mango"  not in fruits)   # True

# ─── type() / isinstance() ───
t = (1, 2, 3)
print(type(t))                     # <class 'tuple'>
print(isinstance(t, tuple))        # True
print(isinstance(t, (list, tuple)))# True
```

---

## ⭐ Tuple Unpacking — The Star Feature

> Unpacking = **pulling values out** of a tuple into variables.
> This is where tuples TRULY shine! ✨

```python
# ─── Basic unpacking ───
point  = (3, 7)
x, y   = point
print(x)   # 3
print(y)   # 7

rgb     = (255, 128, 0)
red, green, blue = rgb
print(f"R:{red} G:{green} B:{blue}")
# R:255 G:128 B:0

person  = ("Alice", 25, "Mumbai", "Engineer")
name, age, city, job = person
print(f"{name} is a {job} from {city}")
# Alice is a Engineer from Mumbai
```

```python
# ─── The magic swap! ───
a = 10
b = 20

a, b = b, a      # Python creates a tuple (b,a) and unpacks it!
print(a, b)      # 20  10

# Works with more variables too!
x, y, z = 1, 2, 3
x, y, z = z, x, y   # rotate values
print(x, y, z)       # 3  1  2
```

```python
# ─── Extended unpacking with * (star) ───
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

first, *rest = numbers
print(first)   # 1
print(rest)    # [2, 3, 4, 5, 6, 7, 8, 9, 10]  ← rest becomes a LIST!

*start, last = numbers
print(start)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(last)    # 10

first, *middle, last = numbers
print(first)    # 1
print(middle)   # [2, 3, 4, 5, 6, 7, 8, 9]
print(last)     # 10

a, b, *_ = numbers   # _ = "I don't care about the rest"
print(a, b)          # 1  2
```

```python
# ─── Ignore values with _ ───
data = ("Alice", 25, "Mumbai", "Engineer", 85000, "Active")

name, _, city, *_, status = data
print(f"{name} from {city} — Status: {status}")
# Alice from Mumbai — Status: Active
```

```python
# ─── Unpacking in for loops ───
students = [
    ("Alice",   88, "Pass"),
    ("Bob",     45, "Fail"),
    ("Charlie", 72, "Pass"),
]

for name, score, result in students:   # unpack each tuple!
    icon = "✅" if result == "Pass" else "❌"
    print(f"  {icon} {name:<10} Score: {score}  {result}")

# ✅ Alice      Score: 88  Pass
# ❌ Bob        Score: 45  Fail
# ✅ Charlie    Score: 72  Pass
```

```python
# ─── Nested unpacking ───
data = (("Alice", 25), ("Mumbai", "Maharashtra"))
(name, age), (city, state) = data

print(f"{name}, {age}, {city}, {state}")
# Alice, 25, Mumbai, Maharashtra
```

```python
# ─── Unpacking with enumerate and zip ───
teams = ("Mumbai Indians", "Chennai Super Kings", "RCB")

for rank, team in enumerate(teams, start=1):
    print(f"  #{rank}  {team}")
# #1  Mumbai Indians
# #2  Chennai Super Kings
# #3  RCB

scores_a = (88, 75, 92)
scores_b = (72, 85, 88)

for (s_a, s_b) in zip(scores_a, scores_b):
    diff   = s_a - s_b
    winner = "A wins" if diff > 0 else "B wins" if diff < 0 else "Tie"
    print(f"  {s_a} vs {s_b}  →  {winner}")
```

---

## 🎁 Tuple as Return Value

> Functions returning **multiple values** actually return a **tuple**!
> This is one of tuples' most used and loved features.

```python
# ─── Multiple return values ───
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
#          ↑ this is actually a tuple being returned!

result = min_max_avg([3, 1, 4, 1, 5, 9, 2, 6])
print(result)         # (1, 9, 3.875)
print(type(result))   # <class 'tuple'>

# Unpack immediately (most common pattern!)
lo, hi, avg = min_max_avg([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {lo}  Max: {hi}  Avg: {avg:.2f}")
# Min: 1  Max: 9  Avg: 3.88
```

```python
# ─── Real example — quadratic formula ───
import math

def solve_quadratic(a, b, c):
    """Solve ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None, None   # ← still returns tuple!
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x         # same root twice
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

x1, x2 = solve_quadratic(1, -5, 6)    # x² - 5x + 6 = 0
print(f"Roots: x1={x1}, x2={x2}")     # Roots: x1=3.0, x2=2.0

x1, x2 = solve_quadratic(1, 2, 5)    # no real roots
print(f"Roots: {x1}, {x2}")           # Roots: None, None
```

```python
# ─── Divide with remainder ───
def divide(a, b):
    return a // b, a % b   # quotient, remainder

quotient, remainder = divide(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")
# 17 ÷ 5 = 3 remainder 2

# (Python has divmod() built-in for exactly this!)
q, r = divmod(17, 5)
print(q, r)   # 3  2
```

```python
# ─── Distance and direction ───
def analyze_move(x1, y1, x2, y2):
    dx       = x2 - x1
    dy       = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    angle    = math.degrees(math.atan2(dy, dx))
    return round(distance, 2), round(angle, 2)

dist, angle = analyze_move(0, 0, 3, 4)
print(f"Distance: {dist}, Angle: {angle}°")
# Distance: 5.0, Angle: 53.13°
```

---

## 🏷️ Named Tuples

> A named tuple is like a **tuple with labels** — you can access items
> by **name** OR by **position**! Best of both worlds. 🌟

```python
from collections import namedtuple

# Define a named tuple "class"
Point   = namedtuple("Point",   ["x", "y"])
Person  = namedtuple("Person",  ["name", "age", "city"])
Color   = namedtuple("Color",   ["red", "green", "blue"])
Student = namedtuple("Student", ["name", "score", "grade"])
```

```python
# ─── Create instances ───
p      = Point(3, 7)
alice  = Person("Alice", 25, "Mumbai")
white  = Color(255, 255, 255)
s1     = Student("Alice", 92, "A")
```

```python
# ─── Access by NAME (readable!) ───
print(p.x)           # 3
print(p.y)           # 7
print(alice.name)    # Alice
print(alice.age)     # 25
print(white.red)     # 255

# ─── Access by INDEX (still works!) ───
print(p[0])          # 3
print(alice[1])      # 25

# ─── Still a tuple — unpack works! ───
x, y = p
name, age, city = alice
print(x, y)          # 3  7

# ─── Still immutable! ───
# alice.age = 26    → AttributeError!
```

```python
# ─── Useful methods ───
print(alice._asdict())
# OrderedDict([('name', 'Alice'), ('age', 25), ('city', 'Mumbai')])

# _replace() → creates NEW instance with some fields changed
older_alice = alice._replace(age=26)
print(older_alice)    # Person(name='Alice', age=26, city='Mumbai')
print(alice)          # Person(name='Alice', age=25, city='Mumbai')  ← unchanged!

# _fields → see all field names
print(Person._fields)   # ('name', 'age', 'city')

# _make() → create from iterable
data    = ["Bob", 30, "Delhi"]
bob     = Person._make(data)
print(bob)   # Person(name='Bob', age=30, city='Delhi')
```

```python
# ─── Real example — CSV processing with named tuples ───
from collections import namedtuple

Employee = namedtuple("Employee", ["id", "name", "dept", "salary"])

# Simulate data from CSV
raw_data = [
    (1, "Alice",   "Engineering", 95000),
    (2, "Bob",     "Marketing",   72000),
    (3, "Charlie", "Engineering", 88000),
    (4, "Diana",   "HR",          65000),
    (5, "Eve",     "Engineering", 102000),
]

employees = [Employee(*row) for row in raw_data]

# Filter engineering dept
eng_team  = [e for e in employees if e.dept == "Engineering"]
avg_sal   = sum(e.salary for e in eng_team) / len(eng_team)

print(f"🏢 Engineering Team Report")
print("─" * 40)
for e in eng_team:
    print(f"  #{e.id} {e.name:<12} ₹{e.salary:>8,}")
print(f"  {'Average':<13} ₹{avg_sal:>8,.0f}")
```

---

## ⚖️ Tuple vs List — When to Use Which

```
┌─────────────────────┬──────────────────────┬──────────────────────┐
│ Feature             │ Tuple  ()            │ List   []            │
├─────────────────────┼──────────────────────┼──────────────────────┤
│ Ordered?            │ ✅ Yes               │ ✅ Yes               │
│ Duplicates?         │ ✅ Yes               │ ✅ Yes               │
│ Changeable?         │ ❌ No (immutable)    │ ✅ Yes (mutable)     │
│ Methods             │ 2 (count, index)     │ 11+ methods          │
│ Dict key?           │ ✅ Yes               │ ❌ No                │
│ Memory usage        │ 🔵 Less              │ 🔴 More              │
│ Speed               │ 🔵 Faster            │ 🔴 Slightly slower   │
│ Hashable?           │ ✅ Yes               │ ❌ No                │
└─────────────────────┴──────────────────────┴──────────────────────┘
```

```python
# ─── USE TUPLE when: ───

# 1. Data that should NOT change (coordinates, config, RGB)
SCREEN_SIZE  = (1920, 1080)   # don't change resolution mid-run
GPS_ORIGIN   = (0.0, 0.0)     # fixed origin point
API_ENDPOINT = ("api.example.com", 443, "https")

# 2. Returning multiple values from functions
def get_bounds():
    return (0, 0, 100, 100)   # x, y, width, height

# 3. Dictionary keys (lists can't be dict keys!)
cache = {}
cache[(3, 5)]   = "calculated"   # ✅ tuple as key
cache[("Alice", "Mumbai")] = 42  # ✅

# 4. Data records that shouldn't change
PLANETS = (
    ("Mercury",  0.39),
    ("Venus",    0.72),
    ("Earth",    1.00),
    ("Mars",     1.52),
)

# ─── USE LIST when: ───

# 1. Collection that will grow or shrink
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.remove("milk")

# 2. When you need to sort in-place
scores = [85, 92, 78, 95, 61]
scores.sort()

# 3. When items will be modified
grid = [[0]*3 for _ in range(3)]
grid[1][1] = 9
```

---

## 🔒 Immutability — Deep Understanding

```python
# ─── You CANNOT modify a tuple ───
t = (1, 2, 3)
# t[0]   = 99      → TypeError
# t.append(4)      → AttributeError
# del t[0]         → TypeError
```

```python
# ─── BUT: if a tuple CONTAINS a mutable object... ───
t = ([1, 2], [3, 4])
print(id(t[0]))    # memory address of inner list

t[0].append(99)    # ✅ modifying the LIST inside
print(t)           # ([1, 2, 99], [3, 4])

# The tuple itself didn't change (still 2 items at same addresses)
# but the mutable contents can change!

# ─── Visual ───
# t ─→ slot[0] ─→ [1, 2, 99]   ← list changed
#      slot[1] ─→ [3, 4]
# The SLOT assignments in t are frozen. The list values are not.
```

```python
# ─── Immutability = Hashable = Can be dict key or set member ───

# ✅ Tuple in a set
visited_coords = set()
visited_coords.add((3, 5))
visited_coords.add((1, 2))
visited_coords.add((3, 5))   # duplicate — ignored!
print(visited_coords)         # {(3, 5), (1, 2)}

# ✅ Tuple as dict key
distance_cache = {}
distance_cache[(0,0), (3,4)] = 5.0    # distance from origin to (3,4)
distance_cache[(1,1), (4,5)] = 5.0

# ❌ List in a set — crashes!
# {[1,2], [3,4]}   → TypeError: unhashable type: 'list'
```

```python
# ─── "Modifying" a tuple = creating a NEW one ───
t = (1, 2, 3)

# Can't change it, but can BUILD a new one
t2 = t + (4, 5)       # (1, 2, 3, 4, 5)  ← NEW tuple
t3 = t[:2] + (99,) + t[2:]  # (1, 2, 99, 3)  ← NEW tuple

print(t)    # (1, 2, 3)      ← original safe!
print(t2)   # (1, 2, 3, 4, 5)
print(t3)   # (1, 2, 99, 3)
```

---

## 🗝️ Tuples as Dictionary Keys

> Because tuples are **hashable** (immutable), they can be dictionary keys.
> Lists CANNOT be dictionary keys! This is a big deal. 🔑

```python
# ─── 2D grid with tuple keys ───
grid = {}
grid[(0, 0)] = "start"
grid[(3, 4)] = "treasure"
grid[(5, 5)] = "exit"
grid[(2, 3)] = "enemy"

# Check what's at a position
pos = (3, 4)
if pos in grid:
    print(f"At {pos}: {grid[pos]}")   # At (3, 4): treasure

# ─── Translation cache ───
translations = {
    ("hello",  "en", "es"): "hola",
    ("hello",  "en", "fr"): "bonjour",
    ("hello",  "en", "hi"): "नमस्ते",
    ("goodbye","en", "es"): "adiós",
}

key = ("hello", "en", "hi")
print(translations.get(key, "Not found"))   # नमस्ते
```

```python
# ─── Real example — flight routes ───
flight_prices = {
    ("Mumbai",    "Delhi"):    4500,
    ("Delhi",     "Bangalore"):3800,
    ("Mumbai",    "Chennai"):  3200,
    ("Bangalore", "Kolkata"):  5100,
}

def get_fare(origin, destination):
    key     = (origin, destination)
    rev_key = (destination, origin)
    return (flight_prices.get(key)
            or flight_prices.get(rev_key)
            or "Route not found")

print(f"Mumbai → Delhi:     ₹{get_fare('Mumbai',    'Delhi')}")
print(f"Bangalore → Mumbai: ₹{get_fare('Bangalore', 'Mumbai')}")
print(f"Delhi → Chennai:     {get_fare('Delhi',     'Chennai')}")
```

---

## 🔄 Iterating Tuples

```python
# ─── Basic for loop ───
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(f"  🍎 {fruit}")

# ─── With index using enumerate ───
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# ─── While loop with index ───
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# ─── Reverse iteration ───
for fruit in reversed(fruits):
    print(fruit)

# ─── Loop over tuple of tuples ───
students = (
    ("Alice",   92),
    ("Bob",     85),
    ("Charlie", 78),
)

for name, score in students:
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"  {name:<10} {score}  ({grade})")
```

---

## 🪆 Nested Tuples

```python
# ─── Matrix as tuple of tuples ───
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
)

# Access
print(matrix[0])        # (1, 2, 3)
print(matrix[1][2])     # 6
print(matrix[-1][-1])   # 9

# Iterate
for row in matrix:
    print("  " + "  ".join(f"{n:2}" for n in row))

#    1   2   3
#    4   5   6
#    7   8   9
```

```python
# ─── Nested personal data ───
contacts = (
    ("Alice", ("9876543210", "alice@email.com"), ("MG Road", "Bangalore")),
    ("Bob",   ("9123456789", "bob@email.com"),   ("CP",      "Delhi"    )),
)

for name, (phone, email), (street, city) in contacts:
    print(f"  👤 {name}")
    print(f"     📱 {phone}")
    print(f"     📧 {email}")
    print(f"     📍 {street}, {city}")
    print()
```

```python
# ─── Flatten nested tuple ───
nested = ((1, 2), (3, 4, 5), (6,))

flat = tuple(item for group in nested for item in group)
print(flat)   # (1, 2, 3, 4, 5, 6)
```

---

## 🎩 Tuple Tricks & Patterns

```python
# ─── Tuple packing ───
# Python automatically packs comma-separated values into a tuple!
point   = 3, 7           # (3, 7)
triple  = 1, 2, 3        # (1, 2, 3)
single  = 42,            # (42,)  ← don't forget the comma!

# ─── Conditional expression returning tuple ───
def classify(n):
    return ("positive", n) if n > 0 else ("negative", n) if n < 0 else ("zero", 0)

category, value = classify(42)
print(f"  {value} is {category}")   # 42 is positive
```

```python
# ─── Tuple as immutable default argument (safe!) ───
def process(data, allowed=(1, 2, 3)):   # tuple default is safe!
    return [x for x in data if x in allowed]

result = process([1, 3, 5, 2, 4, 1])
print(result)   # [1, 3, 2, 1]
```

```python
# ─── Zipping tuples ───
keys   = ("name", "age", "city")
values = ("Alice", 25, "Mumbai")

profile = dict(zip(keys, values))
print(profile)   # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}
```

```python
# ─── Using tuple for multiple assignment patterns ───

# Rotate three values
a, b, c = 1, 2, 3
a, b, c = b, c, a     # rotate left
print(a, b, c)         # 2  3  1

# Fibonacci using tuple swap
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b    # ← tuple swap! clean and Pythonic
print()
# 0 1 1 2 3 5 8 13 21 34
```

```python
# ─── Tuple comparison (lexicographic) ───
print((1, 2, 3) == (1, 2, 3))    # True
print((1, 2, 3) == (3, 2, 1))    # False — order matters!
print((1, 2, 3) <  (1, 2, 4))    # True  — compare element by element
print((1, 2)    <  (1, 2, 3))    # True  — shorter is "less"
print((2,)      >  (1, 9, 9))    # True  — 2 > 1 at first position

# ─── Sorting list of tuples ───
players = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 88)]

# Sort by score (desc), then name (asc) for ties
players.sort(key=lambda p: (-p[1], p[0]))
for rank, (name, score) in enumerate(players, 1):
    print(f"  #{rank} {name:<10} {score}")
# #1 Bob        95
# #2 Alice      88   ← Alice before Diana alphabetically
# #3 Diana      88
# #4 Charlie    72
```

```python
# ─── Unpack from function returning tuple ───
import os
path    = "/home/user/documents/report.pdf"

dirname  = os.path.dirname(path)    # /home/user/documents
basename = os.path.basename(path)   # report.pdf
name, ext = os.path.splitext(basename)  # ('report', '.pdf')

print(f"Folder: {dirname}")
print(f"File:   {name}")
print(f"Ext:    {ext}")
```

---

## 🌍 Real-World Examples

### Example 1 — RGB Color Palette

```python
from collections import namedtuple

Color = namedtuple("Color", ["name", "r", "g", "b"])

palette = (
    Color("Red",      255,   0,   0),
    Color("Green",      0, 255,   0),
    Color("Blue",       0,   0, 255),
    Color("White",    255, 255, 255),
    Color("Black",      0,   0,   0),
    Color("Yellow",   255, 255,   0),
    Color("Cyan",       0, 255, 255),
    Color("Magenta",  255,   0, 255),
    Color("Orange",   255, 165,   0),
    Color("Purple",   128,   0, 128),
)

def to_hex(color):
    return f"#{color.r:02X}{color.g:02X}{color.b:02X}"

def brightness(color):
    return (0.299 * color.r + 0.587 * color.g + 0.114 * color.b) / 255

print(f"{'Color':<12} {'R':>4} {'G':>4} {'B':>4}  {'Hex':>8}  {'Brightness':>10}")
print("─" * 55)
for c in palette:
    br  = brightness(c)
    bar = "█" * int(br * 10)
    print(f"  {c.name:<10} {c.r:>4} {c.g:>4} {c.b:>4}  {to_hex(c):>8}  {br:>6.0%}  {bar}")
```

---

### Example 2 — GPS Route Tracker

```python
import math

Waypoint = namedtuple("Waypoint", ["name", "lat", "lon"])

def haversine(p1, p2):
    """Distance in km between two GPS coords."""
    R    = 6371
    dlat = math.radians(p2.lat - p1.lat)
    dlon = math.radians(p2.lon - p1.lon)
    a    = (math.sin(dlat/2)**2
            + math.cos(math.radians(p1.lat))
            * math.cos(math.radians(p2.lat))
            * math.sin(dlon/2)**2)
    return R * 2 * math.asin(math.sqrt(a))

route = (
    Waypoint("Mumbai",    19.0760,  72.8777),
    Waypoint("Pune",      18.5204,  73.8567),
    Waypoint("Bangalore", 12.9716,  77.5946),
    Waypoint("Chennai",   13.0827,  80.2707),
    Waypoint("Hyderabad", 17.3850,  78.4867),
)

print("🗺️  Road Trip Route")
print("─" * 50)
total_km = 0

for i in range(len(route) - 1):
    origin = route[i]
    dest   = route[i + 1]
    km     = haversine(origin, dest)
    total_km += km
    print(f"  📍 {origin.name:<12} → {dest.name:<12}  {km:>7.1f} km")

print("─" * 50)
print(f"  🏁 Total Distance: {total_km:>8.1f} km")
```

---

### Example 3 — Student Records System

```python
from collections import namedtuple

Student = namedtuple("Student", ["id", "name", "marks", "attendance"])

def grade(avg):
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    return "F"

records = (
    Student(1, "Alice",   (88, 92, 85, 90, 94), 95),
    Student(2, "Bob",     (72, 68, 75, 70, 65), 80),
    Student(3, "Charlie", (55, 60, 58, 62, 50), 70),
    Student(4, "Diana",   (98, 95, 99, 100, 97), 99),
    Student(5, "Eve",     (40, 45, 50, 42, 48), 60),
)

print(f"{'─'*60}")
print(f"  {'ID'} {'Name':<12} {'Avg':>6} {'Grade':>6} {'Attend':>8}  Status")
print(f"{'─'*60}")

for s in records:
    avg    = sum(s.marks) / len(s.marks)
    g      = grade(avg)
    passed = avg >= 60 and s.attendance >= 75
    status = "✅ Pass" if passed else "❌ Fail"
    print(f"  {s.id:2} {s.name:<12} {avg:>6.1f} {g:>6} {s.attendance:>7}%  {status}")

print(f"{'─'*60}")

# Stats using tuple methods
all_avgs  = tuple(sum(s.marks)/len(s.marks) for s in records)
top_idx   = all_avgs.index(max(all_avgs))
print(f"\n  🏆 Topper : {records[top_idx].name} ({max(all_avgs):.1f})")
print(f"  📊 Class Avg: {sum(all_avgs)/len(all_avgs):.1f}")
```

---

### Example 4 — Fibonacci with Tuple Swap

```python
def fibonacci(n):
    """Generate first n Fibonacci numbers as a tuple."""
    if n <= 0: return ()
    if n == 1: return (0,)

    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return tuple(fibs)

fib20 = fibonacci(20)
print(f"  First 20 Fibonacci numbers:")
for i, f in enumerate(fib20):
    print(f"  F({i:2}) = {f:5}", end="  " if i % 4 < 3 else "\n")

print(f"\n  count(0) = {fib20.count(0)}")        # 1
print(f"  index(8) = {fib20.index(8)}")          # 6  (F(6)=8)
print(f"  Sum = {sum(fib20)}")
print(f"  Max = {max(fib20)}")
```

---

## 🚨 Common Mistakes

### 1. Forgetting trailing comma for single-item tuple ⚠️

```python
# ❌ This is just an integer!
t = (42)
print(type(t))   # <class 'int'>

# ✅ Trailing comma makes it a tuple
t = (42,)
print(type(t))   # <class 'tuple'>

# ✅ No parens also works
t = 42,
print(type(t))   # <class 'tuple'>
```

### 2. Trying to modify a tuple 🔒

```python
t = (1, 2, 3)

# ❌ All of these crash!
t[0]   = 10          # TypeError
t.append(4)          # AttributeError
t.remove(2)          # AttributeError
del t[0]             # TypeError

# ✅ Build a new tuple instead
t = (10,) + t[1:]    # (10, 2, 3)
```

### 3. Wrong unpacking count 📦

```python
t = (1, 2, 3)

# ❌ Wrong number of variables
a, b = t          # ValueError: too many values to unpack

# ✅ Match exactly
a, b, c = t       # ✅

# ✅ Or use * for flexible unpacking
a, *rest = t      # a=1, rest=[2,3]
```

### 4. Confusing tuple() with (value) 😕

```python
# ❌ (x) is just x with parentheses — not a tuple!
result = (5 + 3)
print(type(result))   # <class 'int'>  ← surprise!

# ✅ Use trailing comma
result = (5 + 3,)
print(type(result))   # <class 'tuple'>
```

### 5. Assuming tuples are always faster 🏎️

```python
# Tuples are faster for CREATION and ITERATION
# For in-membership testing, both are O(n)
# For large membership checks, USE A SET!

data = tuple(range(1_000_000))
# "x in data" scans up to 1M items — slow!

data_set = set(range(1_000_000))
# "x in data_set" is O(1) — instant!
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️  CREATING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

empty    = ()
one      = (42,)            # ← comma required!
many     = (1, 2, 3)
packed   = 1, 2, 3          # parentheses optional
from_lst = tuple([1,2,3])
from_str = tuple("abc")     # ('a','b','c')
from_rng = tuple(range(5))  # (0,1,2,3,4)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔢  INDEXING & SLICING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

t = (10, 20, 30, 40, 50)

t[0]        # 10  (first)
t[-1]       # 50  (last)
t[1:4]      # (20, 30, 40)
t[::-1]     # (50, 40, 30, 20, 10)  reversed

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️  METHODS  (only 2!)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

t.count(20)     # how many times 20 appears
t.index(30)     # index of first 30

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧰  BUILT-INS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

len(t)          # 5
min(t)          # 10
max(t)          # 50
sum(t)          # 150
sorted(t)       # [10,20,30,40,50]  ← returns LIST
20 in t         # True
99 not in t     # True

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦  UNPACKING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

a, b, c = (1, 2, 3)
first, *rest   = (1, 2, 3, 4, 5)
*start, last   = (1, 2, 3, 4, 5)
a, *mid, b     = (1, 2, 3, 4, 5)
a, b = b, a                         # swap!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏷️  NAMED TUPLE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p     = Point(3, 7)
p.x          # 3
p[0]         # 3
x, y = p     # unpack
p._asdict()  # {'x':3, 'y':7}
p._replace(x=10)  # new Point(x=10, y=7)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔑  AS DICT KEY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

d = {}
d[(1,2)] = "point"    # ✅ tuples are hashable!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡  "MODIFY" = CREATE NEW
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

t = (1, 2, 3)
t2 = t + (4, 5)              # (1,2,3,4,5)
t3 = t[:2] + (99,) + t[2:]  # (1,2,99,3)
```

---

## 🎓 Final Summary

```
Tuples in a nutshell:
──────────────────────────────────────────────────────
Created with ( ) or just commas:   x = 1, 2, 3
Single item needs trailing comma:  x = (42,)
Immutable: NO add, remove, change  ← FEATURE not bug!

Methods (only 2):
  .count(val)   → count occurrences
  .index(val)   → find first position

Superpowers:
  ✅ Unpack into variables:   a, b, c = t
  ✅ Extended unpack (*):     first, *rest = t
  ✅ Magic swap:              a, b = b, a
  ✅ Multiple return values:  return x, y, z
  ✅ Dict keys (lists can't!) d[(1,2)] = value
  ✅ Named tuples for clarity (namedtuple)

Use tuple when:
  → data should NOT change (coords, config, records)
  → returning multiple values from a function
  → using as dictionary key
  → representing a fixed "record" (name, age, city)

Use list when:
  → data grows/shrinks dynamically
  → you need to sort, reverse, modify items
──────────────────────────────────────────────────────
```