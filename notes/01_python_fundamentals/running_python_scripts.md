# 🐍 Running Python Scripts — From Code to Execution 🚀

> Writing Python code is only half the job.  
> The next step is **running the Python script** so the computer executes it.

A Python file usually ends with:

```
.py
```

Example:

```
hello.py
```

---

# 🎯 What is a Python Script?

A **Python Script** is simply a file that contains Python code.

Example:

```
hello.py
```

Code inside:

```python
print("Hello Python")
```

This file becomes a **Python program** when we run it.

---

# 📂 Creating a Python Script

### Step 1

Create a file:

```
hello.py
```

### Step 2

Write code:

```python
print("My first Python script")
```

### Step 3

Save the file.

---

# ▶️ Running Python Script from Terminal

Open terminal or command prompt.

Navigate to your folder.

Example:

```
cd Desktop
```

Then run:

```
python hello.py
```

Output:

```
My first Python script
```

Congratulations 🎉  
You just ran your first Python program.

---

# 🖥 Running Script on Windows

Open **Command Prompt**.

Run:

```
python filename.py
```

Example:

```
python hello.py
```

---

# 🖥 Running Script on Mac / Linux

Open **Terminal**.

Run:

```
python3 filename.py
```

Example:

```
python3 hello.py
```

---

# 📂 Running Python Script in VS Code

Steps:

1️⃣ Open VS Code  
2️⃣ Open your Python file  
3️⃣ Click **Run Button ▶️**

OR

Press:

```
Ctrl + F5
```

---

# 🧪 Example Python Script

File:

```
sum.py
```

Code:

```python
a = 10
b = 20

print("Sum =", a + b)
```

Run:

```
python sum.py
```

Output:

```
Sum = 30
```

---

# 🧠 What Happens When You Run a Script?

Execution process:

```
Python Script (.py)
        ↓
Python Interpreter
        ↓
Bytecode (.pyc)
        ↓
Python Virtual Machine
        ↓
Output
```

Python converts code into **bytecode**, then executes it.

---

# 🧩 Script Mode vs Interactive Mode

| Feature | Script Mode | Interactive Mode |
|------|------|------|
| Execution | Whole file | Line by line |
| Usage | Real programs | Testing |
| Example | `python file.py` | `>>>` prompt |

---

# 🎮 Example Program

File:

```
greet.py
```

Code:

```python
name = input("Enter your name: ")

print("Hello", name)
```

Run:

```
python greet.py
```

Example Output:

```
Enter your name: Tarra
Hello Tarra
```

---

# ⚡ Running Python Script with Arguments

You can pass arguments to a script.

Example file:

```
args.py
```

Code:

```python
import sys

print(sys.argv)
```

Run:

```
python args.py hello world
```

Output:

```
['args.py', 'hello', 'world']
```

---

# 🧠 Making Python Script Executable (Linux / Mac)

Add this line at the top:

```python
#!/usr/bin/env python3
```

Example:

```python
#!/usr/bin/env python3

print("Hello from executable script")
```

Then run:

```
chmod +x hello.py
./hello.py
```

---

# ⚠️ Common Errors

---

## ❌ Python Not Found

Error:

```
python is not recognized
```

Solution:

Add Python to **PATH** during installation.

---

## ❌ File Not Found

Error:

```
can't open file
```

Solution:

Make sure you are in the **correct directory**.

---

## ❌ Syntax Error

Example:

```python
print("Hello
```

Error:

```
SyntaxError
```

Fix the code.

---

# 🧪 Mini Project Example

File:

```
calculator.py
```

Code:

```python
a = int(input("Enter number: "))
b = int(input("Enter number: "))

print("Sum:", a + b)
```

Run:

```
python calculator.py
```

Output:

```
Enter number: 10
Enter number: 5
Sum: 15
```

---

# 🧠 Memory Trick

Remember:

```
Write Code
    ↓
Save .py file
    ↓
Run python filename.py
    ↓
Get Output
```

---

# 🧪 Practice Questions

### Question 1

Which command runs a Python script?

Answer:

```
python filename.py
```

---

### Question 2

What extension do Python scripts use?

Answer:

```
.py
```

---

### Question 3

Which module is used for command-line arguments?

Answer:

```
sys
```

---

# 🏆 Summary

| Concept | Meaning |
|------|------|
| Python Script | File containing Python code |
| Extension | `.py` |
| Run Command | `python filename.py` |
| Execution | Interpreter executes code |

---

# 🚀 What's Next?

After learning how to run scripts, learn:

```
Identifiers
Variables
Data Types
Operators
Input / Output
Conditionals
Loops
Functions
```

These are the **core building blocks of Python**.

---

# 🎉 Final Thought

Running Python scripts turns:

```
Code → Real Programs 🚀
```

Now you are officially **executing Python programs like a developer** 🧑‍💻.

---

🐍 Happy Coding!