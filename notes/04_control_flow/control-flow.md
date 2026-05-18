# 🐍 Python Control Flow
## Basic to Advanced — The Fun & Complete Guide

> 🧠 **What is Control Flow?**
> By default, Python runs code **line by line, top to bottom**.
> Control flow = **YOU decide** which lines run, which skip, and which repeat.
> It's the difference between a dumb script and a smart program! 🤖

```
Normal code (no control flow):        With control flow:
─────────────────────────────          ──────────────────────────────
Line 1 → runs                          Line 1 → runs
Line 2 → runs                          Line 2 → SKIP (condition false)
Line 3 → runs                          Line 3 → runs 5 TIMES (loop)
Line 4 → runs                          Line 4 → jump to line 8
```

---

## 📚 Table of Contents

1. [if — Basic Condition](#-if--basic-condition)
2. [if-else — Two Paths](#-if-else--two-paths)
3. [if-elif-else — Many Paths](#-if-elif-else--many-paths)
4. [Nested if — Conditions inside Conditions](#-nested-if--conditions-inside-conditions)
5. [Ternary Operator — One-liner if-else](#-ternary-operator--one-liner-if-else)
6. [match-case — Python's Switch](#-match-case--pythons-switch-python-310)
7. [for Loop — Repeat for Each Item](#-for-loop--repeat-for-each-item)
8. [while Loop — Repeat Until False](#-while-loop--repeat-until-false)
9. [break — Exit the Loop](#-break--exit-the-loop)
10. [continue — Skip This Round](#-continue--skip-this-round)
11. [pass — Do Nothing](#-pass--do-nothing)
12. [else on Loops](#-else-on-loops)
13. [range() — The Loop Engine](#-range--the-loop-engine)
14. [enumerate() — Loop with Index](#-enumerate--loop-with-index)
15. [zip() — Loop Multiple Lists](#-zip--loop-multiple-lists)
16. [List Comprehensions](#-list-comprehensions)
17. [Dict & Set Comprehensions](#-dict--set-comprehensions)
18. [Generator Expressions](#-generator-expressions)
19. [Nested Loops](#-nested-loops)
20. [Common Patterns & Recipes](#-common-patterns--recipes)
21. [Common Mistakes](#-common-mistakes)
22. [Quick Cheat Sheet](#-quick-cheat-sheet)

---

## 🚦 if — Basic Condition

> **"Only do this IF the condition is True"**

```python
# Syntax
if condition:
    # this block runs ONLY if condition is True
    do_something()

# 🔑 condition must evaluate to True or False
# 🔑 the body MUST be indented (4 spaces)
```

```python
# 🌡️ Temperature Check
temperature = 38

if temperature > 37.5:
    print("🤒 You have a fever!")
    print("💊 Please rest and drink water.")

print("✅ Check complete.")    # always runs (outside if block)

# Output:
# 🤒 You have a fever!
# 💊 Please rest and drink water.
# ✅ Check complete.
```

```python
# ✅ Any expression that gives True/False works as condition
age    = 20
name   = "Alice"
items  = [1, 2, 3]
score  = 0

if age >= 18:           # comparison      → True
    print("Adult")

if name:                # truthy string   → True (non-empty)
    print("Has name")

if items:               # truthy list     → True (non-empty)
    print("Has items")

if not score:           # falsy int       → True (0 is falsy!)
    print("No score yet")

if "py" in "python":    # membership      → True
    print("Found!")
```

---

## 🛤️ if-else — Two Paths

> **"Do THIS if true, do THAT if false"**

```python
if condition:
    # runs when True  ✅
else:
    # runs when False ❌
```

```python
# 🎫 Age Verification
age = 16

if age >= 18:
    print("🎉 Welcome! You can enter.")
    print("🍺 Enjoy responsibly.")
else:
    print("🚫 Sorry, you're too young.")
    print(f"   Come back in {18 - age} year(s)!")

# Output:
# 🚫 Sorry, you're too young.
#    Come back in 2 year(s)!
```

```python
# 🏦 ATM Machine
balance       = 5000
withdraw_amount = 3000

if withdraw_amount <= balance:
    balance -= withdraw_amount
    print(f"✅ Withdrawal successful!")
    print(f"💰 Remaining balance: ₹{balance}")
else:
    shortfall = withdraw_amount - balance
    print(f"❌ Insufficient funds!")
    print(f"   You need ₹{shortfall} more.")

# Output:
# ✅ Withdrawal successful!
# 💰 Remaining balance: ₹2000
```

---

## 🌿 if-elif-else — Many Paths

> **"Check multiple conditions one by one. First True wins."**

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 False AND condition2 True
elif condition3:
    # runs if condition1,2 False AND condition3 True
else:
    # runs if ALL conditions above are False
```

> 💡 **Only ONE block ever runs** — whichever condition is True first.
> Once a match is found, the rest are completely skipped!

```python
# 🎓 Grade Calculator
score = 82

if score >= 90:
    grade = "A ⭐"
    remark = "Outstanding!"
elif score >= 80:
    grade = "B 👍"
    remark = "Very Good!"
elif score >= 70:
    grade = "C 🙂"
    remark = "Good, keep improving."
elif score >= 60:
    grade = "D 📚"
    remark = "Needs more effort."
else:
    grade = "F 😢"
    remark = "Please study harder."

print(f"Score : {score}")
print(f"Grade : {grade}")
print(f"Remark: {remark}")

# Output:
# Score : 82
# Grade : B 👍
# Remark: Very Good!
```

```python
# 🌤️ Weather Advisor
temp = 15    # in Celsius

if temp >= 35:
    advice = "🥵 Very hot! Stay indoors, drink water."
elif temp >= 25:
    advice = "☀️  Warm day! Light clothes."
elif temp >= 15:
    advice = "🌤️  Pleasant! Jacket optional."
elif temp >= 5:
    advice = "🧥 Cold! Wear a jacket."
else:
    advice = "🥶 Freezing! Bundle up!"

print(f"🌡️  Temp: {temp}°C")
print(f"💬 {advice}")

# Output:
# 🌡️  Temp: 15°C
# 💬 🌤️  Pleasant! Jacket optional.
```

### ⚠️ Order matters! First True wins.

```python
x = 85

# ❌ Wrong order — catches too early!
if x > 50:
    print("Greater than 50")       # This fires for 85
elif x > 80:
    print("Greater than 80")       # NEVER REACHED for 85

# ✅ Correct — most specific first!
if x > 80:
    print("Greater than 80")       # Fires! ✅
elif x > 50:
    print("Greater than 50")       # Skipped
```

---

## 🪆 Nested if — Conditions inside Conditions

```python
# 🎢 Ride Eligibility (height AND age AND health)
height    = 155
age       = 16
has_heart = False

if height >= 150:
    print("✅ Height OK")
    if age >= 14:
        print("✅ Age OK")
        if not has_heart:
            print("✅ Health OK")
            print("🎢 Enjoy the ride!")
        else:
            print("❌ Heart condition detected. Sorry!")
    else:
        print(f"❌ Must be at least 14. You need {14-age} more years.")
else:
    print(f"❌ Too short! Need {150-height}cm more.")

# Output:
# ✅ Height OK
# ✅ Age OK
# ✅ Health OK
# 🎢 Enjoy the ride!
```

> 💡 **Tip:** Deep nesting (more than 2–3 levels) = hard to read.
> Try to flatten with `and` / `or` or early returns in functions!

```python
# ❌ Deeply nested (hard to read)
if a:
    if b:
        if c:
            do_something()

# ✅ Flattened with and (much cleaner!)
if a and b and c:
    do_something()
```

---

## ⚡ Ternary Operator — One-liner if-else

```python
# Syntax:
value = thing_if_true  if  condition  else  thing_if_false

#        ┌── result when True    ┌── condition    ┌── result when False
result =     "yes"           if    x > 0      else    "no"
```

```python
# 🔢 Simple examples
age    = 20
status = "Adult" if age >= 18 else "Minor"
print(status)    # Adult

score  = 75
grade  = "Pass ✅" if score >= 60 else "Fail ❌"
print(grade)     # Pass ✅

# 🌡️ Inside f-string (very useful!)
temp   = 30
print(f"It's {'hot 🥵' if temp > 28 else 'cool 😎'} today!")
# It's hot 🥵 today!

# 🔢 Even/odd check
num   = 7
parity = "even" if num % 2 == 0 else "odd"
print(f"{num} is {parity}")    # 7 is odd
```

```python
# 🛒 Discount Calculator
price      = 1200
is_member  = True

final_price = price * 0.80 if is_member else price * 0.95
print(f"💰 You pay: ₹{final_price:.0f}")
# 💰 You pay: ₹960
```

> ⚠️ Don't chain multiple ternaries — it becomes unreadable!
> ```python
> # ❌ Too confusing
> x = "a" if p else "b" if q else "c" if r else "d"
>
> # ✅ Use if-elif-else instead
> ```

---

## 🎛️ match-case — Python's Switch (Python 3.10+)

> Python 3.10 introduced `match-case` — like a cleaner alternative to many `elif`s!

```python
# Syntax
match variable:
    case value1:
        # runs if variable == value1
    case value2:
        # runs if variable == value2
    case _:
        # default — runs if nothing matched (like else)
```

```python
# 🚦 Traffic Light
light = "red"

match light:
    case "red":
        print("🔴 STOP!")
    case "yellow":
        print("🟡 Get ready...")
    case "green":
        print("🟢 GO!")
    case _:
        print("❓ Unknown signal!")

# Output: 🔴 STOP!
```

```python
# 🎮 Command Processor
command = "quit"

match command:
    case "start":
        print("🎮 Game starting...")
    case "pause":
        print("⏸️  Game paused.")
    case "resume":
        print("▶️  Game resumed.")
    case "quit" | "exit":       # ← OR pattern!
        print("👋 Goodbye!")
    case _:
        print(f"❓ Unknown command: '{command}'")

# Output: 👋 Goodbye!
```

```python
# 🏆 Match with conditions (guards)
score = 87

match score:
    case s if s >= 90:
        print(f"Grade A ⭐ ({s})")
    case s if s >= 80:
        print(f"Grade B 👍 ({s})")
    case s if s >= 70:
        print(f"Grade C 🙂 ({s})")
    case _:
        print("Grade F 😢")

# Output: Grade B 👍 (87)
```

```python
# 🧩 Match with structures (advanced!)
point = (0, 5)

match point:
    case (0, 0):
        print("📍 Origin")
    case (x, 0):
        print(f"📍 On X-axis at {x}")
    case (0, y):
        print(f"📍 On Y-axis at {y}")
    case (x, y):
        print(f"📍 Point at ({x}, {y})")

# Output: 📍 On Y-axis at 5
```

---

## 🔁 for Loop — Repeat for Each Item

> **"Do this FOR EACH item in a collection"**

```python
for item in collection:
    # runs once per item
    do_something(item)
```

```python
# 📋 Loop over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"🍎 I like {fruit}!")

# 🍎 I like apple!
# 🍎 I like banana!
# 🍎 I like cherry!
```

```python
# 📝 Loop over a string (character by character!)
word = "Python"

for letter in word:
    print(letter, end=" ")    # P y t h o n
print()    # newline
```

```python
# 🔑 Loop over dictionary
person = {"name": "Alice", "age": 25, "city": "Mumbai"}

# Keys only (default)
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Keys AND values ← most common!
for key, value in person.items():
    print(f"  {key}: {value}")

# Output:
#   name: Alice
#   age: 25
#   city: Mumbai
```

```python
# 🎯 Loop over a set
colors = {"red", "green", "blue"}

for color in colors:
    print(f"🎨 {color}")    # order not guaranteed!
```

---

## ⏳ while Loop — Repeat Until False

> **"Keep doing this WHILE the condition is True"**
> Use when you **don't know** in advance how many times to repeat.

```python
while condition:
    # runs as long as condition is True
    do_something()
    # ⚠️ MUST eventually make condition False or infinite loop!
```

```python
# 🔢 Count down
countdown = 5

while countdown > 0:
    print(f"⏳ {countdown}...")
    countdown -= 1    # ← makes condition eventually False!

print("🚀 Blastoff!")

# Output:
# ⏳ 5...
# ⏳ 4...
# ⏳ 3...
# ⏳ 2...
# ⏳ 1...
# 🚀 Blastoff!
```

```python
# 🎮 Simple Number Guessing Game
secret = 42
guess  = 0

while guess != secret:
    guess = int(input("Guess a number: "))
    if guess < secret:
        print("📉 Too low!")
    elif guess > secret:
        print("📈 Too high!")

print("🎉 You got it!")
```

```python
# 🔄 Input validation loop (very common pattern!)
while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break    # ← valid input, exit loop
    print("⚠️ Please enter a valid positive number!")

print(f"✅ Age recorded: {age}")
```

---

## 💥 break — Exit the Loop

> **"STOP the loop immediately, right now!"**

```python
# break exits the ENTIRE loop
for i in range(10):
    if i == 5:
        break          # 💥 Stop here!
    print(i)

# Output: 0 1 2 3 4     (5 never printed)
```

```python
# 🔍 Search — stop when found!
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target   = "Charlie"
found    = False

for student in students:
    if student == target:
        found = True
        break    # 💥 No need to check the rest!

if found:
    print(f"✅ Found {target}!")
else:
    print(f"❌ {target} not found.")
```

```python
# 🍕 Pizza Ordering — stop when done
toppings = []

while True:
    topping = input("Add topping (or 'done'): ")
    if topping.lower() == "done":
        break    # 💥 User is done
    toppings.append(topping)
    print(f"✅ Added: {topping}")

print(f"🍕 Your pizza: {', '.join(toppings)}")
```

### break in nested loops

```python
# ⚠️ break only exits the INNERMOST loop!
for i in range(3):
    for j in range(3):
        if j == 1:
            break    # exits inner loop only
        print(f"({i},{j})", end=" ")
    print()

# Output:
# (0,0)
# (1,0)
# (2,0)
```

---

## ⏭️ continue — Skip This Round

> **"Skip the rest of THIS iteration, go to the NEXT one"**

```python
# continue skips to the next iteration
for i in range(6):
    if i == 3:
        continue    # ⏭️ Skip 3!
    print(i, end=" ")

# Output: 0 1 2 4 5    (3 is skipped)
```

```python
# 🧹 Skip invalid data
data = [10, -5, 0, 25, -3, 42, 0, 8]

print("Valid positive numbers:")
for num in data:
    if num <= 0:
        continue    # ⏭️ Skip zeros and negatives
    print(f"  ✅ {num}")

# Output:
#   ✅ 10
#   ✅ 25
#   ✅ 42
#   ✅ 8
```

```python
# 📚 Skip already-processed items
processed = {"Alice", "Bob"}
all_users = ["Alice", "Bob", "Charlie", "Diana"]

for user in all_users:
    if user in processed:
        print(f"⏭️  Skipping {user} (already done)")
        continue
    print(f"⚙️  Processing {user}...")
    processed.add(user)

# ⏭️  Skipping Alice (already done)
# ⏭️  Skipping Bob (already done)
# ⚙️  Processing Charlie...
# ⚙️  Processing Diana...
```

---

## 🤫 pass — Do Nothing

> **"This is intentionally empty."**
> A placeholder so Python doesn't complain about empty blocks.

```python
# ❌ Empty block crashes!
if True:
    # nothing here
    # SyntaxError!

# ✅ pass fixes it
if True:
    pass    # "I'll fill this in later"

# 🏗️ Placeholder functions/classes
def process_data():
    pass    # TODO: implement later

class Animal:
    pass    # TODO: add methods later

# 🔕 Intentionally ignore an error
try:
    risky_operation()
except Exception:
    pass    # silently ignore (use carefully!)
```

---

## 🔁➕ else on Loops

> Python has a **unique** feature: `else` on `for` and `while` loops!
> The `else` block runs only if the loop **finished normally** (no `break`)!

```python
# for...else
for item in collection:
    if condition:
        break
else:
    # runs ONLY if loop completed without break
    print("Loop finished normally!")
```

```python
# 🔍 Search with for-else (elegant!)
numbers = [3, 7, 12, 19, 25]
target  = 15

for num in numbers:
    if num == target:
        print(f"✅ Found {target}!")
        break
else:
    # Only runs if we never broke (never found it)
    print(f"❌ {target} not in list.")

# Output: ❌ 15 not in list.
```

```python
# 🔐 Login attempt with while-else
attempts  = 3
password  = "secret123"

while attempts > 0:
    guess = input(f"Password ({attempts} tries left): ")
    if guess == password:
        print("✅ Access granted!")
        break
    attempts -= 1
    print("❌ Wrong password!")
else:
    # Runs only if while condition became False (no break)
    print("🔒 Account locked! Too many attempts.")
```

---

## 🎰 range() — The Loop Engine

> `range()` generates a sequence of numbers — perfect for loops!

```python
# 3 forms of range():
range(stop)              # 0, 1, 2, ..., stop-1
range(start, stop)       # start, start+1, ..., stop-1
range(start, stop, step) # start, start+step, ..., < stop
```

```python
# 📊 Examples
list(range(5))           # [0, 1, 2, 3, 4]
list(range(2, 7))        # [2, 3, 4, 5, 6]
list(range(0, 10, 2))    # [0, 2, 4, 6, 8]    ← evens
list(range(10, 0, -1))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  ← countdown
list(range(5, -1, -1))   # [5, 4, 3, 2, 1, 0]
```

```python
# 🔢 Common usage patterns
# 1️⃣ Repeat N times
for _ in range(5):         # _ = "don't care about index"
    print("Hello! 👋")

# 2️⃣ Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 3️⃣ Print multiplication table
n = 7
for i in range(1, 11):
    print(f"  {n} × {i:2} = {n*i:3}")

# 4️⃣ Draw a pattern
for i in range(1, 6):
    print("⭐" * i)
# ⭐
# ⭐⭐
# ⭐⭐⭐
# ⭐⭐⭐⭐
# ⭐⭐⭐⭐⭐

# 5️⃣ Even numbers only
for n in range(0, 21, 2):
    print(n, end=" ")    # 0 2 4 6 8 10 12 14 16 18 20
```

---

## 🏷️ enumerate() — Loop with Index

> Get **both index and value** without manual counting!

```python
# Without enumerate (clunky) 😴
fruits = ["apple", "banana", "cherry"]
i = 0
for fruit in fruits:
    print(f"{i}: {fruit}")
    i += 1

# With enumerate (clean!) 😎
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start counting from 1 instead of 0!
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

```python
# 🏆 Leaderboard
scores = [95, 88, 76, 65, 52]
names  = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

medals = ["🥇", "🥈", "🥉"]

print("🏆 LEADERBOARD")
print("─" * 30)
for rank, (name, score) in enumerate(zip(names, scores), start=1):
    medal = medals[rank-1] if rank <= 3 else f"  {rank}."
    print(f"  {medal} {name:<10} {score}")
```

---

## 🤐 zip() — Loop Multiple Lists

> Loop over **two or more** lists **at the same time**!

```python
names  = ["Alice", "Bob", "Charlie"]
scores = [88,      92,    75       ]
cities = ["Delhi", "Mumbai", "Chennai"]

# zip pairs them up!
for name, score, city in zip(names, scores, cities):
    print(f"👤 {name} | 🏆 {score} | 🏙️  {city}")

# 👤 Alice   | 🏆 88 | 🏙️  Delhi
# 👤 Bob     | 🏆 92 | 🏙️  Mumbai
# 👤 Charlie | 🏆 75 | 🏙️  Chennai
```

```python
# ⚠️ zip stops at the SHORTEST list
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]

for x, y in zip(a, b):
    print(x, y)
# 1 a
# 2 b
# 3 c    ← stops here! 4 and 5 are lost

# Use zip_longest to keep all:
from itertools import zip_longest
for x, y in zip_longest(a, b, fillvalue="?"):
    print(x, y)
# 1 a  2 b  3 c  4 ?  5 ?
```

```python
# 🔄 Unzip — split pairs back apart
pairs   = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)      # (1, 2, 3)
print(letters)   # ('a', 'b', 'c')
```

---

## 💎 List Comprehensions

> Create a new list in **ONE elegant line**!

```python
# Without comprehension (verbose) 😴
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)    # [1, 4, 9, 16, 25]

# With comprehension (elegant!) 💎
squares = [n ** 2 for n in range(1, 6)]
print(squares)    # [1, 4, 9, 16, 25]
```

```python
# Anatomy of a comprehension:
# [ expression  for  item  in  iterable  if  condition ]
#       ↑              ↑           ↑            ↑
#   what to make   variable   what to loop   optional filter
```

```python
# 🎯 Plenty of examples!

# 1️⃣ Squares of 1–10
squares = [x**2 for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2️⃣ ONLY even numbers
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 3️⃣ Uppercase names
names = ["alice", "bob", "charlie"]
upper = [name.title() for name in names]
# ['Alice', 'Bob', 'Charlie']

# 4️⃣ Filter and transform together
scores  = [85, 42, 91, 37, 73, 60]
passing = [s for s in scores if s >= 60]
# [85, 91, 73, 60]

# 5️⃣ With if-else in expression (ternary!)
labels = ["pass" if s >= 60 else "fail" for s in scores]
# ['pass', 'fail', 'pass', 'fail', 'pass', 'pass']

# 6️⃣ From string
vowels = [c for c in "hello world" if c in "aeiou"]
# ['e', 'o', 'o']

# 7️⃣ Flatten a nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat   = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# 🔗 Real Example — clean and process data
raw = ["  Alice ", "BOB", "", "charlie ", "  "]

cleaned = [
    name.strip().title()
    for name in raw
    if name.strip()      # ← skip empty/whitespace-only strings
]
print(cleaned)   # ['Alice', 'Bob', 'Charlie']
```

---

## 🗂️ Dict & Set Comprehensions

### Dict Comprehension

```python
# { key: value for item in iterable if condition }

# 🔢 Squares as dict
squares = {n: n**2 for n in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 🔄 Flip a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
flipped  = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# 🧹 Filter a dictionary
inventory = {"apple": 50, "banana": 0, "cherry": 30, "mango": 0}
in_stock  = {item: qty for item, qty in inventory.items() if qty > 0}
# {'apple': 50, 'cherry': 30}

# 📊 Word frequency
text  = "the cat sat on the mat the cat"
words = text.split()
freq  = {word: words.count(word) for word in set(words)}
# {'on': 1, 'sat': 1, 'mat': 1, 'the': 3, 'cat': 2}
```

### Set Comprehension

```python
# { expression for item in iterable if condition }

# Unique squares
nums    = [1, -1, 2, -2, 3, 3, -3]
squares = {n**2 for n in nums}
# {1, 4, 9}

# Unique first letters
names  = ["Alice", "Bob", "Anna", "Brian", "Charlie"]
firsts = {name[0] for name in names}
# {'A', 'B', 'C'}
```

---

## ⚙️ Generator Expressions

> Like list comprehensions but **lazy** — computes one at a time, saves memory!

```python
# List comprehension — creates full list in memory
squares_list = [x**2 for x in range(1_000_000)]   # 🐘 uses lots of RAM

# Generator expression — creates items one by one
squares_gen  = (x**2 for x in range(1_000_000))    # 🪶 uses barely any RAM
```

```python
# Use () instead of []
gen = (x**2 for x in range(5))
print(next(gen))   # 0   ← compute one at a time
print(next(gen))   # 1
print(next(gen))   # 4

# Or just iterate
for val in (x**2 for x in range(5)):
    print(val, end=" ")    # 0 1 4 9 16
```

```python
# 💡 Great for one-time calculations
total   = sum(x**2 for x in range(1000))         # sum of squares
maximum = max(len(name) for name in names)        # longest name length
any_pass = any(s >= 60 for s in scores)           # anyone passing?
all_pass = all(s >= 60 for s in scores)           # everyone passing?
```

---

## 🪆 Nested Loops

> A loop inside a loop. Inner loop completes **fully** for each outer iteration.

```python
# 📊 Multiplication Table
print("  ×  |", end="")
for i in range(1, 6):
    print(f" {i:2}", end="")
print("\n" + "─"*20)

for i in range(1, 6):
    print(f"  {i}  |", end="")
    for j in range(1, 6):
        print(f" {i*j:2}", end="")
    print()

#   ×  |  1  2  3  4  5
# ────────────────────
#   1  |  1  2  3  4  5
#   2  |  2  4  6  8 10
#   3  |  3  6  9 12 15
#   4  |  4  8 12 16 20
#   5  |  5 10 15 20 25
```

```python
# ⭐ Star Patterns
# Right triangle
rows = 5
for i in range(1, rows+1):
    print("⭐" * i)
# ⭐
# ⭐⭐
# ⭐⭐⭐
# ⭐⭐⭐⭐
# ⭐⭐⭐⭐⭐

# Pyramid
for i in range(1, rows+1):
    spaces = " " * (rows - i)
    stars  = "⭐" * (2*i - 1)
    print(spaces + stars)
#     ⭐
#    ⭐⭐⭐
#   ⭐⭐⭐⭐⭐
#  ⭐⭐⭐⭐⭐⭐⭐
# ⭐⭐⭐⭐⭐⭐⭐⭐⭐
```

```python
# 🔍 Searching in 2D (nested list)
classroom = [
    ["Alice", "Bob",     "Charlie"],
    ["Diana", "Eve",     "Frank"  ],
    ["Grace", "Heidi",   "Ivan"   ],
]

target = "Eve"
for row_idx, row in enumerate(classroom):
    for col_idx, name in enumerate(row):
        if name == target:
            print(f"✅ Found '{target}' at row {row_idx}, seat {col_idx}")
            break   # breaks inner loop only!

# ✅ Found 'Eve' at row 1, seat 1
```

---

## 🍳 Common Patterns & Recipes

### Pattern 1: Accumulator 📊

```python
# Collect results as you loop
numbers = [3, 7, 2, 9, 1, 6, 4, 8, 5]

total   = 0
maximum = numbers[0]
minimum = numbers[0]
evens   = []

for n in numbers:
    total += n                        # accumulate sum
    if n > maximum: maximum = n      # track max
    if n < minimum: minimum = n      # track min
    if n % 2 == 0: evens.append(n)  # collect evens

print(f"Total   : {total}")
print(f"Average : {total/len(numbers):.1f}")
print(f"Max     : {maximum}")
print(f"Min     : {minimum}")
print(f"Evens   : {evens}")
```

### Pattern 2: Flag Variable 🚩

```python
# Use a boolean flag to track something across the loop
numbers = [4, 8, 15, 16, 23, 42]
found_prime = False

for n in numbers:
    is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
    if is_prime:
        print(f"🔢 Found prime: {n}")
        found_prime = True

if not found_prime:
    print("No primes found.")
```

### Pattern 3: Group / Bucket items 🪣

```python
students = [
    ("Alice", 88), ("Bob", 45), ("Charlie", 72),
    ("Diana", 91), ("Eve", 55), ("Frank", 83),
]

passed  = []
failed  = []

for name, score in students:
    if score >= 60:
        passed.append(name)
    else:
        failed.append(name)

print(f"✅ Passed ({len(passed)}): {', '.join(passed)}")
print(f"❌ Failed ({len(failed)}): {', '.join(failed)}")
```

### Pattern 4: Running Total / Moving Window 📈

```python
# Daily sales — show running total
daily_sales = [1200, 850, 2100, 1750, 900, 3000, 1400]
running_total = 0

print("📅 Day | 💰 Sales | 📈 Running Total")
print("─" * 40)
for day, sale in enumerate(daily_sales, 1):
    running_total += sale
    print(f"  Day {day}  | ₹{sale:>6,}  | ₹{running_total:>9,}")
```

### Pattern 5: Early Exit (guard clause) 🚪

```python
def find_first_negative(numbers):
    for n in numbers:
        if n < 0:
            return n    # exit immediately when found
    return None         # only if nothing found

result = find_first_negative([3, 7, -2, 9, -5])
print(result)    # -2
```

### Pattern 6: Sliding Window 🪟

```python
data   = [10, 20, 30, 40, 50, 60, 70]
window = 3

print(f"📊 {window}-day moving averages:")
for i in range(len(data) - window + 1):
    chunk   = data[i : i + window]
    avg     = sum(chunk) / window
    print(f"  Days {i+1}-{i+window}: {chunk} → avg {avg:.1f}")

# Days 1-3: [10, 20, 30] → avg 20.0
# Days 2-4: [20, 30, 40] → avg 30.0
# Days 3-5: [30, 40, 50] → avg 40.0
# Days 4-6: [40, 50, 60] → avg 50.0
# Days 5-7: [50, 60, 70] → avg 60.0
```

---

## 🚨 Common Mistakes

### 1. Off-by-one in range 🔢

```python
# ❌ range(5) gives 0,1,2,3,4 — NOT 5!
for i in range(5):
    print(i)    # prints 0 to 4

# ✅ If you want 1 to 5:
for i in range(1, 6):
    print(i)    # prints 1 to 5
```

### 2. Modifying a list while iterating 😱

```python
nums = [1, 2, 3, 4, 5]

# ❌ Dangerous! Skips items!
for n in nums:
    if n % 2 == 0:
        nums.remove(n)

print(nums)    # [1, 3, 5]  ← looks right but may skip items!

# ✅ Iterate over a copy instead
for n in nums[:]:        # nums[:] is a copy
    if n % 2 == 0:
        nums.remove(n)

# ✅ Or use list comprehension
nums = [n for n in nums if n % 2 != 0]
```

### 3. Infinite while loop 🔄♾️

```python
# ❌ Forgot to update the condition variable!
n = 0
while n < 5:
    print(n)
    # FORGOT: n += 1   ← infinite loop! Ctrl+C to stop!

# ✅ Always update something that will eventually make condition False
n = 0
while n < 5:
    print(n)
    n += 1    # ← must be here!
```

### 4. Using = instead of == in conditions 💥

```python
x = 5

# ❌ Assignment inside if — SyntaxError in Python (but bugs in other languages)
if x = 5:     # SyntaxError!
    print("yes")

# ✅ Always == for comparison
if x == 5:
    print("yes")
```

### 5. Misunderstanding break vs continue ⚡

```python
for i in range(5):
    if i == 3:
        break        # 💥 EXITS loop: 0 1 2
    print(i)

for i in range(5):
    if i == 3:
        continue     # ⏭️ SKIPS 3: 0 1 2 4
    print(i)
```

### 6. Comparing with == instead of is for None ⚠️

```python
result = None

# ❌ Not wrong, but not Pythonic
if result == None:
    print("empty")

# ✅ Always use 'is' for None
if result is None:
    print("empty")
```

---

## 📝 Quick Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚦 CONDITIONALS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Basic if
if x > 0:
    print("positive")

# if-else
if x > 0:
    print("positive")
else:
    print("non-positive")

# if-elif-else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary
result = "yes" if x > 0 else "no"

# match-case (3.10+)
match command:
    case "quit":  exit()
    case "go":    move()
    case _:       print("unknown")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔁 LOOPS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# for loop
for item in collection:
    process(item)

# for with range
for i in range(10):
    print(i)

# for with enumerate
for i, item in enumerate(collection, start=1):
    print(i, item)

# for with zip
for a, b in zip(list1, list2):
    print(a, b)

# while loop
while condition:
    do_something()
    update_condition()

# while True (manual break)
while True:
    if done:
        break

# break / continue / pass
for x in items:
    if skip_this: continue    # next iteration
    if stop_now:  break       # exit loop
    if todo:      pass        # placeholder

# Loop else
for x in items:
    if found: break
else:
    print("not found")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💎 COMPREHENSIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# List
evens   = [x for x in range(10) if x%2==0]
squares = [x**2 for x in range(5)]

# Dict
d = {k: v for k, v in pairs}
d = {k: v for k, v in d.items() if v > 0}

# Set
s = {x**2 for x in range(5)}

# Generator
g = (x**2 for x in range(1000000))
total = sum(x**2 for x in range(1000))
```

---

## 🎓 Final Summary

```
Control Flow Tools:
─────────────────────────────────────────────────────
if              → Run code conditionally
if-elif-else    → Choose one of many paths
ternary         → One-liner conditional assignment
match-case      → Pattern matching (3.10+)

for             → Loop over a sequence
while           → Loop while condition is True
break           → Exit the loop NOW
continue        → Skip to next iteration
pass            → Do nothing (placeholder)
else on loop    → Run if loop ended without break

range()         → Generate number sequences
enumerate()     → Loop with index
zip()           → Loop multiple sequences together

List comp       → [expr for x in iter if cond]
Dict comp       → {k: v for x in iter if cond}
Set comp        → {expr for x in iter if cond}
Generator       → (expr for x in iter if cond)
─────────────────────────────────────────────────────
```

---

> 🚀 **Control flow is the brain of your program!**
> Without it, code is just a list of steps.
> With it, your code makes decisions, repeats tasks, and reacts to data.
>
> **Master these and you can build ANYTHING! 🏗️🐍✨**