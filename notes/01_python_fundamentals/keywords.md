# 🐍 Python Keywords — The Reserved Power Words

> Keywords are **special reserved words in Python** that have predefined meanings.

You **cannot use them as variable names, function names, or identifiers** ❌

Think of keywords as **VIP words 👑** — only Python can use them.

---

# 🎯 What Are Keywords?

Keywords are words that:

✔ Have special meaning  
✔ Are part of Python syntax  
✔ Cannot be used as identifiers  

Example:

```python
if True:
    print("Hello")
```

Here:

```
if
True
```

are Python keywords.

---

# 🧠 Why Keywords Are Important

Keywords define:

- Conditions (`if`, `else`)
- Loops (`for`, `while`)
- Functions (`def`, `return`)
- Classes (`class`)
- Exception handling (`try`, `except`)
- Boolean logic (`and`, `or`, `not`)

Without keywords, Python cannot function 🚀.

---

# 📜 Complete List of Python Keywords (Python 3)

```
False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
match
case
```

(Note: `match` and `case` were introduced in Python 3.10.)

---

# 🧪 How to Check Keywords in Python

Python provides a built-in module:

```python
import keyword

print(keyword.kwlist)
```

Output:

```
[List of keywords]
```

---

# 🚫 You Cannot Use Keywords as Identifiers

Wrong ❌

```python
class = 10
```

Correct ✅

```python
class_name = 10
```

---

# 📂 Categories of Keywords (Easy Understanding)

Let’s group keywords logically.

---

# 1️⃣ Conditional Keywords

Used for decision making.

```
if
elif
else
match
case
```

Example:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# 2️⃣ Loop Keywords

Used for repetition.

```
for
while
break
continue
```

Example:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

# 3️⃣ Function Keywords

Used for creating functions.

```
def
return
lambda
```

Example:

```python
def greet():
    return "Hello"
```

---

# 4️⃣ Class & OOP Keywords

```
class
self (not keyword but convention)
global
nonlocal
```

Example:

```python
class Student:
    pass
```

---

# 5️⃣ Boolean & Logical Keywords

```
True
False
None
and
or
not
is
in
```

Example:

```python
if True and False:
    print("Impossible")
```

---

# 6️⃣ Exception Handling Keywords

```
try
except
finally
raise
assert
```

Example:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error")
```

---

# 7️⃣ Import Keywords

```
import
from
as
```

Example:

```python
from math import sqrt as square_root
```

---

# 8️⃣ Async Programming Keywords

```
async
await
```

Used in asynchronous programming.

Example:

```python
async def fetch_data():
    await some_function()
```

---

# 🧠 Memory Trick to Remember Keywords

Think in categories:

```
Conditions → if, else, elif
Loops → for, while
Functions → def, return
OOP → class
Logic → and, or, not
Errors → try, except
Import → import, from
```

Don’t try to memorize all at once 😅  
Use them naturally while coding.

---

# ⚠️ Case Sensitivity

Keywords are **case-sensitive**.

Correct:

```python
True
False
None
```

Wrong:

```python
true
false
none
```

---

# 🧪 Practice Questions

### Question 1

Is this valid?

```python
if = 10
```

❌ No.

---

### Question 2

Which of these are keywords?

```
1. for
2. total
3. return
4. data
```

Answer:

```
for
return
```

---

### Question 3

What happens?

```python
True = False
```

❌ SyntaxError

---

# 🏆 Real World Example

Example combining multiple keywords:

```python
def login(user):
    if user is None:
        return False
    else:
        return True
```

Keywords used:

```
def
if
is
None
return
else
True
False
```

---

# 🚀 Summary

| Concept | Meaning |
|------|------|
| Keywords | Reserved words |
| Can we use as variable? | ❌ No |
| Case sensitive? | ✅ Yes |
| Total keywords | Around 35+ |

---

# 🎉 Congratulations

You now understand **Python Keywords**.

They are the **building blocks of Python syntax** 🧱.

---

# 📚 Next Topics

After keywords, learn:

1️⃣ Variables  
2️⃣ Data Types  
3️⃣ Operators  
4️⃣ Input / Output  
5️⃣ Conditional Statements  
6️⃣ Loops  

These will make your Python foundation strong 💪.

---

🐍 Happy Coding!