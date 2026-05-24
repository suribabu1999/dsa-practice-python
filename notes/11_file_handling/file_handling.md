# 🐍 Python File Handling — Zero to Hero
## Every Mode · Every Method · Every Pattern · Advanced Mastery

> 🧠 **What is File Handling?**
> File handling is how Python **reads from** and **writes to** files on disk.
> Without it, your program forgets everything when it stops running.
> With it, your data **lives forever** — saved in files, ready to load again.
>
> Think of a file like a **notebook** 📓:
> - You can **open** it (open)
> - **Read** what's written (read)
> - **Write** new things (write)
> - **Add** to existing content (append)
> - **Close** it when done (close)
>
> Python makes all of this beautifully simple. Let's go! 🚀

---

## 📚 Table of Contents

1. [Opening & Closing Files](#-opening--closing-files)
2. [File Modes — Every Single One](#-file-modes--every-single-one)
3. [Reading Files — Every Method](#-reading-files--every-method)
4. [Writing Files — Every Method](#-writing-files--every-method)
5. [The with Statement — Context Manager](#-the-with-statement--context-manager)
6. [File Object Methods & Attributes](#-file-object-methods--attributes)
7. [Working with Text Files](#-working-with-text-files)
8. [Working with Binary Files](#-working-with-binary-files)
9. [CSV Files](#-csv-files)
10. [JSON Files](#-json-files)
11. [os Module — File System Operations](#-os-module--file-system-operations)
12. [pathlib Module — Modern Path Handling](#-pathlib-module--modern-path-handling)
13. [shutil Module — File Operations](#-shutil-module--file-operations)
14. [File Exceptions & Error Handling](#-file-exceptions--error-handling)
15. [Real-World Projects](#-real-world-projects)
16. [Common Mistakes](#-common-mistakes)
17. [Cheat Sheet](#-cheat-sheet)

---

## 📂 Opening & Closing Files

> The gateway to all file operations is the built-in `open()` function.

```python
# Syntax:
# open(file, mode='r', encoding=None, errors=None, newline=None)
#       ↑       ↑           ↑
#     path    how?       text encoding (use 'utf-8' always!)
```

```python
# ─── The manual way (old style) ───
file = open("hello.txt", "r")   # open
content = file.read()           # use
file.close()                    # MUST close — or data is lost / file locked!

# ─── The problem: if an error happens before close()... ───
file = open("data.txt", "r")
data = file.read()
# ... if something crashes here ...
file.close()   # ← this might NEVER run! 😱
```

```python
# ─── The RIGHT way — with statement (always use this!) ───
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
# File is automatically closed here — no matter what happens! ✅
```

```python
# ─── Opening multiple files at once ───
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    data = infile.read()
    outfile.write(data.upper())
# Both files closed automatically ✅
```

---

## 🔑 File Modes — Every Single One

```
Mode  │ Read │ Write │ Create │ Truncate │ Position │ Description
──────┼──────┼───────┼────────┼──────────┼──────────┼──────────────────────────
'r'   │  ✅  │  ❌   │   ❌   │    ❌    │  Start   │ Read only (default)
'w'   │  ❌  │  ✅   │   ✅   │    ✅    │  Start   │ Write only — WIPES existing!
'a'   │  ❌  │  ✅   │   ✅   │    ❌    │   End    │ Append — adds to end
'x'   │  ❌  │  ✅   │   ✅   │    ❌    │  Start   │ Exclusive create — fails if exists
'r+'  │  ✅  │  ✅   │   ❌   │    ❌    │  Start   │ Read + Write (file must exist)
'w+'  │  ✅  │  ✅   │   ✅   │    ✅    │  Start   │ Read + Write — WIPES existing!
'a+'  │  ✅  │  ✅   │   ✅   │    ❌    │  Start/E │ Read + Append
──────┼──────┼───────┼────────┼──────────┼──────────┼──────────────────────────
Add 'b' for binary mode:  'rb', 'wb', 'ab', 'rb+', 'wb+'
```

```python
# ─── 'r' — Read only (file must exist) ───
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# FileNotFoundError if file doesn't exist!

# ─── 'w' — Write only (creates OR overwrites!) ───
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!")
# ⚠️ If output.txt had content → IT'S GONE! Wiped completely.

# ─── 'a' — Append (creates if needed, adds to end) ───
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
# ✅ Safe — existing content preserved!

# ─── 'x' — Exclusive create (fails if file exists) ───
try:
    with open("new_file.txt", "x", encoding="utf-8") as f:
        f.write("Brand new file!")
except FileExistsError:
    print("File already exists! Won't overwrite.")

# ─── 'r+' — Read AND Write ───
with open("data.txt", "r+", encoding="utf-8") as f:
    content = f.read()         # read first
    f.seek(0)                  # go back to start
    f.write("NEW START\n")     # overwrite from beginning

# ─── Binary modes ───
with open("image.png", "rb") as f:      # read binary
    data = f.read()

with open("copy.png", "wb") as f:       # write binary
    f.write(data)
```

---

## 📖 Reading Files — Every Method

---

### read() — Read entire file at once

```python
# Returns entire file content as ONE string
with open("story.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
print(type(content))   # <class 'str'>

# ─── read(n) — Read exactly n characters ───
with open("data.txt", "r", encoding="utf-8") as f:
    first_10  = f.read(10)   # first 10 characters
    next_10   = f.read(10)   # next 10 (cursor moved!)
    rest      = f.read()     # everything remaining
```

```python
# ─── Real example — read a config file ───
with open("config.txt", "r", encoding="utf-8") as f:
    config = f.read()

print(f"File size: {len(config)} characters")
print(f"Preview: {config[:100]}...")
```

---

### readline() — Read one line at a time

```python
# Returns ONE line including the \n at the end
# Returns '' (empty string) when file is exhausted

with open("data.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()   # "Hello\n"
    line2 = f.readline()   # "World\n"
    line3 = f.readline()   # "Python\n"
    line4 = f.readline()   # ""  ← end of file!

print(repr(line1))   # 'Hello\n'
print(line1.strip()) # 'Hello'   ← strip removes \n
```

```python
# ─── Read all lines with readline() in a loop ───
with open("data.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:        # empty string = end of file
            break
        print(line.strip())
```

---

### readlines() — Read all lines into a list

```python
# Returns a LIST of strings, each ending with \n
with open("names.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)
# ['Alice\n', 'Bob\n', 'Charlie\n', 'Diana\n']

# Strip newlines
clean_lines = [line.strip() for line in lines]
print(clean_lines)
# ['Alice', 'Bob', 'Charlie', 'Diana']

# ─── readlines(hint) — read approximately 'hint' bytes ───
with open("big_file.txt", "r") as f:
    chunk = f.readlines(1024)   # read approx 1KB worth of lines
```

---

### Iterating Directly — Best for Large Files! ⭐

```python
# Most memory-efficient — reads ONE line at a time, never all at once!
with open("huge_file.txt", "r", encoding="utf-8") as f:
    for line in f:             # iterate file object directly!
        print(line.strip())    # process one line at a time

# ─── Real example — process a large log file ───
error_count  = 0
errors       = []

with open("server.log", "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        if "ERROR" in line:
            error_count += 1
            errors.append(f"Line {line_num}: {line.strip()}")

print(f"Found {error_count} errors")
for e in errors[:5]:   # show first 5
    print(f"  {e}")
```

---

### Comparison: Which Read Method to Use?

```python
# read()       → small files, need entire content as string
# readline()   → process line by line manually, custom logic
# readlines()  → need all lines as a list, file fits in memory
# for line in f → LARGE files, memory-efficient, most Pythonic ✅
```

---

## ✍️ Writing Files — Every Method

---

### write() — Write a string

```python
# Returns: number of characters written
with open("output.txt", "w", encoding="utf-8") as f:
    chars_written = f.write("Hello, World!\n")
    print(chars_written)   # 14

    f.write("Line 2\n")
    f.write("Line 3\n")
# File contains:
# Hello, World!
# Line 2
# Line 3
```

```python
# ─── ⚠️ write() does NOT add \n automatically! ───
with open("test.txt", "w") as f:
    f.write("Line 1")    # no newline!
    f.write("Line 2")    # runs into Line 1!
# File: "Line 1Line 2"  ← all on one line!

# ✅ Always add \n yourself:
with open("test.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

---

### writelines() — Write a list of strings

```python
# Writes each item in the list — does NOT add \n between them!
lines = ["Alice\n", "Bob\n", "Charlie\n", "Diana\n"]

with open("names.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
# File:
# Alice
# Bob
# Charlie
# Diana

# ─── Generate lines and write ───
data = ["apple", "banana", "cherry", "mango"]

with open("fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(f"{item}\n" for item in data)   # generator!
```

---

### print() to file — Convenient!

```python
# print() has a file parameter!
with open("output.txt", "w", encoding="utf-8") as f:
    print("Hello, World!", file=f)        # auto adds \n ✅
    print("Line 2", file=f)
    print("Score:", 95, file=f)           # works like normal print!
    print("Items:", 1, 2, 3, sep=", ", file=f)
# Advantage: auto adds newline, handles non-strings automatically!
```

---

## 🛡️ The with Statement — Context Manager

> `with` is the **safest, most Pythonic** way to handle files.
> It **guarantees** the file is closed — even if an exception occurs!

```python
# Without with — risky:
f = open("data.txt", "r")
data = int(f.read())   # ← if this crashes, f.close() never runs!
f.close()              # ← might never execute!

# With with — safe:
with open("data.txt", "r") as f:
    data = int(f.read())   # ← if this crashes...
# ...file is STILL closed here. ✅ Always.
```

```python
# ─── How it works under the hood ───
# with open(...) as f:
#     ...
#
# Is equivalent to:
f = open(...)
try:
    ...
finally:
    f.close()   # always runs!
```

```python
# ─── Nested with statements ───
with open("input.txt", "r") as src, open("output.txt", "w") as dst:
    for line in src:
        dst.write(line.upper())

# ─── Custom context manager using contextlib ───
from contextlib import contextmanager

@contextmanager
def open_with_backup(filename):
    """Open a file and create a backup before writing."""
    import shutil, os
    if os.path.exists(filename):
        shutil.copy(filename, filename + ".bak")
    f = open(filename, "w", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        print(f"  ✅ File saved: {filename}")

with open_with_backup("important.txt") as f:
    f.write("Critical data here!")
```

---

## 🔧 File Object Methods & Attributes

```python
with open("sample.txt", "r+", encoding="utf-8") as f:

    # ─── tell() — current position in file (bytes) ───
    print(f.tell())      # 0  ← at the start

    f.read(5)
    print(f.tell())      # 5  ← moved 5 bytes forward

    # ─── seek(offset, whence) — move to a position ───
    f.seek(0)            # go to beginning
    f.seek(0, 0)         # same — 0 = from start
    f.seek(0, 1)         # 0 bytes from current position
    f.seek(0, 2)         # go to END of file

    f.seek(10)           # go to byte 10
    print(f.tell())      # 10

    # ─── readable(), writable(), seekable() ───
    print(f.readable())    # True
    print(f.writable())    # True  (opened with r+)
    print(f.seekable())    # True

    # ─── name — filename ───
    print(f.name)          # 'sample.txt'

    # ─── mode — open mode ───
    print(f.mode)          # 'r+'

    # ─── closed — is the file closed? ───
    print(f.closed)        # False (still open)

print(f.closed)            # True  (after with block)

# ─── flush() — force write buffer to disk ───
with open("log.txt", "a") as f:
    f.write("Important entry\n")
    f.flush()    # ensure it's written NOW (useful for real-time logs)
```

---

## 📄 Working with Text Files

---

### Encoding — Always Specify It!

```python
# ❌ Never rely on default encoding (platform-dependent!)
f = open("data.txt", "r")   # might use 'cp1252' on Windows!

# ✅ Always specify encoding explicitly:
f = open("data.txt", "r", encoding="utf-8")     # Unicode, most files
f = open("data.txt", "r", encoding="utf-16")    # Windows word files
f = open("data.txt", "r", encoding="latin-1")   # Western European
f = open("data.txt", "r", encoding="ascii")     # ASCII only

# ─── Handle encoding errors ───
with open("messy.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()    # silently skip undecodable bytes

with open("messy.txt", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()    # replace bad bytes with '?'
```

---

### Reading Line by Line — Real Examples

```python
# ─── Count lines, words, characters ───
def file_stats(filename):
    """Return line, word, and char count for a file."""
    lines = words = chars = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return lines, words, chars

l, w, c = file_stats("essay.txt")
print(f"Lines: {l}  Words: {w}  Chars: {c}")
```

```python
# ─── Find and replace in a file ───
def find_replace(filename, old, new):
    """Replace all occurrences of 'old' with 'new' in a file."""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    updated = content.replace(old, new)
    count   = content.count(old)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"  Replaced {count} occurrence(s) of '{old}' → '{new}'")

find_replace("config.txt", "localhost", "192.168.1.100")
```

```python
# ─── Filter lines matching a pattern ───
import re

def grep(filename, pattern):
    """Return all lines matching a regex pattern."""
    results = []
    with open(filename, "r", encoding="utf-8") as f:
        for num, line in enumerate(f, 1):
            if re.search(pattern, line, re.IGNORECASE):
                results.append((num, line.rstrip()))
    return results

matches = grep("server.log", r"ERROR|CRITICAL")
for num, line in matches:
    print(f"  Line {num:4}: {line}")
```

```python
# ─── Read specific line numbers ───
def read_lines(filename, line_numbers):
    """Read specific line numbers from a file."""
    target = set(line_numbers)
    result = {}
    with open(filename, "r", encoding="utf-8") as f:
        for num, line in enumerate(f, 1):
            if num in target:
                result[num] = line.rstrip()
            if num > max(target):
                break
    return result

lines = read_lines("data.txt", [1, 5, 10, 15])
for num, content in lines.items():
    print(f"  Line {num}: {content}")
```

```python
# ─── Tail — read last N lines (like Unix tail) ───
from collections import deque

def tail(filename, n=10):
    """Return the last n lines of a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return list(deque(f, maxlen=n))

last_lines = tail("server.log", 5)
for line in last_lines:
    print(line.rstrip())
```

```python
# ─── Merge multiple files ───
def merge_files(output_file, *input_files):
    """Merge multiple text files into one."""
    with open(output_file, "w", encoding="utf-8") as outf:
        for filename in input_files:
            outf.write(f"{'='*40}\n")
            outf.write(f"FILE: {filename}\n")
            outf.write(f"{'='*40}\n")
            with open(filename, "r", encoding="utf-8") as inf:
                outf.write(inf.read())
            outf.write("\n")
    print(f"  ✅ Merged {len(input_files)} files into {output_file}")
```

---

## 🔢 Working with Binary Files

```python
# ─── Copy a binary file (image, audio, video) ───
def copy_file(src, dst):
    """Copy a binary file from src to dst."""
    CHUNK_SIZE = 64 * 1024   # 64KB chunks

    with open(src, "rb") as source, open(dst, "wb") as dest:
        while True:
            chunk = source.read(CHUNK_SIZE)
            if not chunk:
                break
            dest.write(chunk)

    print(f"  ✅ Copied {src} → {dst}")

copy_file("photo.jpg", "photo_backup.jpg")
```

```python
# ─── Read file as bytes ───
with open("image.png", "rb") as f:
    header = f.read(8)   # PNG files start with these 8 bytes
    print(header)        # b'\x89PNG\r\n\x1a\n'
    print(list(header))  # [137, 80, 78, 71, 13, 10, 26, 10]

# ─── Check file signature (magic bytes) ───
MAGIC_BYTES = {
    b'\x89PNG':  "PNG image",
    b'\xff\xd8': "JPEG image",
    b'PK':       "ZIP archive",
    b'%PDF':     "PDF document",
    b'GIF8':     "GIF image",
}

def identify_file(filename):
    with open(filename, "rb") as f:
        header = f.read(4)
    for magic, filetype in MAGIC_BYTES.items():
        if header.startswith(magic):
            return filetype
    return "Unknown file type"
```

```python
# ─── Write binary data ───
import struct

# Write a simple binary record: name(20 bytes) + score(int 4 bytes)
with open("scores.bin", "wb") as f:
    records = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
    for name, score in records:
        name_bytes = name.encode("utf-8").ljust(20, b'\x00')  # pad to 20 bytes
        score_bytes = struct.pack("I", score)                   # 4-byte unsigned int
        f.write(name_bytes + score_bytes)

# Read back binary records
with open("scores.bin", "rb") as f:
    RECORD_SIZE = 24   # 20 + 4 bytes
    while True:
        data = f.read(RECORD_SIZE)
        if not data: break
        name  = data[:20].rstrip(b'\x00').decode("utf-8")
        score = struct.unpack("I", data[20:])[0]
        print(f"  {name}: {score}")
```

---

## 📊 CSV Files

```python
import csv

# ─── Write CSV ───
students = [
    ["Name",    "Age", "Score", "Grade"],
    ["Alice",    20,    92,     "A"   ],
    ["Bob",      22,    85,     "B"   ],
    ["Charlie",  21,    78,     "C"   ],
    ["Diana",    20,    95,     "A"   ],
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)   # write all at once

print("  ✅ CSV written")
```

```python
# ─── Read CSV ───
with open("students.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)   # skip header row
    print(f"  Columns: {header}")
    for row in reader:
        name, age, score, grade = row
        print(f"  {name:<10} Age:{age}  Score:{score}  Grade:{grade}")
```

```python
# ─── DictWriter — write with column names ───
students = [
    {"name": "Alice",   "age": 20, "score": 92, "grade": "A"},
    {"name": "Bob",     "age": 22, "score": 85, "grade": "B"},
    {"name": "Charlie", "age": 21, "score": 78, "grade": "C"},
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "score", "grade"]
    writer     = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()        # writes the header row
    writer.writerows(students)  # writes all data rows
```

```python
# ─── DictReader — read as dicts ───
with open("students.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # each row is an OrderedDict!
        print(f"  {row['name']:<10} Score: {row['score']}")
```

```python
# ─── Advanced CSV — custom delimiter, quoting ───
# Tab-separated values (TSV)
with open("data.tsv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["Name", "City", "Score"])
    writer.writerow(["Alice", "New York", 95])

# Semicolon-separated (common in Europe)
with open("data_eu.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Name;Age;Score"])
```

```python
# ─── CSV → dict of lists for analysis ───
def load_csv(filename):
    """Load CSV into a dict of column lists."""
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data   = {field: [] for field in reader.fieldnames}
        for row in reader:
            for field in reader.fieldnames:
                data[field].append(row[field])
    return data

data   = load_csv("students.csv")
scores = [int(s) for s in data["score"]]
print(f"  Avg Score: {sum(scores)/len(scores):.1f}")
print(f"  Top Score: {max(scores)}")
```

---

## 🗃️ JSON Files

```python
import json

# ─── Write JSON ───
data = {
    "app":     "MyApp",
    "version": "2.1.0",
    "users": [
        {"id": 1, "name": "Alice", "role": "admin",  "active": True},
        {"id": 2, "name": "Bob",   "role": "user",   "active": True},
        {"id": 3, "name": "Carol", "role": "user",   "active": False},
    ],
    "config": {
        "max_users":   100,
        "timeout_sec": 30,
        "debug":       False,
    }
}

with open("app_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
#           ↑      ↑     ↑             ↑
#         data  file  pretty      allow unicode

print("  ✅ JSON written")
```

```python
# ─── Read JSON ───
with open("app_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["app"])           # MyApp
print(loaded["version"])       # 2.1.0
print(len(loaded["users"]))    # 3

for user in loaded["users"]:
    status = "✅" if user["active"] else "❌"
    print(f"  {status} {user['name']:<10} ({user['role']})")
```

```python
# ─── json.dumps / json.loads — string versions ───
# dumps → dict to JSON string
# loads → JSON string to dict

config = {"debug": True, "port": 8080}
json_str = json.dumps(config, indent=2)
print(json_str)
# {
#   "debug": true,
#   "port": 8080
# }

restored = json.loads(json_str)
print(restored["port"])   # 8080
```

```python
# ─── Pretty print JSON file ───
def pretty_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps(data, indent=2, ensure_ascii=False))

pretty_json("app_data.json")
```

```python
# ─── Update JSON file safely ───
def update_json(filename, updates):
    """Load a JSON file, apply updates, save back."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data.update(updates)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

update_json("config.json", {"debug": False, "version": "3.0"})
```

```python
# ─── Custom JSON encoder for non-serializable types ───
from datetime import datetime, date
import decimal

class CustomEncoder(json.JSONEncoder):
    """Handle types JSON doesn't know about."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data = {
    "created_at": datetime.now(),
    "price":      decimal.Decimal("99.99"),
    "tags":       {"python", "programming"},
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_str)
```

---

## 🗂️ os Module — File System Operations

```python
import os

# ─── Current directory ───
print(os.getcwd())                  # /home/user/project
os.chdir("/tmp")                    # change directory
print(os.getcwd())                  # /tmp

# ─── List directory contents ───
print(os.listdir("."))              # ['file1.txt', 'dir1', ...]
print(os.listdir("/home/user"))

# ─── Check existence ───
print(os.path.exists("data.txt"))   # True or False
print(os.path.isfile("data.txt"))   # True if it's a FILE
print(os.path.isdir("my_folder"))   # True if it's a DIRECTORY

# ─── File info ───
print(os.path.getsize("data.txt"))  # size in bytes
import time
mtime = os.path.getmtime("data.txt")
print(time.ctime(mtime))           # last modified time

# ─── Path operations ───
path = "/home/user/documents/report.pdf"
print(os.path.dirname(path))       # /home/user/documents
print(os.path.basename(path))      # report.pdf
print(os.path.splitext(path))      # ('/home/user/documents/report', '.pdf')
name, ext = os.path.splitext(os.path.basename(path))
print(name)   # report
print(ext)    # .pdf

# ─── Join paths (OS-independent!) ───
full_path = os.path.join("home", "user", "documents", "file.txt")
print(full_path)   # home/user/documents/file.txt  (Linux/Mac)
                   # home\user\documents\file.txt  (Windows)

# ─── Create directories ───
os.mkdir("new_folder")                           # create one level
os.makedirs("parent/child/grandchild")           # create all levels
os.makedirs("parent/child", exist_ok=True)       # no error if exists ✅

# ─── Remove files and directories ───
os.remove("old_file.txt")          # delete a file
os.rmdir("empty_folder")           # delete empty directory
import shutil
shutil.rmtree("full_folder")       # delete directory with contents

# ─── Rename / Move ───
os.rename("old_name.txt", "new_name.txt")        # rename file
os.rename("old_folder", "new_folder")            # rename folder

# ─── Walk directory tree ───
for dirpath, dirnames, filenames in os.walk("my_project"):
    print(f"📁 {dirpath}/")
    for f in filenames:
        full = os.path.join(dirpath, f)
        size = os.path.getsize(full)
        print(f"   📄 {f}  ({size:,} bytes)")
```

```python
# ─── Environment variables ───
print(os.environ.get("HOME"))         # /home/username
print(os.environ.get("PATH"))         # system PATH
print(os.environ.get("MY_KEY", "default"))  # safe with default
os.environ["MY_SETTING"] = "value"   # set env variable
```

---

## 🛤️ pathlib Module — Modern Path Handling

> `pathlib` is the modern, object-oriented way to handle paths.
> **Prefer pathlib over os.path** for new code!

```python
from pathlib import Path

# ─── Create paths ───
p = Path("documents/report.txt")
p = Path("/home/user/data.csv")
p = Path.home()                    # user's home directory
p = Path.cwd()                     # current working directory

# ─── Path arithmetic with / operator ───
home     = Path.home()
docs     = home / "Documents"               # joining paths!
report   = home / "Documents" / "report.pdf"
print(report)   # /home/user/Documents/report.pdf
```

```python
# ─── Path properties ───
p = Path("/home/user/documents/report.pdf")

print(p.name)       # report.pdf       (filename with extension)
print(p.stem)       # report           (filename without extension)
print(p.suffix)     # .pdf             (extension)
print(p.suffixes)   # ['.pdf']         (all extensions)
print(p.parent)     # /home/user/documents
print(p.parents[0]) # /home/user/documents
print(p.parents[1]) # /home/user
print(p.parts)      # ('/', 'home', 'user', 'documents', 'report.pdf')
print(p.root)       # /
```

```python
# ─── Check and query ───
p = Path("data.txt")

print(p.exists())      # True / False
print(p.is_file())     # True if file
print(p.is_dir())      # True if directory
print(p.stat().st_size)  # size in bytes

# ─── Create directories ───
Path("my/new/directory").mkdir(parents=True, exist_ok=True)

# ─── Read and write — SO clean! ───
p = Path("hello.txt")

# Write
p.write_text("Hello, World!\n", encoding="utf-8")

# Read
content = p.read_text(encoding="utf-8")
print(content)

# Binary
p_bin = Path("data.bin")
p_bin.write_bytes(b'\x00\x01\x02\x03')
data  = p_bin.read_bytes()
```

```python
# ─── Glob — find files matching a pattern ───
project = Path("my_project")

# All Python files in project (non-recursive)
py_files = list(project.glob("*.py"))

# All Python files recursively (** = any depth)
all_py   = list(project.rglob("*.py"))

# All text files
txt_files = list(project.glob("**/*.txt"))

# All files with any extension
all_files = list(project.rglob("*"))

for f in all_py:
    print(f"  🐍 {f}")
```

```python
# ─── Rename, move, delete ───
p = Path("old_name.txt")
p.rename("new_name.txt")             # rename
p.replace("other_dir/file.txt")     # move (overwrites destination)
p.unlink()                           # delete file
p.unlink(missing_ok=True)           # delete — no error if not found ✅

# Directory
d = Path("empty_dir")
d.mkdir(exist_ok=True)
d.rmdir()                            # delete (must be empty)

# ─── Iterate directory ───
p = Path("my_project")
for item in p.iterdir():
    icon = "📁" if item.is_dir() else "📄"
    print(f"  {icon} {item.name}")
```

```python
# ─── Change extension ───
p = Path("document.txt")
new_p = p.with_suffix(".md")
print(new_p)   # document.md

p2 = p.with_name("new_document.txt")
print(p2)      # new_document.txt

# ─── Resolve absolute path ───
p = Path("../data/file.txt")
print(p.resolve())   # /home/user/data/file.txt (full absolute path)
```

---

## 📦 shutil Module — File Operations

```python
import shutil

# ─── Copy files ───
shutil.copy("source.txt", "dest.txt")          # copy file + permissions
shutil.copy2("source.txt", "dest.txt")         # copy + metadata (timestamps too)
shutil.copyfile("source.txt", "dest.txt")      # copy content only

# ─── Copy directory tree ───
shutil.copytree("source_dir", "dest_dir")      # copy entire directory
shutil.copytree("src", "dst", ignore=shutil.ignore_patterns("*.pyc", "__pycache__"))

# ─── Move ───
shutil.move("file.txt", "new_dir/file.txt")    # move file
shutil.move("old_dir",  "new_dir")             # move directory

# ─── Delete directory tree ───
shutil.rmtree("unwanted_dir")                  # delete with all contents

# ─── Archive / Zip ───
shutil.make_archive("backup",       # output name
                    "zip",          # format: zip, tar, gztar, bztar
                    "my_project")   # directory to archive

shutil.unpack_archive("backup.zip", "extracted/")

# ─── Disk usage ───
total, used, free = shutil.disk_usage("/")
print(f"  Total: {total//2**30:,} GB")
print(f"  Used:  {used//2**30:,} GB")
print(f"  Free:  {free//2**30:,} GB")
```

---

## ⚠️ File Exceptions & Error Handling

```python
# ─── Common file exceptions ───
#
# FileNotFoundError  → file/dir doesn't exist
# PermissionError    → no access rights
# IsADirectoryError  → tried to open a dir as file
# FileExistsError    → file already exists ('x' mode)
# OSError            → base class for most file errors
# UnicodeDecodeError → encoding mismatch
# IOError            → I/O failure (same as OSError)
```

```python
# ─── Handle all common errors ───
def safe_read(filename, encoding="utf-8"):
    """Safely read a file with comprehensive error handling."""
    try:
        with open(filename, "r", encoding=encoding) as f:
            return f.read()

    except FileNotFoundError:
        print(f"  ❌ File not found: {filename}")
    except PermissionError:
        print(f"  🔒 Permission denied: {filename}")
    except IsADirectoryError:
        print(f"  📁 {filename} is a directory, not a file")
    except UnicodeDecodeError as e:
        print(f"  🔤 Encoding error in {filename}: {e}")
    except OSError as e:
        print(f"  💥 OS error: {e}")
    return None

content = safe_read("data.txt")
if content:
    print(content[:100])
```

```python
# ─── Safe write with backup ───
def safe_write(filename, content, encoding="utf-8"):
    """Write to file, creating a backup if it exists."""
    import shutil, os

    # Create backup
    if os.path.exists(filename):
        shutil.copy2(filename, filename + ".bak")
        print(f"  📋 Backup created: {filename}.bak")

    try:
        with open(filename, "w", encoding=encoding) as f:
            f.write(content)
        print(f"  ✅ Written: {filename}")
        return True

    except PermissionError:
        print(f"  🔒 Cannot write — permission denied: {filename}")
        # Restore backup if write failed
        if os.path.exists(filename + ".bak"):
            shutil.copy2(filename + ".bak", filename)
        return False
```

```python
# ─── Atomic write — write to temp, then rename ───
import tempfile, os, shutil

def atomic_write(filename, content, encoding="utf-8"):
    """
    Write file atomically — either fully succeeds or fails completely.
    No partial writes! Safe for concurrent processes.
    """
    dir_name = os.path.dirname(os.path.abspath(filename))

    # Write to temp file in same directory
    fd, tmp_path = tempfile.mkstemp(dir=dir_name, text=True)
    try:
        with os.fdopen(fd, "w", encoding=encoding) as tmp:
            tmp.write(content)
        # Atomic rename — replaces destination instantly
        shutil.move(tmp_path, filename)
        print(f"  ✅ Atomically written: {filename}")
    except Exception:
        os.unlink(tmp_path)   # clean up temp file on failure
        raise
```

---

## 🌍 Real-World Projects

---

### Project 1 — Log File Analyzer

```python
import re
from datetime import datetime
from collections import defaultdict, Counter

def analyze_log(log_file):
    """
    Parse and analyze a web server access log.

    Expected format: IP - - [timestamp] "METHOD /path HTTP/1.1" status size
    """
    pattern = re.compile(
        r'(\d+\.\d+\.\d+\.\d+)'         # IP address
        r'.+\[(.+?)\]'                    # timestamp
        r' "(\w+) (.+?) HTTP'             # method + path
        r'" (\d+) (\d+)'                  # status + size
    )

    stats = {
        "total_requests": 0,
        "status_counts":  Counter(),
        "top_ips":        Counter(),
        "top_paths":      Counter(),
        "errors":         [],
        "total_bytes":    0,
    }

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                match = pattern.match(line)
                if not match:
                    continue

                ip, ts, method, path, status, size = match.groups()
                status = int(status)
                size   = int(size)

                stats["total_requests"] += 1
                stats["status_counts"][status] += 1
                stats["top_ips"][ip] += 1
                stats["top_paths"][path] += 1
                stats["total_bytes"] += size

                if status >= 400:
                    stats["errors"].append({
                        "ip": ip, "status": status,
                        "path": path, "method": method
                    })

    except FileNotFoundError:
        print(f"  ❌ Log file not found: {log_file}")
        return None

    # Report
    print(f"\n  📊 LOG ANALYSIS: {log_file}")
    print(f"  {'─'*50}")
    print(f"  Total Requests : {stats['total_requests']:,}")
    print(f"  Total Data     : {stats['total_bytes'] / 1024**2:.2f} MB")
    print(f"  Error Requests : {len(stats['errors'])}")

    print(f"\n  📈 Status Codes:")
    for code, count in sorted(stats["status_counts"].items()):
        icon = "✅" if code < 400 else "⚠️" if code < 500 else "❌"
        print(f"     {icon} {code}: {count:,}")

    print(f"\n  🔝 Top 5 IPs:")
    for ip, count in stats["top_ips"].most_common(5):
        print(f"     {ip:<18} {count:,} requests")

    print(f"\n  🔝 Top 5 Paths:")
    for path, count in stats["top_paths"].most_common(5):
        print(f"     {count:>6,}x  {path[:40]}")

    return stats
```

---

### Project 2 — Configuration File Manager

```python
import json, os, shutil
from datetime import datetime
from pathlib import Path

class ConfigManager:
    """
    A robust configuration manager that reads/writes JSON config files
    with validation, versioning, and backup support.
    """

    def __init__(self, config_path, defaults=None):
        """
        Initialize config manager.

        Args:
            config_path (str): Path to config JSON file.
            defaults   (dict): Default values if file doesn't exist.
        """
        self.path     = Path(config_path)
        self.defaults = defaults or {}
        self._data    = {}
        self.load()

    def load(self):
        """Load config from file, using defaults for missing keys."""
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self._data = json.load(f)
                print(f"  ✅ Config loaded: {self.path}")
            except json.JSONDecodeError as e:
                print(f"  ⚠️ Corrupt config, using defaults: {e}")
                self._data = {}
        else:
            print(f"  📝 No config found, using defaults")
            self._data = {}

        # Apply defaults for any missing keys
        for key, value in self.defaults.items():
            self._data.setdefault(key, value)

    def save(self, backup=True):
        """Save config to file with optional backup."""
        # Create backup
        if backup and self.path.exists():
            backup_path = self.path.with_suffix(
                f".bak.{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            )
            shutil.copy2(self.path, backup_path)

        # Ensure directory exists
        self.path.parent.mkdir(parents=True, exist_ok=True)

        # Write atomically
        tmp = self.path.with_suffix(".tmp")
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self._data, f, indent=4, ensure_ascii=False)
            shutil.move(tmp, self.path)
            print(f"  ✅ Config saved: {self.path}")
        except Exception as e:
            tmp.unlink(missing_ok=True)
            raise

    def get(self, key, default=None):
        """Get a config value with optional default."""
        keys   = key.split(".")   # support nested keys: "server.port"
        value  = self._data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value

    def set(self, key, value):
        """Set a config value (supports nested keys)."""
        keys   = key.split(".")
        target = self._data
        for k in keys[:-1]:
            target = target.setdefault(k, {})
        target[keys[-1]] = value

    def __repr__(self):
        return f"ConfigManager({self.path}, {len(self._data)} keys)"


# Usage:
config = ConfigManager("app_config.json", defaults={
    "server":  {"host": "localhost", "port": 8080, "debug": False},
    "database":{"url": "sqlite:///app.db", "pool_size": 5},
    "logging": {"level": "INFO", "file": "app.log"},
})

print(config.get("server.port"))         # 8080
config.set("server.port", 9090)
config.set("server.debug", True)
config.save()
print(config.get("server.port"))         # 9090
```

---

### Project 3 — File-Based To-Do App

```python
import json
from pathlib import Path
from datetime import datetime

class TodoApp:
    """Simple persistent to-do list using JSON file storage."""

    def __init__(self, filename="todos.json"):
        self.file  = Path(filename)
        self.todos = self._load()

    def _load(self):
        """Load todos from file."""
        if self.file.exists():
            with open(self.file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save(self):
        """Save todos to file."""
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, indent=2, ensure_ascii=False)

    def add(self, title, priority="medium"):
        """Add a new to-do item."""
        todo = {
            "id":         len(self.todos) + 1,
            "title":      title,
            "priority":   priority,
            "done":       False,
            "created_at": datetime.now().isoformat(),
        }
        self.todos.append(todo)
        self._save()
        print(f"  ✅ Added: [{todo['id']}] {title}")
        return todo

    def complete(self, todo_id):
        """Mark a to-do as done."""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"]         = True
                todo["completed_at"] = datetime.now().isoformat()
                self._save()
                print(f"  ✅ Completed: {todo['title']}")
                return
        print(f"  ❌ Todo #{todo_id} not found")

    def delete(self, todo_id):
        """Delete a to-do item."""
        before = len(self.todos)
        self.todos = [t for t in self.todos if t["id"] != todo_id]
        if len(self.todos) < before:
            self._save()
            print(f"  🗑️  Deleted todo #{todo_id}")
        else:
            print(f"  ❌ Todo #{todo_id} not found")

    def list(self, show_done=False):
        """Display all to-dos."""
        items = self.todos if show_done else [t for t in self.todos if not t["done"]]

        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        print(f"\n  📋 TO-DO LIST ({len(items)} items)")
        print(f"  {'─'*45}")

        for todo in items:
            done = "✅" if todo["done"] else "⬜"
            icon = priority_icon.get(todo["priority"], "⚪")
            print(f"  {done} {icon} [{todo['id']:2}] {todo['title']}")

        print(f"  {'─'*45}")
        done_count    = sum(1 for t in self.todos if t["done"])
        pending_count = len(self.todos) - done_count
        print(f"  Pending: {pending_count}  Completed: {done_count}")

    def export_txt(self, filename="todos_export.txt"):
        """Export to-dos to a readable text file."""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"TO-DO LIST — Exported {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write("=" * 50 + "\n\n")
            for todo in self.todos:
                status = "✓" if todo["done"] else "○"
                f.write(f"[{status}] {todo['title']}\n")
                f.write(f"    Priority: {todo['priority']}\n")
                f.write(f"    Created:  {todo['created_at'][:10]}\n\n")
        print(f"  📄 Exported to {filename}")


# Usage:
app = TodoApp("my_todos.json")
app.add("Learn Python file handling", priority="high")
app.add("Build a project", priority="high")
app.add("Read a book", priority="low")
app.complete(1)
app.list()
app.export_txt()
```

---

## 🚨 Common Mistakes

### 1. Forgetting to close the file

```python
# ❌ File might stay open, data might not flush!
f = open("data.txt", "w")
f.write("Hello")
# forgot f.close() — data might not be written!

# ✅ Always use with:
with open("data.txt", "w") as f:
    f.write("Hello")
# automatically closed and flushed ✅
```

### 2. Wrong mode — accidentally wiping data

```python
# ❌ 'w' mode WIPES the file!
with open("important_data.txt", "w") as f:   # 💀 data gone!
    f.write("new stuff")

# ✅ Use 'a' to append, 'r+' to read+write
with open("important_data.txt", "a") as f:   # ✅ data safe
    f.write("new stuff\n")
```

### 3. Missing encoding

```python
# ❌ Platform-dependent — breaks on different OS!
with open("data.txt", "r") as f:
    content = f.read()

# ✅ Always specify encoding:
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### 4. Forgetting newlines in write()

```python
# ❌ Everything on one line!
with open("list.txt", "w") as f:
    f.write("item1")
    f.write("item2")    # File: "item1item2"

# ✅ Add \n yourself:
with open("list.txt", "w") as f:
    f.write("item1\n")
    f.write("item2\n")  # File: "item1\nitem2\n"

# ✅ Or use print():
with open("list.txt", "w") as f:
    print("item1", file=f)    # auto adds \n
    print("item2", file=f)
```

### 5. Reading a closed file

```python
# ❌ File closed before reading!
with open("data.txt", "r") as f:
    content_func = f.read   # stored the METHOD, not the result!
# file is closed here!
result = content_func()     # ❌ ValueError: I/O operation on closed file

# ✅ Read INSIDE the with block:
with open("data.txt", "r") as f:
    content = f.read()      # actual string, not the method
# use content here ✅
```

### 6. Path separators across platforms

```python
# ❌ Hardcoded — breaks on Windows!
path = "data/files/report.txt"     # Linux/Mac
path = "data\\files\\report.txt"   # Windows — breaks on Linux!

# ✅ Use os.path.join or pathlib (cross-platform!):
import os
path = os.path.join("data", "files", "report.txt")  # ✅

from pathlib import Path
path = Path("data") / "files" / "report.txt"         # ✅ cleanest!
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📂  OPENING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

with open("file.txt", "r",  encoding="utf-8") as f: ...  # read
with open("file.txt", "w",  encoding="utf-8") as f: ...  # write (wipes!)
with open("file.txt", "a",  encoding="utf-8") as f: ...  # append
with open("file.txt", "x",  encoding="utf-8") as f: ...  # create new only
with open("file.txt", "r+", encoding="utf-8") as f: ...  # read+write
with open("file.bin", "rb")                  as f: ...  # binary read
with open("file.bin", "wb")                  as f: ...  # binary write

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📖  READING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

f.read()           # entire file as string
f.read(n)          # n characters
f.readline()       # one line (includes \n)
f.readlines()      # list of all lines
for line in f:     # most efficient ⭐

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ✍️  WRITING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

f.write("text\n")          # write string (add \n yourself!)
f.writelines(["a\n","b\n"])# write list of strings
print("text", file=f)      # auto adds \n ✅

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎛️  CURSOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

f.tell()           # current position (bytes)
f.seek(0)          # go to start
f.seek(0, 2)       # go to end

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊  CSV
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import csv
# write
with open("f.csv","w",newline="") as f:
    csv.writer(f).writerows(data)

with open("f.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=["a","b"])
    w.writeheader(); w.writerows(dicts)

# read
with open("f.csv","r",newline="") as f:
    for row in csv.reader(f): ...

with open("f.csv","r",newline="") as f:
    for row in csv.DictReader(f): ...

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗃️  JSON
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import json
# write
with open("f.json","w") as f:
    json.dump(data, f, indent=4)

# read
with open("f.json","r") as f:
    data = json.load(f)

# string
s    = json.dumps(data)       # dict → string
data = json.loads(s)          # string → dict

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🗂️  PATHS (pathlib ⭐)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from pathlib import Path
p = Path("dir") / "file.txt"  # join with /
p.exists()                    # does it exist?
p.is_file() / p.is_dir()      # what is it?
p.name / p.stem / p.suffix    # filename parts
p.parent                      # parent directory
p.read_text(encoding="utf-8") # read in one line!
p.write_text("...", encoding="utf-8")
p.mkdir(parents=True, exist_ok=True)
p.unlink(missing_ok=True)     # delete file
list(p.rglob("*.py"))         # find all .py files

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧  os MODULE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
os.getcwd()                    # current directory
os.listdir(".")                # list contents
os.path.exists("f.txt")        # check exists
os.path.join("a","b","c.txt")  # safe path join
os.makedirs("a/b", exist_ok=True)
os.remove("file.txt")          # delete file
os.rename("old.txt","new.txt") # rename
os.walk("dir")                 # recursive walk

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦  shutil
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import shutil
shutil.copy2("src","dst")      # copy file
shutil.copytree("src","dst")   # copy directory
shutil.move("old","new")       # move
shutil.rmtree("dir")           # delete directory
shutil.make_archive("out","zip","dir") # zip
```

---

## 🎓 Final Summary

```
File Handling in Python:
──────────────────────────────────────────────────────────────
GOLDEN RULE: Always use  with open(...) as f:
             Never forget:  encoding="utf-8"

MODES:   r  = read only        w  = write (wipes!)
         a  = append           x  = create only
         r+ = read+write       b  = binary (add to any)

READ:    f.read()       → whole file as string
         f.readline()   → one line
         f.readlines()  → list of lines
         for line in f  → best for large files ⭐

WRITE:   f.write(str)       → write string
         f.writelines(list)  → write list
         print(..., file=f)  → auto newline

FORMATS: CSV  → import csv  → reader/writer/DictReader/DictWriter
         JSON → import json → load/dump/loads/dumps

PATHS:   pathlib.Path  → modern, clean, cross-platform ⭐
         os.path       → classic, still widely used

TOOLS:   os     → listdir, makedirs, remove, rename, walk
         shutil → copy, move, rmtree, make_archive

ERRORS:  FileNotFoundError, PermissionError, UnicodeDecodeError
         Always wrap in try/except for production code!
──────────────────────────────────────────────────────────────
```

---

