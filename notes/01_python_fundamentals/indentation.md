# Indentation

# Notes and examples here
# 🐍 Python Indentation — The Backbone of Python Code

> In Python, **indentation is not just style — it is syntax!**  
> That means Python **uses spaces to understand code structure**.

Think of indentation like **tabs in a notebook 📒** that group ideas together.

---

# 🎯 What is Indentation?

**Indentation = spaces at the beginning of a line of code.**

Python uses indentation to define **blocks of code**.

Example:

```python
if True:
    print("Hello")
```

Here:

```
if True:
    print("Hello")
```

The **4 spaces before `print()`** tell Python that this line belongs to the `if` block.

---

# 🧠 Real Life Example

Imagine instructions for making tea ☕

```
Make Tea
    Boil water
    Add tea powder
    Add milk
Serve
```

Indented steps belong to **"Make Tea"**.

Python works exactly the same way.

---

# ⚙️ Why Indentation is Important in Python

Other languages use **curly braces `{}`**.

Example in **C / Java / JavaScript**:

```javascript
if (x > 10) {
   console.log("Big");
}
```

Python replaces `{}` with **indentation**.

Python version:

```python
if x > 10:
    print("Big")
```

Cleaner and easier to read ✨.

---

# 📜 Basic Indentation Rules

---

## Rule 1️⃣ Use 4 Spaces (Python Standard)

Python style guide (**PEP 8**) recommends **4 spaces**.

Example:

```python
if True:
    print("Hello")
```

---

## Rule 2️⃣ Same Block = Same Indentation

Correct:

```python
if True:
    print("Line 1")
    print("Line 2")
```

Wrong:

```python
if True:
    print("Line 1")
       print("Line 2")
```

❌ Error:

```
IndentationError
```

---

## Rule 3️⃣ Indentation Defines Code Blocks

Example:

```python
age = 20

if age > 18:
    print("Adult")
    print("Can vote")

print("Done")
```

Explanation:

```
if block
    print
    print

outside block
print("Done")
```

Output:

```
Adult
Can vote
Done
```

---

# 🚨 Indentation Errors

Python throws errors if indentation is wrong.

Example:

```python
if True:
print("Hello")
```

Error:

```
IndentationError: expected an indented block
```

Correct:

```python
if True:
    print("Hello")
```

---

# ⚠️ Mixing Tabs and Spaces

Python **does not allow mixing tabs and spaces**.

Bad:

```
(tab)print("Hello")
(space space space space)print("World")
```

Error:

```
TabError: inconsistent use of tabs and spaces
```

Best practice:

✅ Always use **4 spaces**.

---

# 📦 Indentation with If Statements

Example:

```python
temperature = 35

if temperature > 30:
    print("Hot day")
```

Indentation shows that **print belongs to if block**.

---

# 🔁 Indentation with Loops

Example:

```python
for i in range(3):
    print(i)
```

Output:

```
0
1
2
```

Without indentation Python would not know **what belongs to the loop**.

---

# 🧩 Indentation in Functions

Example:

```python
def greet():
    print("Hello")
    print("Welcome")
```

Everything indented belongs to the **function body**.

---

# 🏗 Nested Indentation (Blocks inside Blocks)

Example:

```python
age = 25

if age > 18:
    print("Adult")

    if age > 21:
        print("Can drink in some countries")
```

Structure:

```
if
    print
    if
        print
```

---

# 🧑‍💻 Real World Example

Example: Login check.

```python
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
```

Indentation makes this **easy to understand**.

---

# 🧠 Visual Understanding

Bad indentation:

```
if condition:
print("Hello")
print("World")
```

Python confusion 😵

Good indentation:

```
if condition:
    print("Hello")
    print("World")
```

Python understands perfectly ✅.

---

# 🎯 Best Practices

### ✔ Always use 4 spaces

```
    correct
```

---

### ✔ Keep indentation consistent

Wrong:

```
    line
        line
   line
```

---

### ✔ Use an IDE or editor

Editors automatically indent:

- VS Code
- PyCharm
- Jupyter Notebook

---

# 🧪 Practice Questions

### Question 1

Find the error:

```python
if True:
print("Hello")
```

---

### Question 2

Predict output:

```python
if True:
    print("A")
    print("B")
print("C")
```

Answer:

```
A
B
C
```

---

### Question 3

What happens?

```python
for i in range(2):
print(i)
```

Answer:

```
IndentationError
```

---

# 🏆 Memory Trick

Remember this:

```
Python uses indentation instead of {}
```

And:

```
Block of code = same indentation
```

---

# 🚀 Final Summary

| Concept | Meaning |
|------|------|
| Indentation | Spaces at start of line |
| Purpose | Define code blocks |
| Standard | 4 spaces |
| Error | IndentationError |
| Best Practice | Consistent indentation |

---

# 🎉 Congratulations

You now understand **Python Indentation — one of the most important Python concepts**.

Without indentation **Python code cannot run**.

---

🐍 Happy Coding!