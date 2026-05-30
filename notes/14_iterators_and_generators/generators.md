# ⚡ Python Generators — Zero to Hero
## The Complete Friendly Study Notes

> 🧠 **The Big Idea in One Line:**
> A generator is a function that can **pause itself** mid-execution,
> give you a value, and then **resume exactly where it left off** later. 🎬
>
> Think of it like a **TV show with episodes** 📺:
> - One episode plays (one value yielded)
> - Show **pauses** (execution suspended, state frozen)
> - You come back whenever you're ready
> - Show **resumes** from exactly where it paused
> - When all episodes are done → StopIteration
>
> The magic word is `yield` — it's what makes a function a generator!

```python
# Regular function — runs completely, returns once
def regular():
    return 1     # runs, returns, DONE

# Generator function — pauses and resumes, yields many times
def my_gen():
    yield 1      # pause here, give 1
    yield 2      # resume, pause here, give 2
    yield 3      # resume, pause here, give 3
    # function returns → StopIteration

g = my_gen()
print(next(g))   # 1  ← runs to first yield, pauses
print(next(g))   # 2  ← resumes, runs to second yield, pauses
print(next(g))   # 3  ← resumes, runs to third yield, pauses
# next(g)        # StopIteration ← no more yields!
```

---

## 📚 Table of Contents

