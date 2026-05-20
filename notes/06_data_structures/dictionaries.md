# 📖 Python Dictionaries — Zero to Advanced (Complete Notes)

> **"Dictionaries are Python's key-value powerhouse — like a real dictionary, look up anything instantly!"**

---

## 📌 Table of Contents

1. [What is a Dictionary?](#what-is-a-dictionary)
2. [Creating Dictionaries](#creating-dictionaries)
3. [Accessing Values](#accessing-values)
4. [Adding & Modifying](#adding--modifying)
5. [Deleting Items](#deleting-items)
6. [All Dictionary Methods](#all-dictionary-methods)
7. [Looping Through Dictionaries](#looping-through-dictionaries)
8. [Dictionary Comprehensions](#dictionary-comprehensions)
9. [Nested Dictionaries](#nested-dictionaries)
10. [Merging Dictionaries](#merging-dictionaries)
11. [Advanced Techniques](#advanced-techniques)
12. [Dict vs Other Structures](#dict-vs-other-structures)
13. [Quick Cheat Sheet](#quick-cheat-sheet)

---

## 🤔 What is a Dictionary?

A **dictionary** is an **unordered** (ordered since Python 3.7+), **mutable** collection of **key-value pairs**.

```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}
#          ^key^   ^value^   ^key^  ^v^   ^key^    ^value^
```

### ✅ Key Properties

| Property         | Meaning                                         |
|------------------|-------------------------------------------------|
| ✅ Key-Value Pairs | Every item is a `key: value` pair             |
| ✅ Ordered        | Insertion order maintained (Python 3.7+)        |
| ✅ Mutable        | Can add, change, delete items                   |
| ❌ Duplicate Keys | Keys must be **unique** (values can repeat)     |
| ✅ Any Value Type | Values can be anything — list, dict, func, etc. |
| ✅ Immutable Keys | Keys must be hashable (str, int, tuple — not list) |

### 🔑 Valid Key Types
```python
d = {
    "string_key":  1,     # ✅ string
    42:            2,     # ✅ integer
    3.14:          3,     # ✅ float
    True:          4,     # ✅ bool
    (1, 2):        5,     # ✅ tuple
    # [1, 2]:      6,     # ❌ list → TypeError (unhashable)
    # {1, 2}:      7,     # ❌ set  → TypeError (unhashable)
}
```

---

## 🏗️ Creating Dictionaries

### Basic Ways
```python
# Empty dictionary
empty1 = {}
empty2 = dict()

# With values — curly brace syntax
student = {
    "name":   "Alice",
    "age":    21,
    "grades": [90, 85, 92],
    "active": True
}

# Using dict() constructor
person = dict(name="Bob", age=30, city="Mumbai")
print(person)  # {'name': 'Bob', 'age': 30, 'city': 'Mumbai'}

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# From two lists using zip
keys   = ["name", "age", "city"]
values = ["Carol", 28, "Pune"]
d = dict(zip(keys, values))
print(d)  # {'name': 'Carol', 'age': 28, 'city': 'Pune'}
```

### `fromkeys()` — Pre-fill with Default Value
```python
keys = ["a", "b", "c", "d"]

d1 = dict.fromkeys(keys)       # All values = None
print(d1)  # {'a': None, 'b': None, 'c': None, 'd': None}

d2 = dict.fromkeys(keys, 0)    # All values = 0
print(d2)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0}

d3 = dict.fromkeys(keys, [])   # ⚠️ All share same list!
d3["a"].append(1)
print(d3)  # {'a': [1], 'b': [1], 'c': [1], 'd': [1]} ← all changed!
```

---

## 🎯 Accessing Values

### By Key
```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}

# Direct access — KeyError if missing
print(person["name"])   # Alice
print(person["age"])    # 25

# ❌ KeyError if key doesn't exist
# print(person["phone"])  # KeyError!
```

### `.get()` — Safe Access
```python
person = {"name": "Alice", "age": 25}

# Returns None if key missing (no error!)
print(person.get("name"))     # Alice
print(person.get("phone"))    # None

# Returns default value if key missing
print(person.get("phone", "N/A"))     # N/A
print(person.get("age",   0))         # 25 (key exists)
print(person.get("score", 100))       # 100 (key missing)
```

### Checking Key Existence
```python
person = {"name": "Alice", "age": 25}

print("name" in person)       # True
print("phone" in person)      # False
print("phone" not in person)  # True

# Check value existence
print("Alice" in person.values())  # True
print(25 in person.values())       # True
```

---

## ✏️ Adding & Modifying

```python
person = {"name": "Alice", "age": 25}

# Add new key
person["city"]  = "Delhi"
person["phone"] = "9876543210"
print(person)
# {'name': 'Alice', 'age': 25, 'city': 'Delhi', 'phone': '9876543210'}

# Modify existing key
person["age"]  = 26
person["city"] = "Mumbai"
print(person)
# {'name': 'Alice', 'age': 26, 'city': 'Mumbai', ...}

# Add/update multiple keys at once
person.update({"age": 27, "email": "alice@example.com"})
print(person)

# Using setdefault — add only if key doesn't exist
person.setdefault("age",    99)    # age exists → NOT changed
person.setdefault("hobby", "reading")  # new key → added
print(person["age"])    # 27 (unchanged)
print(person["hobby"])  # reading (added)
```

---

## 🗑️ Deleting Items

```python
person = {"name": "Alice", "age": 25, "city": "Delhi", "phone": "123"}

# del — delete by key (KeyError if missing)
del person["phone"]
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Delhi'}

# pop() — remove & return value
age = person.pop("age")
print(age)     # 25
print(person)  # {'name': 'Alice', 'city': 'Delhi'}

# pop() with default — no error if missing
val = person.pop("country", "Not found")
print(val)     # Not found

# popitem() — remove & return LAST inserted pair (Python 3.7+)
person = {"a": 1, "b": 2, "c": 3}
last = person.popitem()
print(last)    # ('c', 3)
print(person)  # {'a': 1, 'b': 2}

# clear() — remove ALL items
person.clear()
print(person)  # {}
```

---

## 🔧 All Dictionary Methods

Python dicts have **12 built-in methods**. Here's every one:

---

### 1️⃣ `keys()` — Get All Keys

```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}

keys = person.keys()
print(keys)        # dict_keys(['name', 'age', 'city'])
print(list(keys))  # ['name', 'age', 'city']

# 🔥 It's a live view — updates automatically!
person["phone"] = "123"
print(keys)  # dict_keys(['name', 'age', 'city', 'phone']) ← updated!

# Iterate
for key in person.keys():
    print(key)
```

---

### 2️⃣ `values()` — Get All Values

```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}

values = person.values()
print(values)        # dict_values(['Alice', 25, 'Delhi'])
print(list(values))  # ['Alice', 25, 'Delhi']

# Check if a value exists
print("Alice" in person.values())  # True
print(99 in person.values())       # False

# Sum all values
scores = {"math": 90, "english": 85, "science": 92}
print(sum(scores.values()))   # 267
print(max(scores.values()))   # 92
print(min(scores.values()))   # 85
```

---

### 3️⃣ `items()` — Get All Key-Value Pairs

```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}

items = person.items()
print(items)        # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Delhi')])
print(list(items))  # [('name', 'Alice'), ('age', 25), ('city', 'Delhi')]

# Most useful for looping!
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# city: Delhi
```

---

### 4️⃣ `get(key, default)` — Safe Value Lookup

```python
person = {"name": "Alice", "age": 25}

print(person.get("name"))           # Alice
print(person.get("phone"))          # None
print(person.get("phone", "N/A"))   # N/A

# 🔥 Pattern: Count with get()
sentence = "hello world hello python hello"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'hello': 3, 'world': 1, 'python': 1}
```

---

### 5️⃣ `setdefault(key, default)` — Get or Set

```python
d = {"a": 1, "b": 2}

# Key exists → returns existing value, does NOT change it
val = d.setdefault("a", 99)
print(val)   # 1
print(d)     # {'a': 1, 'b': 2}  ← unchanged

# Key missing → sets it and returns default
val = d.setdefault("c", 99)
print(val)   # 99
print(d)     # {'a': 1, 'b': 2, 'c': 99}  ← added!

# 🔥 Pattern: Grouping with setdefault
data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana"), ("veg", "spinach")]
grouped = {}
for category, item in data:
    grouped.setdefault(category, []).append(item)
print(grouped)
# {'fruit': ['apple', 'banana'], 'veg': ['carrot', 'spinach']}
```

---

### 6️⃣ `update(other)` — Merge / Update

```python
person = {"name": "Alice", "age": 25}

# Update with another dict
person.update({"age": 26, "city": "Delhi"})
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'Delhi'}

# Update with keyword arguments
person.update(phone="9876543210", email="alice@gmail.com")
print(person)

# Update with list of tuples
person.update([("hobby", "chess"), ("language", "Python")])
print(person)
```

---

### 7️⃣ `pop(key, default)` — Remove & Return

```python
d = {"a": 1, "b": 2, "c": 3}

val = d.pop("b")         # Returns 2, removes key "b"
print(val)    # 2
print(d)      # {'a': 1, 'c': 3}

val = d.pop("z", "N/A")  # Key missing → returns default
print(val)    # N/A  (no error!)

# ❌ Without default → KeyError if missing
# d.pop("z")  # KeyError!
```

---

### 8️⃣ `popitem()` — Remove & Return Last Pair

```python
d = {"a": 1, "b": 2, "c": 3}

item = d.popitem()
print(item)   # ('c', 3)  ← last inserted
print(d)      # {'a': 1, 'b': 2}

item = d.popitem()
print(item)   # ('b', 2)
print(d)      # {'a': 1}

# ❌ Empty dict → KeyError
# {}.popitem()  # KeyError!
```

---

### 9️⃣ `clear()` — Remove All Items

```python
d = {"a": 1, "b": 2, "c": 3}
d.clear()
print(d)   # {}

# 🆚 clear() vs reassign
d1 = {"a": 1}
d2 = d1          # d2 points to same dict

d1.clear()       # Clears in-place → d2 also {}
print(d2)        # {}

d1 = {"a": 1}
d2 = d1
d1 = {}          # Reassign d1 → d2 still {"a": 1}
print(d2)        # {'a': 1}
```

---

### 🔟 `copy()` — Shallow Copy

```python
original = {"name": "Alice", "scores": [90, 85, 92]}

copy1 = original.copy()
copy1["name"] = "Bob"         # doesn't affect original
print(original["name"])       # Alice ✅

# ⚠️ Shallow copy — nested objects still shared!
copy1["scores"].append(100)
print(original["scores"])     # [90, 85, 92, 100] ← also changed!

# ✅ Deep copy for fully independent copy
import copy
deep = copy.deepcopy(original)
deep["scores"].append(999)
print(original["scores"])     # [90, 85, 92, 100] ← untouched ✅
```

---

### 1️⃣1️⃣ `fromkeys(keys, value)` — Create from Keys

```python
# Class method — called on dict, not an instance
subjects = ["math", "science", "english"]

d1 = dict.fromkeys(subjects)       # Default value = None
print(d1)  # {'math': None, 'science': None, 'english': None}

d2 = dict.fromkeys(subjects, 0)    # All values = 0
print(d2)  # {'math': 0, 'science': 0, 'english': 0}

d3 = dict.fromkeys(subjects, [])   # ⚠️ All share same list!
d3["math"].append(90)
print(d3)  # All subjects now have [90] — shared reference bug!

# ✅ Fix — use comprehension instead
d4 = {k: [] for k in subjects}
d4["math"].append(90)
print(d4)  # {'math': [90], 'science': [], 'english': []}
```

---

### 1️⃣2️⃣ `__contains__` / `in` — Membership (not a method, but key!)

```python
d = {"a": 1, "b": 2, "c": 3}

# in checks KEYS by default
print("a" in d)            # True
print(1 in d)              # False ← not a key!
print(1 in d.values())     # True  ← check values explicitly
print(("a", 1) in d.items())  # True ← check pairs
```

---

## 🔁 Looping Through Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "Delhi"}

# Loop over KEYS (default)
for key in person:
    print(key)
# name  age  city

# Loop over KEYS explicitly
for key in person.keys():
    print(key)

# Loop over VALUES
for value in person.values():
    print(value)
# Alice  25  Delhi

# Loop over KEY-VALUE PAIRS ← most common!
for key, value in person.items():
    print(f"{key} → {value}")
# name → Alice
# age  → 25
# city → Delhi

# Loop with index
for i, (key, value) in enumerate(person.items(), start=1):
    print(f"{i}. {key}: {value}")
# 1. name: Alice
# 2. age: 25
# 3. city: Delhi

# Conditional loop
scores = {"math": 90, "english": 65, "science": 80, "history": 55}
for subject, score in scores.items():
    if score >= 80:
        print(f"✅ {subject}: {score}")
    else:
        print(f"❌ {subject}: {score}")
```

---

## 💡 Dictionary Comprehensions

```
{key_expr: value_expr  for  item  in  iterable  if  condition}
```

### Basic Comprehensions
```python
# Square each number
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Uppercase keys
original = {"name": "alice", "city": "delhi"}
upper_keys = {k.upper(): v for k, v in original.items()}
print(upper_keys)  # {'NAME': 'alice', 'CITY': 'delhi'}

# Uppercase values
upper_vals = {k: v.upper() for k, v in original.items()}
print(upper_vals)  # {'name': 'ALICE', 'city': 'DELHI'}

# Swap keys and values
flipped = {v: k for k, v in original.items()}
print(flipped)  # {'alice': 'name', 'delhi': 'city'}
```

### With Conditions
```python
scores = {"math": 90, "english": 65, "science": 80, "history": 55}

# Only passing scores (>= 70)
passing = {sub: score for sub, score in scores.items() if score >= 70}
print(passing)  # {'math': 90, 'science': 80}

# Grade mapping
grades = {sub: "Pass" if score >= 70 else "Fail"
          for sub, score in scores.items()}
print(grades)
# {'math': 'Pass', 'english': 'Fail', 'science': 'Pass', 'history': 'Fail'}
```

### From Two Lists
```python
keys   = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]

d = {k: v for k, v in zip(keys, values)}
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

## 🗂️ Nested Dictionaries

```python
# Dictionary of dictionaries
company = {
    "Alice": {"dept": "Engineering", "salary": 80000, "age": 28},
    "Bob":   {"dept": "Marketing",   "salary": 60000, "age": 32},
    "Carol": {"dept": "Engineering", "salary": 90000, "age": 35},
}

# Access nested value
print(company["Alice"]["dept"])     # Engineering
print(company["Bob"]["salary"])     # 60000

# Modify nested value
company["Alice"]["salary"] = 85000
print(company["Alice"]["salary"])   # 85000

# Add a new person
company["Dave"] = {"dept": "HR", "salary": 55000, "age": 27}

# Loop through nested dict
for name, info in company.items():
    print(f"\n{name}:")
    for key, val in info.items():
        print(f"  {key}: {val}")

# Safe nested access with .get()
phone = company.get("Alice", {}).get("phone", "N/A")
print(phone)  # N/A (no error even though phone doesn't exist)

# List of dicts (very common!)
students = [
    {"name": "Alice", "gpa": 3.8},
    {"name": "Bob",   "gpa": 3.5},
    {"name": "Carol", "gpa": 3.9},
]

# Sort by gpa
top = sorted(students, key=lambda s: s["gpa"], reverse=True)
print(top[0]["name"])  # Carol

# Filter
honor_roll = [s for s in students if s["gpa"] >= 3.7]
print([s["name"] for s in honor_roll])  # ['Alice', 'Carol']
```

---

## 🔀 Merging Dictionaries

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}   # "b" conflicts!

# Method 1: update() — modifies d1 in-place
d1.update(d2)
print(d1)  # {'a': 1, 'b': 99, 'c': 3}  ← d2 wins on conflict

# Method 2: {**d1, **d2} — new dict (Python 3.5+)
d1 = {"a": 1, "b": 2}
merged = {**d1, **d2}
print(merged)  # {'a': 1, 'b': 99, 'c': 3}  ← d2 wins on conflict
print(d1)      # {'a': 1, 'b': 2}  ← original unchanged!

# Method 3: | operator — new dict (Python 3.9+) 🔥
d1 = {"a": 1, "b": 2}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 99, 'c': 3}

# Method 4: |= operator — in-place (Python 3.9+)
d1 |= d2
print(d1)  # {'a': 1, 'b': 99, 'c': 3}

# d1 wins on conflict (reverse order)
merged = {**d2, **d1}
print(merged)  # {'b': 2, 'c': 3, 'a': 1}  ← d1 wins
```

---

## 🚀 Advanced Techniques

### 🔥 defaultdict — Auto Default Values
```python
from collections import defaultdict

# No KeyError for missing keys!
word_count = defaultdict(int)   # default = 0
for word in "hello world hello python hello".split():
    word_count[word] += 1
print(dict(word_count))  # {'hello': 3, 'world': 1, 'python': 1}

# defaultdict with list
grouped = defaultdict(list)
data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
for category, item in data:
    grouped[category].append(item)
print(dict(grouped))  # {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

# defaultdict with set
graph = defaultdict(set)
edges = [(1, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
print(dict(graph))  # {1: {2,3}, 2: {1,3}, 3: {1,2,4}, 4: {3}}
```

### 🔥 Counter — Count Frequencies
```python
from collections import Counter

# Count characters
text = "hello world"
c = Counter(text)
print(c)  # Counter({'l': 3, 'o': 2, ...})

# Count words
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
c = Counter(words)
print(c)              # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(c["apple"])     # 3
print(c["mango"])     # 0  ← no KeyError!
print(c.most_common(2))  # [('apple', 3), ('banana', 2)]

# Arithmetic on Counters
c1 = Counter({"a": 3, "b": 2})
c2 = Counter({"a": 1, "b": 4, "c": 2})
print(c1 + c2)  # Counter({'b': 6, 'a': 4, 'c': 2})
print(c1 - c2)  # Counter({'a': 2})
```

### 🔥 OrderedDict — Explicit Ordering (pre-3.7)
```python
from collections import OrderedDict

od = OrderedDict()
od["first"]  = 1
od["second"] = 2
od["third"]  = 3

# Move to end / beginning
od.move_to_end("first")
print(list(od.keys()))  # ['second', 'third', 'first']

od.move_to_end("first", last=False)
print(list(od.keys()))  # ['first', 'second', 'third']
```

### 🔥 ChainMap — Chain Multiple Dicts
```python
from collections import ChainMap

defaults = {"theme": "light", "lang": "en",  "size": 12}
user     = {"theme": "dark",  "size": 14}

config = ChainMap(user, defaults)
print(config["theme"])  # dark  ← user overrides
print(config["lang"])   # en    ← from defaults
print(config["size"])   # 14    ← user overrides
```

### 🔥 Invert a Dictionary
```python
d = {"a": 1, "b": 2, "c": 3}

# Simple invert
inverted = {v: k for k, v in d.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}

# Invert with duplicate values → group into lists
d = {"a": 1, "b": 2, "c": 1, "d": 3}
inverted = {}
for k, v in d.items():
    inverted.setdefault(v, []).append(k)
print(inverted)  # {1: ['a', 'c'], 2: ['b'], 3: ['d']}
```

### 🔥 Nested Access Safely
```python
data = {
    "user": {
        "profile": {
            "name": "Alice"
        }
    }
}

# Safe chained get
name = data.get("user", {}).get("profile", {}).get("name", "Unknown")
print(name)  # Alice

missing = data.get("user", {}).get("address", {}).get("city", "N/A")
print(missing)  # N/A  (no error!)
```

### 🔥 Sort a Dictionary
```python
scores = {"math": 90, "english": 65, "science": 80, "history": 55}

# Sort by KEY
sorted_by_key = dict(sorted(scores.items()))
print(sorted_by_key)
# {'english': 65, 'history': 55, 'math': 90, 'science': 80}

# Sort by VALUE
sorted_by_val = dict(sorted(scores.items(), key=lambda x: x[1]))
print(sorted_by_val)
# {'history': 55, 'english': 65, 'science': 80, 'math': 90}

# Sort by value descending
sorted_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_desc)
# {'math': 90, 'science': 80, 'english': 65, 'history': 55}
```

### 🔥 Filter a Dictionary
```python
scores = {"math": 90, "english": 65, "science": 80, "history": 55}

# Keep only passing scores
passing = {k: v for k, v in scores.items() if v >= 70}
print(passing)  # {'math': 90, 'science': 80}

# Filter by key
keep_keys = ["math", "science"]
filtered = {k: v for k, v in scores.items() if k in keep_keys}
print(filtered)  # {'math': 90, 'science': 80}
```

### 🔥 Aggregate / Group Data
```python
employees = [
    {"name": "Alice", "dept": "Eng",  "salary": 80000},
    {"name": "Bob",   "dept": "HR",   "salary": 60000},
    {"name": "Carol", "dept": "Eng",  "salary": 90000},
    {"name": "Dave",  "dept": "HR",   "salary": 55000},
]

# Group by department
from collections import defaultdict
by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept"]].append(emp["name"])
print(dict(by_dept))
# {'Eng': ['Alice', 'Carol'], 'HR': ['Bob', 'Dave']}

# Average salary by department
dept_salary = defaultdict(list)
for emp in employees:
    dept_salary[emp["dept"]].append(emp["salary"])
avg = {dept: sum(sals)/len(sals) for dept, sals in dept_salary.items()}
print(avg)  # {'Eng': 85000.0, 'HR': 57500.0}
```

---

## 📊 Dict vs Other Structures

| Feature         | Dict `{k:v}` | List `[]`  | Set `{}`   | Tuple `()` |
|-----------------|--------------|------------|------------|------------|
| Ordered         | ✅ (3.7+)    | ✅         | ❌         | ✅         |
| Mutable         | ✅           | ✅         | ✅         | ❌         |
| Duplicates      | Keys: ❌     | ✅         | ❌         | ✅         |
| Access by       | Key          | Index      | —          | Index      |
| Lookup speed    | ⚡ O(1)      | 🐢 O(n)    | ⚡ O(1)    | 🐢 O(n)    |
| Use when        | Key-value    | Ordered    | Unique     | Immutable  |

---

## 📋 Quick Cheat Sheet

```python
# ── CREATE ────────────────────────────────────────────────────
{}                           # Empty
{"key": "value"}             # With pair
dict(a=1, b=2)               # Keyword args
dict(zip(keys, values))      # From two lists
dict.fromkeys(keys, default) # Pre-filled

# ── ACCESS ────────────────────────────────────────────────────
d["key"]                     # Direct (KeyError if missing)
d.get("key")                 # Safe (returns None)
d.get("key", default)        # Safe with fallback
"key" in d                   # Check existence

# ── ADD / MODIFY ──────────────────────────────────────────────
d["key"] = value             # Add or update
d.update({...})              # Add/update many
d.setdefault("key", val)     # Add only if missing

# ── DELETE ────────────────────────────────────────────────────
del d["key"]                 # Delete (KeyError if missing)
d.pop("key")                 # Remove & return
d.pop("key", default)        # Safe remove
d.popitem()                  # Remove & return last pair
d.clear()                    # Remove all

# ── VIEWS ─────────────────────────────────────────────────────
d.keys()                     # All keys
d.values()                   # All values
d.items()                    # All (key, value) pairs

# ── LOOP ──────────────────────────────────────────────────────
for k in d:                  # Keys
for v in d.values():         # Values
for k, v in d.items():       # Key-value pairs

# ── COPY ──────────────────────────────────────────────────────
d.copy()                     # Shallow copy
copy.deepcopy(d)             # Deep copy

# ── MERGE ─────────────────────────────────────────────────────
{**d1, **d2}                 # Merge (Python 3.5+)
d1 | d2                      # Merge (Python 3.9+)
d1 |= d2                     # In-place merge (Python 3.9+)

# ── COMPREHENSION ─────────────────────────────────────────────
{k: v for k, v in d.items()}           # Copy
{k: v for k, v in d.items() if cond}   # Filter
{v: k for k, v in d.items()}           # Invert

# ── USEFUL FROM COLLECTIONS ───────────────────────────────────
from collections import defaultdict, Counter, OrderedDict, ChainMap
```

---

## 🧠 Memory Tip — All 12 Methods

```
K — keys()        → All keys
V — values()      → All values
I — items()       → All pairs

G — get()         → Safe access
S — setdefault()  → Get or set
U — update()      → Update many

P — pop()         → Remove & return
PI — popitem()    → Remove last pair
C — clear()       → Clear all

CO — copy()       → Shallow copy
F — fromkeys()    → Create from keys
IN — in           → Membership check

"KVI | GSU | PPC | CFI"
```
