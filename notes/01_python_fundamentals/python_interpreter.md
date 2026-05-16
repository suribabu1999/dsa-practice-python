# Python Interpreter

# Notes and examples here
# 🐍 Python Interpreter — The Brain Behind Python Code

> The **Python Interpreter** is the program that **reads and executes Python code**.

It acts like a **translator 🧠** that converts Python code into instructions the computer understands.

---

# 🎯 What is a Python Interpreter?

A **Python Interpreter** is software that:

✔ Reads Python code  
✔ Converts it into machine instructions  
✔ Executes the code line by line  

Flow:

```
Python Code
     ↓
Python Interpreter
     ↓
Machine Instructions
     ↓
Output
```

Without the interpreter, Python code **cannot run**.

---

# 🧠 Why Python is Called an Interpreted Language

Python executes code **line by line** instead of compiling everything first.

Example:

```python
print("Hello")
print("Python")
```

Execution flow:

```
Line 1 → Execute
Line 2 → Execute
```

This makes debugging easier.

---

# ⚙️ How Python Code Actually Runs

When you run:

```
python program.py
```

The process is:

```
Python Source Code (.py)
        ↓
Python Compiler
        ↓
Bytecode (.pyc)
        ↓
Python Virtual Machine (PVM)
        ↓
Output
```

So internally Python:

1️⃣ Compiles code to **bytecode**  
2️⃣ Executes bytecode using **Python Virtual Machine**

---

# 📦 Components of Python Interpreter

Python execution has two major components.

---

# 1️⃣ Python Compiler

The compiler converts:

```
Python code → Bytecode
```

Example:

```python
x = 10
print(x)
```

Converted into **bytecode instructions**.

Bytecode is stored in:

```
__pycache__
```

Example file:

```
program.cpython-312.pyc
```

---

# 2️⃣ Python Virtual Machine (PVM)

The **Python Virtual Machine** executes bytecode.

Think of it as:

```
Python CPU
```

It reads bytecode instructions and runs them.

---

# 🖥 Types of Python Interpreter Modes

Python has **two main execution modes**.

---

# 1️⃣ Interactive Mode (REPL)

REPL means:

```
Read
Evaluate
Print
Loop
```

Start it by running:

```
python
```

You will see:

```
>>>
```

Example:

```python
>>> 5 + 5
10
```

Python instantly returns the result.

---

# 2️⃣ Script Mode

In script mode, Python executes a **file**.

Example file:

```
program.py
```

Code:

```python
print("Hello Python")
```

Run using:

```
python program.py
```

Output:

```
Hello Python
```

---

# 🧩 Interactive vs Script Mode

| Feature | Interactive Mode | Script Mode |
|------|------|------|
| Execution | Line by line | Entire file |
| Best for | Testing code | Real programs |
| Prompt | `>>>` | No prompt |

---

# 🧪 Example — Interactive Mode

Open terminal:

```
python
```

Then type:

```python
>>> name = "Tarra"
>>> print(name)
```

Output:

```
Tarra
```

Exit interpreter:

```
exit()
```

or

```
Ctrl + Z + Enter
```

---

# ⚡ Example — Script Mode

Create file:

```
sum.py
```

Code:

```python
a = 5
b = 10

print(a + b)
```

Run:

```
python sum.py
```

Output:

```
15
```

---

# 🧠 Advantages of Python Interpreter

✔ Easy debugging  
✔ Quick execution  
✔ Interactive testing  
✔ Portable across systems  

Perfect for:

```
Learning
Automation
Prototyping
AI experiments
```

---

# ⚠️ Disadvantages

Because Python is interpreted:

❌ Slower than compiled languages  
❌ Runtime errors appear during execution  

Example:

```python
print(x)
```

Error:

```
NameError: x is not defined
```

---

# 🏗 Popular Python Interpreters

Different implementations exist.

| Interpreter | Description |
|------|------|
| CPython | Default Python interpreter |
| PyPy | Faster implementation |
| Jython | Python on JVM |
| IronPython | Python on .NET |

Most developers use:

```
CPython
```

---

# 🧠 Memory Trick

Remember:

```
Python Interpreter = Code Runner
```

Steps:

```
.py file
   ↓
Bytecode
   ↓
Python Virtual Machine
   ↓
Output
```

---

# 🧪 Practice Questions

### Question 1

What does REPL stand for?

Answer:

```
Read Evaluate Print Loop
```

---

### Question 2

Which file extension stores Python bytecode?

Answer:

```
.pyc
```

---

### Question 3

Which interpreter is the default Python implementation?

Answer:

```
CPython
```

---

# 🏆 Summary

| Concept | Explanation |
|------|------|
| Python Interpreter | Executes Python code |
| Execution type | Interpreted |
| Bytecode file | `.pyc` |
| Execution engine | Python Virtual Machine |

---

# 🚀 What's Next?

After learning Python interpreter, continue with:

```
Variables
Data Types
Operators
Input / Output
Conditionals
Loops
Functions
```

These are the **core foundations of Python programming**.

---

# 🎉 Final Thought

The Python Interpreter is the **engine that makes Python programs run**.

Without it:

```
Python code = Just text
```

With it:

```
Python code = Running program 🚀
```

---

🐍 Happy Coding!