1. [What Makes a Generator Special?](#-what-makes-a-generator-special)
2. [yield — The Magic Keyword](#-yield--the-magic-keyword)
3. [Generator Functions vs Regular Functions](#-generator-functions-vs-regular-functions)
4. [Generator Objects](#-generator-objects)
5. [Generator Expressions](#-generator-expressions)
6. [Sending Values INTO a Generator — send()](#-sending-values-into-a-generator--send)
7. [throw() and close()](#-throw-and-close)
8. [yield from — Delegation](#-yield-from--delegation)
9. [Infinite Generators](#-infinite-generators)
10. [Generator Pipelines — The Superpower](#-generator-pipelines--the-superpower)
11. [Generators vs Iterators vs Lists](#-generators-vs-iterators-vs-lists)
12. [Memory Deep Dive](#-memory-deep-dive)
13. [Coroutines (Advanced yield)](#-coroutines-advanced-yield)
14. [Real-World Generator Projects](#-real-world-generator-projects)
15. [Common Mistakes](#-common-mistakes)
16. [Cheat Sheet](#-cheat-sheet)

---

## 🌟 What Makes a Generator Special?

```
Regular Function                    Generator Function
────────────────                    ──────────────────
def regular(n):                     def generator(n):
    results = []                        for i in range(n):
    for i in range(n):                      yield i   ← pause here!
        results.append(i)
    return results                  # no explicit return needed

Called once, runs completely,       Called once, returns an object.
returns ONE value (the list).       Each next() runs to the NEXT yield.
```

```python
# Why does this matter? Consider n = 1,000,000:

def make_squares_list(n):
    return [x**2 for x in range(n)]    # 🐘 ALL stored in RAM

def make_squares_gen(n):
    for x in range(n):
        yield x**2                      # 🪶 ONE at a time

import sys
lst = make_squares_list(10_000)
gen = make_squares_gen(10_000)

print(sys.getsizeof(lst))    # 87,624  bytes 🐘
print(sys.getsizeof(gen))    # 112     bytes 🪶

# Same results, 800x less memory!
print(sum(make_squares_list(10_000)) == sum(make_squares_gen(10_000)))   # True
```

---

## 🎯 yield — The Magic Keyword

> `yield` does THREE things at once:
> 1. **Produces** a value (like return)
> 2. **Pauses** the function (saves ALL local state)
> 3. **Waits** for the next `next()` call to resume

```python
def step_by_step():
    print("Step 1: Starting...")
    yield "value A"                  # ← pauses here

    print("Step 2: Resumed!")
    yield "value B"                  # ← pauses here

    print("Step 3: Resumed again!")
    yield "value C"                  # ← pauses here

    print("Step 4: No more yields — function ends!")
    # implicit StopIteration

gen = step_by_step()

print("About to call next()...")
v1 = next(gen)
print(f"Got: {v1}\n")
# Step 1: Starting...
# Got: value A

v2 = next(gen)
print(f"Got: {v2}\n")
# Step 2: Resumed!
# Got: value B

v3 = next(gen)
print(f"Got: {v3}\n")
# Step 3: Resumed again!
# Got: value C

# next(gen)  ← would print "Step 4: No more..." then StopIteration!
```

```python
# ─── yield inside a loop ───
def count_up(start, stop):
    current = start
    while current <= stop:
        yield current
        current += 1

for n in count_up(1, 5):
    print(n, end=" ")
# 1 2 3 4 5
```

```python
# ─── yield without a value — yields None ───
def yield_nones():
    yield
    yield
    yield

gen = yield_nones()
print(next(gen))   # None
print(next(gen))   # None
print(next(gen))   # None
```

```python
# ─── return in a generator — sets StopIteration value ───
def gen_with_return():
    yield 1
    yield 2
    return "All done!"   # sets value in StopIteration exception

g = gen_with_return()
print(next(g))   # 1
print(next(g))   # 2
try:
    next(g)
except StopIteration as e:
    print(f"StopIteration value: {e.value}")   # "All done!"
```

---

## 🔄 Generator Functions vs Regular Functions

```python
# ─── Key differences in behavior ───

def regular_sum(n):
    """Computes and returns ALL results immediately."""
    return sum(range(n))

def gen_counter(n):
    """Produces numbers ONE AT A TIME — never all at once."""
    for i in range(n):
        yield i

# Regular: immediate, complete
result = regular_sum(5)
print(result)          # 10 (computed immediately)
print(type(result))    # <class 'int'>

# Generator: lazy, incremental
gen = gen_counter(5)
print(gen)             # <generator object gen_counter at 0x...>
print(type(gen))       # <class 'generator'>
print(next(gen))       # 0 (computed NOW, rest waiting)
print(next(gen))       # 1
```

```python
# ─── State is completely preserved between yields! ───
def stateful_gen():
    x = 0
    while True:
        x += 10
        yield x

g = stateful_gen()
print(next(g))    # 10
print(next(g))    # 20  ← x remembered from last time!
print(next(g))    # 30
print(next(g))    # 40

# ─── Multiple independent generators ───
g1 = stateful_gen()
g2 = stateful_gen()   # completely independent!

print(next(g1))   # 10
print(next(g1))   # 20
print(next(g2))   # 10  ← g2 has its OWN state!
print(next(g1))   # 30  ← g1 still has its own state!
```

---

## 🧬 Generator Objects

```python
# A generator object implements the FULL iterator protocol:

def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

# It has __iter__ and __next__:
print(hasattr(g, '__iter__'))    # True
print(hasattr(g, '__next__'))    # True

# iter(g) returns itself:
print(iter(g) is g)              # True ← generator IS its own iterator!

# Works in for loops:
for val in simple_gen():
    print(val, end=" ")   # 1 2 3

# Works with list(), tuple(), set(), sum(), max(), min(), etc.:
print(list(simple_gen()))     # [1, 2, 3]
print(tuple(simple_gen()))    # (1, 2, 3)
print(sum(simple_gen()))      # 6
print(max(simple_gen()))      # 3
```

```python
# ─── Generator object methods ───
g = simple_gen()

# .send(value) → send a value in AND get next item
# .throw(type) → throw an exception into the generator
# .close()     → tell generator to stop (throws GeneratorExit)

# gi_frame     → the frame (None if exhausted)
# gi_running   → True if generator is currently executing
# gi_code      → the code object
print(g.gi_frame)    # <frame object at ...>
print(g.gi_running)  # False
```

---

## 💎 Generator Expressions

> Generator expressions are **one-liner generators** — like list comprehensions
> but with `()` instead of `[]`, and **lazy**!

```python
# List comprehension — creates ALL values NOW:
squares_list = [x**2 for x in range(10)]
print(squares_list)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(type(squares_list))   # <class 'list'>

# Generator expression — creates values ON DEMAND:
squares_gen = (x**2 for x in range(10))
print(squares_gen)    # <generator object <genexpr> at 0x...>
print(type(squares_gen))    # <class 'generator'>
```

```python
# ─── Syntax ───
# (expression for variable in iterable)
# (expression for variable in iterable if condition)

gen1 = (x**2 for x in range(10))
gen2 = (x for x in range(20) if x % 2 == 0)
gen3 = (x.upper() for x in ["hello", "world"])

print(list(gen1))   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(gen2))   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(list(gen3))   # ['HELLO', 'WORLD']
```

```python
# ─── Generator expressions directly inside function calls ───
# No extra () needed when it's the ONLY argument!

total    = sum(x**2 for x in range(100))      # ✅ clean!
maximum  = max(len(word) for word in ["cat", "elephant", "ox"])
has_big  = any(x > 90 for x in [85, 92, 78])
all_pos  = all(x > 0 for x in [1, 2, 3, 4])
joined   = ", ".join(str(x) for x in range(5))

print(total)    # 328350
print(maximum)  # 8 (elephant)
print(has_big)  # True
print(all_pos)  # True
print(joined)   # 0, 1, 2, 3, 4
```

```python
# ─── Generator expression vs comprehension — when to use which ───

# Use list comp [...]  when:
#   → you need to index into it: result[5]
#   → you need len(): len(result)
#   → you'll use it multiple times
#   → you need to modify it

# Use generator expression (...) when:
#   → you only iterate through it ONCE
#   → you're passing it directly to sum/max/min/any/all
#   → data is huge — memory matters
#   → results are used one at a time in a pipeline
```

---

## 📮 Sending Values INTO a Generator — send()

> This is where generators get truly powerful — **two-way communication**!
> `next(g)` gets a value FROM the generator.
> `g.send(value)` sends a value INTO the generator AND gets the next value back.

```python
# The yield expression HAS a value — it's what send() provides!

def echo():
    while True:
        received = yield           # yield gives None, but receives sent value
        print(f"Got: {received}")

g = echo()
next(g)          # MUST call next() first to start — runs to first yield!

g.send("hello")  # sends "hello" → received = "hello" → prints "Got: hello"
g.send("world")  # sends "world" → received = "world" → prints "Got: world"
g.send(42)       # Got: 42
```

```python
# ─── yield as both producer AND consumer ───
def accumulator():
    """Yield running total while accepting new numbers."""
    total = 0
    while True:
        value = yield total    # yield current total, receive new value
        if value is None:
            break
        total += value

acc = accumulator()
print(next(acc))        # 0    ← initial total
print(acc.send(10))     # 10   ← total after adding 10
print(acc.send(25))     # 35   ← total after adding 25
print(acc.send(5))      # 40   ← total after adding 5
print(acc.send(-15))    # 25   ← total after adding -15
```

```python
# ─── send() rule: first call must be next() or send(None) ───
def my_gen():
    x = yield "first"
    yield f"you sent: {x}"

g = my_gen()
print(next(g))           # "first"      ← MUST use next() or send(None) first!
# print(g.send("hi"))    # "you sent: hi"

# Equivalently:
g2 = my_gen()
print(g2.send(None))     # "first"      ← send(None) also works to start!
print(g2.send("hello"))  # "you sent: hello"
```

```python
# ─── Practical send() example: running average ───
def running_average():
    """Compute running average of sent numbers."""
    count = 0
    total = 0.0
    avg   = None
    while True:
        value = yield avg
        if value is not None:
            total += value
            count += 1
            avg    = total / count

ra = running_average()
next(ra)                      # start
print(ra.send(10))            # 10.0
print(ra.send(20))            # 15.0
print(ra.send(30))            # 20.0
print(ra.send(40))            # 25.0
```

---

## 💣 throw() and close()

```python
# ─── throw() — inject an exception into the generator ───
def gen_with_error_handling():
    try:
        while True:
            value = yield
            print(f"  Processing: {value}")
    except ValueError as e:
        print(f"  ⚠️  Got ValueError: {e}")
        yield "recovered!"   # can yield AFTER handling!

g = gen_with_error_handling()
next(g)                                # start
g.send("apple")                        # Processing: apple
g.send("banana")                       # Processing: banana
result = g.throw(ValueError, "bad input!")  # ⚠️ Got ValueError: bad input!
print(result)                          # recovered!
```

```python
# ─── close() — gracefully stop a generator ───
def infinite_counter():
    n = 0
    try:
        while True:
            yield n
            n += 1
    except GeneratorExit:
        print("  🛑 Generator was closed! Cleaning up...")
        # Can do cleanup here — but cannot yield after GeneratorExit!

g = infinite_counter()
print(next(g))   # 0
print(next(g))   # 1
print(next(g))   # 2
g.close()        # 🛑 Generator was closed! Cleaning up...
# next(g)        # StopIteration — generator is closed
```

---

## 🔀 yield from — Delegation

> `yield from` lets a generator **delegate** to another iterable/generator.
> It's a shortcut that's more powerful than it looks!

```python
# ─── Basic yield from ───
def gen_a():
    yield 1
    yield 2
    yield 3

def gen_b():
    yield "x"
    yield "y"

# Without yield from — manual:
def combined_manual():
    for item in gen_a():
        yield item
    for item in gen_b():
        yield item

# With yield from — clean!
def combined():
    yield from gen_a()    # delegates everything to gen_a
    yield from gen_b()    # then delegates to gen_b

print(list(combined()))   # [1, 2, 3, 'x', 'y']
```

```python
# ─── yield from with any iterable ───
def flatten_one_level():
    yield from [1, 2, 3]         # from list
    yield from "ABC"             # from string
    yield from range(4, 7)       # from range
    yield from (x**2 for x in range(3))  # from generator!

print(list(flatten_one_level()))
# [1, 2, 3, 'A', 'B', 'C', 4, 5, 6, 0, 1, 4]
```

```python
# ─── Recursive flatten with yield from ───
def flatten(nested):
    """Recursively flatten any deeply nested structure."""
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)   # ← recursive delegation!
        else:
            yield item

deep = [1, [2, [3, [4, [5, 6]], 7]], 8, [9, 10]]
print(list(flatten(deep)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```python
# ─── yield from passes send() and throw() through! ───
# This is yield from's superpower — it's a transparent tunnel!

def inner():
    value = yield "inner yield"
    print(f"  inner received: {value}")
    yield "inner done"

def outer():
    result = yield from inner()   # transparently delegates!
    print(f"  outer got return: {result}")

g = outer()
print(next(g))          # "inner yield" ← from inner!
print(g.send("hello"))  # inner received: hello → "inner done"
```

---

## ♾️ Infinite Generators

```python
# ─── Infinite counter ───
def count_from(start=0, step=1):
    """Count forever from start."""
    n = start
    while True:
        yield n
        n += step

# Always use islice, take, or break with infinite generators!
from itertools import islice

evens = count_from(0, 2)
print(list(islice(evens, 10)))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

```python
# ─── Fibonacci forever ───
def fibonacci():
    """Yield Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_15 = [next(fib) for _ in range(15)]
print(first_15)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
```

```python
# ─── Prime number generator ───
def primes():
    """Yield all prime numbers — forever!"""
    def is_prime(n):
        if n < 2: return False
        return all(n % i != 0 for i in range(2, int(n**0.5)+1))

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_gen = primes()
first_10_primes = [next(prime_gen) for _ in range(10)]
print(first_10_primes)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

```python
# ─── Random walk ───
import random

def random_walk(start=0, step_size=1):
    """Random walk — go up or down randomly, forever."""
    position = start
    while True:
        yield position
        position += random.choice([-step_size, step_size])

walk = random_walk(0)
positions = [next(walk) for _ in range(10)]
print(positions)
# [0, -1, 0, 1, 0, 1, 2, 1, 0, -1]  (random!)
```

---

## 🚰 Generator Pipelines — The Superpower

> This is where generators truly shine!
> Chain generators together like UNIX pipes: `data → filter → transform → output`
> **Nothing computed until the final consumer pulls!** 🎣

```python
# ─── Building a data pipeline ───
def read_numbers(n):
    """Source: generate numbers."""
    for i in range(n):
        yield i

def only_even(source):
    """Stage 1: filter to only even numbers."""
    for n in source:
        if n % 2 == 0:
            yield n

def square(source):
    """Stage 2: square each number."""
    for n in source:
        yield n ** 2

def add_label(source):
    """Stage 3: add a string label."""
    for n in source:
        yield f"Value: {n}"

# Connect the pipeline:
source   = read_numbers(20)       # 0..19
filtered = only_even(source)      # 0,2,4,6,8,10,12,14,16,18
squared  = square(filtered)       # 0,4,16,36,64,100,144,196,256,324
labeled  = add_label(squared)     # "Value: 0", "Value: 4", ...

# Nothing has been computed yet! Just pipeline definition.
# Pull the values:
for item in labeled:
    print(f"  {item}")

# Value: 0
# Value: 4
# Value: 16
# ... etc.
```

```python
# ─── Pipeline with generator expressions ───
# Even more concise — same lazy behavior!

data = range(1, 101)

# Pipeline:
evens   = (x for x in data if x % 2 == 0)
squared = (x**2 for x in evens)
big     = (x for x in squared if x > 500)
labeled = (f"#{x}" for x in big)

print(list(labeled))
# ['#576', '#676', '#784', '#900', '#1024', '#1156', '#1296', '#1444', '#1600', '#1764', '#1936', '#2100']
```

```python
# ─── Real log processing pipeline ───
import re

def read_logs(lines):
    """Source: yield log lines."""
    yield from lines

def parse_logs(lines):
    """Parse raw lines into structured dicts."""
    pattern = re.compile(
        r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+): (.+)'
    )
    for line in lines:
        m = pattern.match(line.strip())
        if m:
            yield {
                "date":    m.group(1),
                "time":    m.group(2),
                "level":   m.group(3),
                "message": m.group(4),
            }

def filter_level(entries, level):
    """Keep only entries of a specific log level."""
    return (e for e in entries if e["level"] == level)

def format_report(entries):
    """Format entries for display."""
    for e in entries:
        yield f"  [{e['date']} {e['time']}] {e['message']}"

# Sample log lines
sample_logs = [
    "2024-01-15 10:23:01 INFO: Server started",
    "2024-01-15 10:24:12 ERROR: Database connection failed",
    "2024-01-15 10:24:13 INFO: Retrying connection...",
    "2024-01-15 10:24:15 ERROR: Timeout exceeded",
    "2024-01-15 10:25:00 INFO: Connection restored",
    "2024-01-15 10:30:00 WARNING: High memory usage",
]

# Build pipeline:
raw     = read_logs(sample_logs)
parsed  = parse_logs(raw)
errors  = filter_level(parsed, "ERROR")
report  = format_report(errors)

print("🚨 ERROR Log Report:")
for line in report:
    print(line)

# 🚨 ERROR Log Report:
#   [2024-01-15 10:24:12] Database connection failed
#   [2024-01-15 10:24:15] Timeout exceeded
```

---

## 🆚 Generators vs Iterators vs Lists

```
┌──────────────────┬────────────────┬───────────────────┬────────────────────┐
│                  │   LIST [ ]     │    ITERATOR       │   GENERATOR ⚡     │
├──────────────────┼────────────────┼───────────────────┼────────────────────┤
│ Memory           │ 🐘 All values  │ 🪶 Tiny           │ 🪶 Tiny            │
│ Indexing         │ ✅ lst[5]      │ ❌ No             │ ❌ No              │
│ len()            │ ✅ Yes         │ ❌ No             │ ❌ No              │
│ Multiple passes  │ ✅ Yes         │ ❌ One-pass       │ ❌ One-pass        │
│ Lazy?            │ ❌ Eager       │ ✅ Yes            │ ✅ Yes             │
│ Can be infinite  │ ❌ No          │ ✅ Yes            │ ✅ Yes             │
│ send()           │ ❌ No          │ ❌ No             │ ✅ Yes             │
│ Syntax           │ [x for x in …] │ Class-based       │ def + yield OR     │
│                  │                │                   │ (x for x in …)     │
│ Syntax ease      │ ⭐⭐⭐         │ ⭐               │ ⭐⭐⭐            │
└──────────────────┴────────────────┴───────────────────┴────────────────────┘

USE LIST when:      you need indexing, len(), multiple passes, modification
USE ITERATOR when:  custom iteration logic via a class (complex state)
USE GENERATOR when: simple iteration, one-pass, lazy evaluation, pipelines
```

```python
# ─── Same logic: three ways ───

# List
def squares_list(n):
    return [x**2 for x in range(n)]

# Custom Iterator class
class SquaresIterator:
    def __init__(self, n): self.n = n; self.i = 0
    def __iter__(self): return self
    def __next__(self):
        if self.i >= self.n: raise StopIteration
        v = self.i**2; self.i += 1; return v

# Generator function ← simplest and most Pythonic!
def squares_gen(n):
    for x in range(n):
        yield x**2

# Generator expression ← even simpler for one-liners!
squares_expr = lambda n: (x**2 for x in range(n))

# They all produce the same sequence — but generators are
# the simplest, most readable, and most memory-efficient!
```

---

## 💾 Memory Deep Dive

```python
import sys, tracemalloc

def measure(func, n):
    tracemalloc.start()
    result = list(func(n))   # force evaluation
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak, result[:3]

# List approach:
def list_squares(n):
    return [x**2 for x in range(n)]

# Generator approach:
def gen_squares(n):
    for x in range(n):
        yield x**2

n = 100_000
c1, p1, _ = measure(lambda n: iter(list_squares(n)), n)
c2, p2, _ = measure(gen_squares, n)

print(f"List:      current={c1:>10,} bytes  peak={p1:>10,} bytes")
print(f"Generator: current={c2:>10,} bytes  peak={p2:>10,} bytes")
print(f"Generator uses {p1/p2:.0f}x less peak memory!")
```

```python
# ─── Generator with large data — stays constant memory! ───
def process_big_file(filename):
    """
    Process a 10GB file.
    Memory usage: ~constant regardless of file size!
    """
    def read_lines(path):
        with open(path, encoding="utf-8") as f:
            yield from f       # yield one line at a time!

    def parse(lines):
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                yield {
                    "id":    parts[0],
                    "name":  parts[1],
                    "value": float(parts[2]),
                }

    def filter_big(records):
        return (r for r in records if r["value"] > 1000)

    def format_output(records):
        for r in records:
            yield f"{r['id']}: {r['name']} = {r['value']:.2f}"

    lines   = read_lines(filename)
    records = parse(lines)
    big     = filter_big(records)
    output  = format_output(big)

    return output

# Each stage processes ONE item at a time
# Total memory ≈ a few KB regardless of file size!
```

---

## 🤖 Coroutines (Advanced yield)

> When `yield` is used as an **expression** that RECEIVES values,
> the generator becomes a **coroutine** — a cooperative multitasking unit!

```python
# ─── Simple coroutine ───
def printer():
    """A coroutine that prints whatever it receives."""
    print("  Printer ready!")
    while True:
        item = yield             # receive without producing
        if item is None:
            break
        print(f"  🖨️  Printing: {item}")
    print("  Printer done!")

p = printer()
next(p)               # start up (run to first yield)
p.send("Hello")       # 🖨️  Printing: Hello
p.send("World")       # 🖨️  Printing: World
p.send("Python!")     # 🖨️  Printing: Python!
p.send(None)          # breaks the loop, printer done!
```

```python
# ─── Coroutine pipeline ───
def pipeline_stage(transform, target):
    """Transform each received value and send to next stage."""
    while True:
        item = yield
        if item is None:
            target.send(None)
            break
        target.send(transform(item))

def sink(name):
    """Terminal stage — just collect/display results."""
    results = []
    try:
        while True:
            item = yield
            print(f"  [{name}] received: {item}")
            results.append(item)
    except GeneratorExit:
        print(f"  [{name}] done. Got {len(results)} items.")

# Build pipeline:
output  = sink("output")
next(output)

upper   = pipeline_stage(str.upper, output)
next(upper)

trimmed = pipeline_stage(str.strip, upper)
next(trimmed)

# Send data through:
for word in ["  hello  ", "  world  ", "  python  "]:
    trimmed.send(word)

trimmed.send(None)

# [output] received: HELLO
# [output] received: WORLD
# [output] received: PYTHON
```

```python
# ─── Coroutine decorator — auto-start ───
def coroutine(func):
    """Decorator to automatically advance a coroutine to first yield."""
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)   # auto-start!
        return gen
    return wrapper

@coroutine
def auto_printer():
    while True:
        item = yield
        print(f"  → {item}")

p = auto_printer()   # no need to call next()!
p.send("Hello")      # → Hello  (works immediately!)
p.send("World")      # → World
```

---

## 🌍 Real-World Generator Projects

---

### Project 1 — Lazy File Processor

```python
def read_chunks(filename, chunk_size=8192):
    """
    Read a file in chunks — handles files of any size!

    Args:
        filename   (str): File to read.
        chunk_size (int): Bytes per chunk.

    Yields:
        bytes: Each chunk of the file.
    """
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk


def count_bytes(filename):
    """Count total bytes without loading entire file."""
    return sum(len(chunk) for chunk in read_chunks(filename))


def find_in_file(filename, search_bytes):
    """Search for bytes in a large file — memory efficient."""
    for i, chunk in enumerate(read_chunks(filename)):
        if search_bytes in chunk:
            yield i   # yield chunk index where found


def lines_from_file(filename, encoding="utf-8"):
    """
    Yield lines from a file, one at a time.
    Works on multi-gigabyte files with constant memory.
    """
    with open(filename, "r", encoding=encoding) as f:
        for line in f:
            yield line.rstrip("\n")


def head(filename, n=10):
    """Yield first n lines — stops reading after n lines."""
    for i, line in enumerate(lines_from_file(filename)):
        if i >= n:
            break
        yield line


def grep(filename, pattern, flags=0):
    """Yield lines matching a regex pattern."""
    import re
    compiled = re.compile(pattern, flags)
    for num, line in enumerate(lines_from_file(filename), 1):
        if compiled.search(line):
            yield num, line


def tail(filename, n=10):
    """Yield last n lines — reads entire file but buffers only n."""
    from collections import deque
    return deque(lines_from_file(filename), maxlen=n)
```

---

### Project 2 — Fibonacci, Primes, and Math Generators

```python
def fibonacci(stop=None):
    """
    Yield Fibonacci numbers, optionally stopping at or below `stop`.

    Args:
        stop: If given, stop when value exceeds stop. If None, run forever.

    Yields:
        int: Next Fibonacci number.

    Examples:
        >>> list(fibonacci(stop=100))
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    a, b = 0, 1
    while stop is None or a <= stop:
        yield a
        a, b = b, a + b


def primes():
    """
    Yield all prime numbers using the Sieve of Eratosthenes (lazily).

    Yields:
        int: Next prime number.
    """
    composites = {}
    candidate  = 2

    while True:
        if candidate not in composites:
            yield candidate                         # it's prime!
            composites[candidate * candidate] = [candidate]
        else:
            for prime in composites[candidate]:
                composites.setdefault(candidate + prime, []).append(prime)
            del composites[candidate]
        candidate += 1


def collatz(n):
    """
    Yield the Collatz sequence starting from n.

    Args:
        n (int): Starting number (must be positive).

    Yields:
        int: Each number in the sequence until reaching 1.

    Examples:
        >>> list(collatz(6))
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
    """
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def powers_of_two():
    """Yield 1, 2, 4, 8, 16, 32, ... forever."""
    n = 1
    while True:
        yield n
        n *= 2


def geometric(first, ratio):
    """Yield a geometric sequence: first, first*ratio, first*ratio², ..."""
    current = first
    while True:
        yield current
        current *= ratio


# ─── Demo ───
from itertools import islice

print("Fibonacci (≤ 200):")
print(list(fibonacci(stop=200)))

print("\nFirst 15 primes:")
print(list(islice(primes(), 15)))

print("\nCollatz(27) — length:")
c = list(collatz(27))
print(f"Length: {len(c)}, Max: {max(c)}")

print("\nPowers of 2 (first 10):")
print(list(islice(powers_of_two(), 10)))
```

---

### Project 3 — Data Pipeline Engine

```python
from typing import Callable, Iterable, TypeVar, Generator
import itertools
import functools

T = TypeVar("T")

class Pipeline:
    """
    A composable, lazy data pipeline built on generators.

    Each stage is a function that takes an iterable and yields results.
    Nothing is computed until you iterate or call list()/sum()/etc.

    Example:
        result = (
            Pipeline.from_source([1..100])
            .filter(lambda x: x % 2 == 0)
            .map(lambda x: x**2)
            .take(5)
            .to_list()
        )
    """
    def __init__(self, source):
        self._source = source

    @classmethod
    def from_source(cls, source):
        """Create pipeline from any iterable."""
        return cls(iter(source))

    @classmethod
    def count_from(cls, start=0, step=1):
        """Create pipeline from infinite counter."""
        return cls(itertools.count(start, step))

    def map(self, func):
        """Apply func to every element."""
        self._source = (func(x) for x in self._source)
        return self

    def filter(self, pred):
        """Keep elements where pred returns True."""
        self._source = (x for x in self._source if pred(x))
        return self

    def take(self, n):
        """Take only the first n elements."""
        self._source = itertools.islice(self._source, n)
        return self

    def skip(self, n):
        """Skip the first n elements."""
        self._source = itertools.islice(self._source, n, None)
        return self

    def take_while(self, pred):
        """Take elements while pred is True."""
        self._source = itertools.takewhile(pred, self._source)
        return self

    def drop_while(self, pred):
        """Drop elements while pred is True."""
        self._source = itertools.dropwhile(pred, self._source)
        return self

    def chunk(self, size):
        """Group elements into chunks of given size."""
        def _chunk(src, n):
            it = iter(src)
            while True:
                batch = list(itertools.islice(it, n))
                if not batch:
                    break
                yield batch
        self._source = _chunk(self._source, size)
        return self

    def flatten(self):
        """Flatten one level of nesting."""
        self._source = itertools.chain.from_iterable(self._source)
        return self

    def enumerate(self, start=0):
        """Attach index to each element."""
        self._source = builtins_enumerate(self._source, start=start)
        return self

    def __iter__(self):
        return self._source

    def to_list(self):       return list(self._source)
    def to_tuple(self):      return tuple(self._source)
    def to_set(self):        return set(self._source)
    def sum(self):           return sum(self._source)
    def count(self):         return sum(1 for _ in self._source)
    def first(self, default=None): return next(self._source, default)

import builtins
builtins_enumerate = builtins.enumerate


# ─── Usage Demo ───
result = (
    Pipeline.count_from(1)
    .filter(lambda x: x % 2 == 0)       # keep evens
    .map(lambda x: x ** 2)              # square them
    .take_while(lambda x: x <= 100)     # stop when > 100
    .to_list()
)
print("Even squares ≤ 100:")
print(result)
# [4, 16, 36, 64, 100]

# More complex:
result2 = (
    Pipeline.from_source(range(1, 50))
    .filter(lambda x: x % 3 == 0)
    .map(lambda x: (x, x**2, x**3))
    .take(5)
    .to_list()
)
print("\nMultiples of 3 with squares and cubes:")
for n, sq, cu in result2:
    print(f"  {n:3}  →  {sq:5}  →  {cu:7}")
```

---

### Project 4 — Batch Processor

```python
import time
import random

def batched(iterable, batch_size):
    """
    Yield successive batches from an iterable.

    Args:
        iterable:   Source of items.
        batch_size: How many items per batch.

    Yields:
        list: Each batch of items.

    Example:
        >>> list(batched(range(10), 3))
        [[0,1,2], [3,4,5], [6,7,8], [9]]
    """
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:   # don't forget the last partial batch!
        yield batch


def retry_generator(gen_func, *args, max_retries=3, delay=0.1, **kwargs):
    """
    Retry a generator function up to max_retries times per item.

    Args:
        gen_func:     Generator function to call.
        max_retries:  Max attempts per item.
        delay:        Seconds between retries.

    Yields:
        Successful results from gen_func.
    """
    for item in gen_func(*args, **kwargs):
        for attempt in range(max_retries):
            try:
                yield item
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(delay)
                else:
                    print(f"  ❌ Failed after {max_retries} retries: {item}")


def process_in_batches(records, batch_size=10):
    """
    Simulate batch database insertion.
    Generators ensure only one batch in memory at a time!
    """
    total_processed = 0

    for batch_num, batch in enumerate(batched(records, batch_size), 1):
        # Simulate processing delay
        time.sleep(0.001)

        # Simulate occasional failure
        if random.random() < 0.1:
            print(f"  ⚠️  Batch {batch_num} failed! Rolling back...")
            continue

        total_processed += len(batch)
        yield {
            "batch":     batch_num,
            "size":      len(batch),
            "total":     total_processed,
            "sample":    batch[:2],
        }


# ─── Demo ───
random.seed(42)
all_records = [{"id": i, "name": f"record_{i}"} for i in range(1, 51)]

print("📦 Batch Processing:")
print("─" * 40)
for result in process_in_batches(all_records, batch_size=10):
    print(f"  Batch {result['batch']:2}: "
          f"{result['size']} records  "
          f"(total: {result['total']})")
```

---

## 🚨 Common Mistakes

### Mistake 1 — Trying to Index a Generator

```python
gen = (x**2 for x in range(10))

# ❌ Generators don't support indexing!
print(gen[5])     # TypeError: 'generator' object is not subscriptable

# ✅ Convert to list if you need indexing:
lst = list(gen)
print(lst[5])     # 25 ✅

# ✅ Or use itertools.islice for the Nth item:
from itertools import islice
gen = (x**2 for x in range(10))
fifth = next(islice(gen, 5, None))   # skip 5, take 1
print(fifth)   # 25
```

### Mistake 2 — Using a Generator Twice

```python
gen = (x**2 for x in range(5))

print(list(gen))   # [0, 1, 4, 9, 16]  ← consumed!
print(list(gen))   # []                 ← empty! already exhausted!

# ✅ Create a new generator each time:
def squares(n):
    return (x**2 for x in range(n))

print(list(squares(5)))   # [0, 1, 4, 9, 16]  ← fresh!
print(list(squares(5)))   # [0, 1, 4, 9, 16]  ← fresh again! ✅
```

### Mistake 3 — Forgetting to Advance with next() Before send()

```python
def my_gen():
    x = yield "ready"
    yield f"got: {x}"

g = my_gen()

# ❌ Can't send a non-None value before starting!
# g.send("hello")   # TypeError!

# ✅ Always start with next() or send(None):
first = next(g)        # ← REQUIRED first step
print(first)           # "ready"
result = g.send("hello")
print(result)          # "got: hello"
```

### Mistake 4 — Assuming Order in Nested Generator Expressions

```python
# ❌ This is evaluated left-to-right — the outer for loop runs FIRST
matrix = [[1,2,3],[4,5,6]]
flat   = (x for row in matrix for x in row)
# The "for row in matrix" creates state at definition time...
# but "for x in row" is evaluated lazily!

# ✅ Be explicit with nested generators if order matters
def flatten(matrix):
    for row in matrix:
        for x in row:
            yield x
```

### Mistake 5 — Not Closing a Generator Properly

```python
def gen_with_resource():
    print("  📂 Opening resource...")
    try:
        yield from range(5)
    finally:
        print("  🔐 Closing resource...")   # ALWAYS runs!

g = gen_with_resource()
print(next(g))   # 0 — "📂 Opening resource..."
print(next(g))   # 1
del g            # ← triggers GeneratorExit → finally runs!
# 🔐 Closing resource...

# ✅ Better: use with statement or explicit close()
g = gen_with_resource()
print(next(g))
g.close()        # explicit close → finally runs ✅
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡  GENERATOR FUNCTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def gen(n):
    for i in range(n):
        yield i            # produce value, pause

g = gen(5)                 # create generator object
next(g)                    # get next value
list(gen(5))               # consume all: [0,1,2,3,4]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 💎  GENERATOR EXPRESSION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

g = (x**2 for x in range(10))
g = (x for x in data if x > 0)
sum(x**2 for x in range(100))    # use directly in builtins!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔀  DELEGATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def outer():
    yield from inner()    # delegate to inner
    yield from [1, 2, 3]  # delegate to list
    yield from range(5)   # delegate to range

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📮  SEND / THROW / CLOSE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

next(g)                   # advance to next yield
g.send(None)              # same as next(g)
g.send(value)             # send value, get next yield
g.throw(ExcType, msg)     # inject exception
g.close()                 # stop generator (GeneratorExit)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️  COROUTINE TEMPLATE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def coroutine():
    while True:
        received = yield          # pause, wait for send()
        process(received)

c = coroutine()
next(c)                           # MUST start first!
c.send("data")                    # send data in

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚰  PIPELINE PATTERN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def source(data):
    yield from data

def transform(src):
    for x in src:
        yield process(x)

def sink(src):
    for x in src:
        output(x)

sink(transform(source(data)))     # lazy pipeline!

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ♾️  INFINITE PATTERNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def infinite():
    while True:
        yield something()

from itertools import islice, takewhile
list(islice(infinite(), 10))          # take 10
list(takewhile(lambda x: x < 100, g)) # take while < 100
for x in infinite():
    if x > 100: break                  # manual break

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧹  CLEANUP WITH FINALLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def safe_gen():
    try:
        yield from do_work()
    finally:
        cleanup()        # runs on close() or normal end
```

---

## 🎓 Final Summary

```
Generators in Python:
──────────────────────────────────────────────────────────────
CORE IDEA
  Generator = function that remembers where it paused.
  yield = pause, produce a value, wait to resume.
  Generator object = lazy iterator backed by a function.

TWO WAYS TO CREATE
  1. Generator function:     def gen(): yield value
  2. Generator expression:   (expr for x in it if cond)

KEY BEHAVIORS
  ✅ Lazy — computes on demand
  ✅ Stateful — remembers local variables between yields
  ✅ One-pass — can't go back or restart
  ✅ Memory-efficient — one item at a time
  ✅ Composable — chain generators into pipelines
  ✅ Can be infinite — no list size limit

ADVANCED FEATURES
  yield from → delegate to sub-generator/iterable
  send()     → two-way communication (coroutines)
  throw()    → inject exception
  close()    → graceful shutdown
  finally    → cleanup always runs

GOLDEN RULES
  1. Once exhausted, generator is done — create a new one
  2. Always next() or send(None) before first send(value)
  3. Use finally for cleanup in generators with resources
  4. Prefer generators over lists when data is large or one-pass
  5. Use yield from for sub-generators (not manual for loops)

WHEN TO USE
  ✅ Processing large/infinite data streams
  ✅ Lazy pipelines (filter → transform → output)
  ✅ One-time iteration over sequences
  ✅ Memory-constrained environments
  ✅ Replacing complex iterator classes with simple functions
──────────────────────────────────────────────────────────────
```

---
