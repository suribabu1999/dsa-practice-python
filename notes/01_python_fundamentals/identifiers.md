# Identifiers

# Notes and examples here
# 🐍 Python Identifiers — Complete Fun Guide

> Learn Python identifiers the **easy and memorable way** 🚀

---

# 🎯 What is an Identifier?

An **Identifier** is the **name given to a variable, function, class, module, or object** in Python.

Think of identifiers as **labels 🏷️ for things in your code**.

Example:

```python
name = "Tarra"
age = 25
```

Here:

| Identifier | Meaning |
|------------|---------|
| `name` | variable identifier |
| `age` | variable identifier |

Python uses these names to **identify data in memory**.

---

# 🧠 Real Life Example

Imagine a classroom 🏫

| Real World | Python |
|-------------|--------|
| Student Name | Identifier |
| Student Data | Value |

Example:

```
Student Name → Tarra
Identifier → name
Value → "Tarra"
```

Python code:

```python
name = "Tarra"
```

---

# ⚙️ Where Identifiers Are Used

Identifiers can represent many things:

| Type | Example |
|-----|------|
| Variable | `age` |
| Function | `calculate_total()` |
| Class | `Car` |
| Module | `math` |
| Object | `user1` |

Example:

```python
age = 25

def greet():
    print("Hello")

class Student:
    pass
```

Identifiers here:

```
age
greet
Student
```

---

# 📜 Rules for Python Identifiers

Python has **strict naming rules**.

---

## Rule 1️⃣ Must Start with Letter or `_`

Valid:

```python
name = "Tarra"
_age = 25
```

Invalid:

```python
1name = "Tarra"
```

❌ Error:

```
SyntaxError
```

---

## Rule 2️⃣ Cannot Start With Number

Wrong:

```python
1user = "Tarra"
```

Correct:

```python
user1 = "Tarra"
```

---

## Rule 3️⃣ Only Letters, Numbers, `_`

Valid:

```python
user_name
user1
_age
```

Invalid:

```python
user-name
user@name
user name
```

❌ These contain special characters.

---

## Rule 4️⃣ Case Sensitive 🔤

Python treats uppercase and lowercase **as different identifiers**.

Example:

```python
age = 25
Age = 30
AGE = 40

print(age)
print(Age)
print(AGE)
```

Output:

```
25
30
40
```

These are **three different identifiers**.

---

## Rule 5️⃣ Cannot Use Python Keywords

Python keywords are **reserved words**.

Example keywords:

```
if
else
while
for
class
def
return
```

Wrong:

```python
class = 10
```

Correct:

```python
class_name = "Python"
```

---

# 📚 Python Keywords List

These **cannot be identifiers**.

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
```

Check keywords using Python:

```python
import keyword

print(keyword.kwlist)
```

---

# ✨ Examples of Valid Identifiers

```python
name
age
student_name
total_price
_count
user1
calculate_total
```

---

# ❌ Examples of Invalid Identifiers

```python
1name
user-name
user name
user@name
class
```

---

# 🧑‍💻 Identifier Naming Best Practices

Good programmers follow **clean naming conventions**.

---

## 🐍 Use Snake Case (Python Standard)

Python recommends **snake_case**.

Example:

```python
user_name
total_price
student_age
```

---

## 🚫 Avoid Single Letters

Bad:

```python
x = 100
```

Good:

```python
total_price = 100
```

---

## 📖 Make Names Meaningful

Bad:

```python
a = 10
b = 20
c = a + b
```

Good:

```python
price = 10
tax = 20
total_price = price + tax
```

---

# 🏆 Real World Example

Example from a **shopping cart program**.

```python
product_name = "Laptop"
product_price = 50000
tax_rate = 0.18

total_price = product_price + (product_price * tax_rate)

print(total_price)
```

Identifiers used:

```
product_name
product_price
tax_rate
total_price
```

---

# 🧪 Quick Practice

### Question 1

Which are valid identifiers?

```
1. user_name
2. 1user
3. user1
4. user-name
```

Answer:

```
user_name
user1
```

---

### Question 2

Is this valid?

```python
class = "Python"
```

❌ No.

---

### Question 3

Are these different?

```python
age
Age
AGE
```

✅ Yes — Python is **case sensitive**.

---

# 🧠 Memory Trick

Remember this rule:

```
Identifier = Name of Something in Python
```

Must follow:

```
Start → Letter or _
Contains → Letters, Numbers, _
Cannot → Use keywords
Case Sensitive
```

---

# 🚀 Final Summary

| Rule | Meaning |
|-----|------|
| Start with letter or `_` | `name`, `_age` |
| Cannot start with number | ❌ `1name` |
| Only letters numbers `_` | ❌ `user-name` |
| Case sensitive | `age ≠ Age` |
| No keywords | ❌ `class` |

---

# 🎉 Congratulations

You now understand **Python Identifiers**!

Next topics you should learn:

1️⃣ Variables  
2️⃣ Data Types  
3️⃣ Operators  
4️⃣ Conditionals  

These build the **foundation of Python programming**.

---

🐍 Happy Coding!