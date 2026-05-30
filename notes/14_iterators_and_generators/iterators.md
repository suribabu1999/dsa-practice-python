# 🔁 Python Iterators — Zero to Hero
## The Complete Friendly Study Notes

> 🧠 **The Big Idea in One Line:**
> An iterator is an object that gives you **one item at a time**,
> remembering **exactly where it left off** each time you ask. 📍
>
> Think of it like a **book with a bookmark** 📖
> - You read one page → bookmark moves forward
> - You come back later → pick up exactly where you left off
> - Pages are given ONE at a time — not all at once
> - When pages run out → "StopIteration" — done!

---

## 📚 Table of Contents

1. [The Iteration Story — Why Does It Exist?](#-the-iteration-story--why-does-it-exist)
2. [Iterable vs Iterator — The Key Difference](#-iterable-vs-iterator--the-key-difference)
3. [The Two Magic Methods](#-the-two-magic-methods)
4. [iter() and next() — The Engine](#-iter-and-next--the-engine)
5. [How for Loops Really Work](#-how-for-loops-really-work)
6. [Built-in Iterators](#-built-in-iterators)
7. [Building Your Own Iterator Class](#-building-your-own-iterator-class)
8. [Iterator Examples — Progressively Advanced](#-iterator-examples--progressively-advanced)
9. [Infinite Iterators](#-infinite-iterators)
10. [itertools Module — The Iterator Toolkit](#-itertools-module--the-iterator-toolkit)
11. [Chaining and Combining Iterators](#-chaining-and-combining-iterators)
12. [Iterator Protocol in Practice](#-iterator-protocol-in-practice)
13. [Memory: Iterator vs List](#-memory-iterator-vs-list)
14. [Real-World Iterator Projects](#-real-world-iterator-projects)
15. [Common Mistakes](#-common-mistakes)
16. [Cheat Sheet](#-cheat-sheet)

---

## 📖 The Iteration Story — Why Does It Exist?

Imagine you have **1 million numbers** and you want to print them.

```python
# ❌ The naive way — store ALL 1 million in memory first!
numbers = [0, 1, 2, 3, ..., 999999]   # 🐘 ~8 MB in RAM just sitting there!
for n in numbers:
    print(n)

# ✅ The iterator way — create ONE number at a time, on demand!
for n in range(1_000_000):             # 🪶 barely any memory!
    print(n)
```

`range(1_000_000)` doesn't create a list of a million numbers.
It creates an **iterator** — a tiny object that produces the
**next number on demand**. That's the whole point. 🎯

```
Without iterators:               With iterators:
┌──────────────────────┐         ┌──────────────────────┐
│ RAM                  │         │ RAM                  │
│ [0,1,2,...,999999]   │         │ Iterator object      │
│ 8,000,000 bytes 🐘   │         │ (just 3 numbers: 🪶  │
└──────────────────────┘         │  start, stop, current│
                                 └──────────────────────┘
```

---

## 🆚 Iterable vs Iterator — The Key Difference

> This is the #1 confusion about iterators. Let's kill it once and for all! 🔪

```
┌─────────────────┬─────────────────────────────────────────────────┐
│                 │                                                   │
│   ITERABLE 🗃️  │   Something you CAN loop over                    │
│                 │   Has __iter__() method                          │
│                 │   Can produce an iterator                        │
│                 │   Example: list, str, dict, set, range, tuple    │
│                 │                                                   │
├─────────────────┼─────────────────────────────────────────────────┤
│                 │                                                   │
│   ITERATOR 🔖  │   Something that IS being looped over            │
│                 │   Has __iter__() AND __next__() methods          │
│                 │   Remembers its current position                 │
│                 │   Example: iter(list), file object, zip, map    │
│                 │                                                   │
└─────────────────┴─────────────────────────────────────────────────┘
```

```python
# 🗃️ A LIST is an ITERABLE (can produce iterators, reusable)
my_list = [1, 2, 3]

# ✅ Can loop many times:
for x in my_list: print(x)    # works!
for x in my_list: print(x)    # works again! ✅

# 🔖 An ITERATOR is a one-way ticket (stateful, one-pass)
my_iter = iter(my_list)   # create iterator FROM the list

print(next(my_iter))   # 1  ← gives item, moves forward
print(next(my_iter))   # 2
print(next(my_iter))   # 3
print(next(my_iter))   # StopIteration! ← exhausted

# ❌ Iterator is EXHAUSTED — can't loop again!
for x in my_iter: print(x)    # prints nothing!
for x in my_iter: print(x)    # still nothing!

# ✅ But the original iterable is still fine:
for x in my_list: print(x)    # works! list is not affected
```

```python
# 🧪 Quick test — is something an iterator?
from collections.abc import Iterator, Iterable

my_list = [1, 2, 3]
my_iter = iter(my_list)

print(isinstance(my_list, Iterable))   # True  ← list is iterable
print(isinstance(my_list, Iterator))   # False ← list is NOT an iterator

print(isinstance(my_iter, Iterable))   # True  ← iterator IS also iterable!
print(isinstance(my_iter, Iterator))   # True  ← iterator IS an iterator

# Key insight: Every iterator is also an iterable!
# (iter(my_iter) returns my_iter itself)
print(iter(my_iter) is my_iter)        # True ✅
```

---

## 🪄 The Two Magic Methods

> The **Iterator Protocol** is just two magic methods. That's it!

```
┌─────────────────────────────────────────────────────────────┐
│  THE ITERATOR PROTOCOL                                       │
│                                                              │
│  __iter__(self)   → return self                             │
│                     Makes object work in for loops          │
│                     and with iter()                         │
│                                                              │
│  __next__(self)   → return next value                       │
│                     Raise StopIteration when done           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

```python
# A class implementing the protocol is an iterator:
class SimpleCounter:
    def __init__(self, start, stop):
        self.current = start
        self.stop    = stop

    def __iter__(self):
        return self          # 👈 return self! (I am the iterator)

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration   # 🛑 signal: we're done!
        value = self.current
        self.current += 1
        return value

# Use it like any iterator:
counter = SimpleCounter(1, 5)

print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3

for n in SimpleCounter(10, 15):
    print(n, end=" ")
# 10 11 12 13 14
```

---

## ⚙️ iter() and next() — The Engine

```python
# iter(iterable)  → creates and returns an iterator
# next(iterator)  → gets the NEXT value from iterator

# ─── iter() ───
my_list  = [10, 20, 30]
iterator = iter(my_list)
print(type(iterator))    # <class 'list_iterator'>

# ─── next() ───
print(next(iterator))   # 10
print(next(iterator))   # 20
print(next(iterator))   # 30
# next(iterator)        # StopIteration!

# ─── next() with default — safe! ───
print(next(iterator, "DONE"))   # "DONE" ← default, no crash!
print(next(iterator, None))     # None   ← another safe default
print(next(iterator, 0))        # 0
```

```python
# ─── iter() with sentinel value ───
# iter(callable, sentinel) — calls callable until it returns sentinel!

import random
random.seed(42)

# Roll a die until we get a 6:
rolls = list(iter(lambda: random.randint(1, 6), 6))
print(rolls)   # [1, 5, 3, 4, 3, 4, 1, ...]  ← everything before the 6

# Read file lines until empty line:
# line_iter = iter(file.readline, "")
# lines = list(line_iter)
```

---

## 🔍 How for Loops Really Work

> A `for` loop is just **syntactic sugar** for the iterator protocol!

```python
# This for loop:
for item in [1, 2, 3]:
    print(item)

# Is EXACTLY equivalent to this:
_iter = iter([1, 2, 3])        # 1. Get iterator from iterable
while True:
    try:
        item = next(_iter)     # 2. Get next item
        print(item)            # 3. Execute body
    except StopIteration:
        break                  # 4. Stop when exhausted
```

```python
# This is WHY you can use for loops on anything that has __iter__!
# Strings, lists, tuples, dicts, sets, files, generators...
# They ALL just need to return an iterator!

for char in "Hello":           print(char)   # str iterator
for item in (1, 2, 3):        print(item)   # tuple iterator
for key  in {"a":1, "b":2}:  print(key)    # dict_keyiterator
for line in open("file.txt"): print(line)   # file object IS an iterator
```

---

## 🧰 Built-in Iterators

> Python gives you lots of built-in iterators — most are **lazy** (compute on demand)!

```python
# ─── enumerate() ───
# Yields (index, value) pairs
fruits = ["apple", "banana", "cherry"]
enum   = enumerate(fruits, start=1)

print(next(enum))   # (1, 'apple')
print(next(enum))   # (2, 'banana')

for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# ─── zip() ───
# Pairs up multiple iterables element-by-element
names  = ["Alice", "Bob", "Charlie"]
scores = [88, 95, 72]
zipped = zip(names, scores)

print(next(zipped))   # ('Alice', 88)
print(next(zipped))   # ('Bob', 95)

for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# ─── map() ───
# Applies function to each element lazily
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)

print(next(squared))   # 1
print(next(squared))   # 4
print(list(squared))   # [9, 16, 25]  ← rest

# ─── filter() ───
# Yields only items where function returns True
evens = filter(lambda x: x % 2 == 0, range(10))

print(next(evens))   # 0
print(next(evens))   # 2
print(list(evens))   # [4, 6, 8]

# ─── reversed() ───
rev = reversed([1, 2, 3, 4, 5])
print(next(rev))   # 5
print(next(rev))   # 4

# ─── All are LAZY — compute nothing until asked! ───
import sys
big_map    = map(lambda x: x**2, range(10**9))   # 🪶 barely any memory
big_list   = [x**2 for x in range(10**6)]        # 🐘 millions of numbers in RAM!
print(sys.getsizeof(big_map))    # ~56 bytes!
```

```python
# ─── File objects are iterators! ───
with open("data.txt") as f:
    print(iter(f) is f)     # True! file IS its own iterator
    first_line = next(f)    # get one line at a time
    second_line = next(f)
    # for line in f: ...    # continues from where we left off!
```

---

## 🏗️ Building Your Own Iterator Class

### Level 1 — Simple Range

```python
class MyRange:
    """
    A simplified version of Python's range().
    Demonstrates the iterator protocol from scratch.
    """
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError("step cannot be zero")
        self.start   = start
        self.stop    = stop
        self.step    = step
        self.current = start

    def __iter__(self):
        """Return self — we ARE the iterator."""
        return self

    def __next__(self):
        """Return next value or raise StopIteration."""
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value        = self.current
        self.current += self.step
        return value

    def __repr__(self):
        return f"MyRange({self.start}, {self.stop}, {self.step})"


# Test it:
for n in MyRange(1, 6):
    print(n, end=" ")
# 1 2 3 4 5

for n in MyRange(10, 0, -2):
    print(n, end=" ")
# 10 8 6 4 2

print(list(MyRange(0, 10, 3)))
# [0, 3, 6, 9]
```

---

### Level 2 — Separate Iterable and Iterator

```python
# IMPORTANT pattern: the ITERABLE creates fresh iterators
# so you can loop over it MULTIPLE TIMES!

class NumberList:
    """
    The ITERABLE class — holds data, creates fresh iterators.
    You can loop over this multiple times!
    """
    def __init__(self, *numbers):
        self.numbers = list(numbers)

    def __iter__(self):
        # Return a FRESH iterator each time!
        return NumberListIterator(self.numbers)


class NumberListIterator:
    """
    The ITERATOR class — holds position state.
    Created fresh by NumberList.__iter__() each time.
    """
    def __init__(self, numbers):
        self.numbers = numbers
        self.index   = 0        # ← position state lives HERE

    def __iter__(self):
        return self             # iterator is also iterable!

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value      = self.numbers[self.index]
        self.index += 1
        return value


# Now we can loop MULTIPLE times (unlike an iterator):
nums = NumberList(10, 20, 30, 40, 50)

for n in nums: print(n, end=" ")   # 10 20 30 40 50
print()
for n in nums: print(n, end=" ")   # 10 20 30 40 50  ← fresh start! ✅
print()

# Create two independent iterators from same object:
it1 = iter(nums)
it2 = iter(nums)
print(next(it1))   # 10  ← it1 at position 1
print(next(it1))   # 20  ← it1 at position 2
print(next(it2))   # 10  ← it2 independently at position 1! ✅
```

---

### Level 3 — Iterator with Filtering

```python
class FilteredIterator:
    """
    Iterates over a sequence, skipping items that don't pass a test.
    Lazy — only evaluates the predicate when asked!
    """
    def __init__(self, iterable, predicate):
        self._iter      = iter(iterable)
        self._predicate = predicate

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iter)   # raises StopIteration when done
            if self._predicate(item):
                return item
            # if predicate is False, loop again to get next item

# Use it:
evens = FilteredIterator(range(20), lambda x: x % 2 == 0)
for n in evens:
    print(n, end=" ")
# 0 2 4 6 8 10 12 14 16 18

long_words = FilteredIterator(
    ["cat", "elephant", "ox", "hippopotamus", "ant"],
    lambda w: len(w) > 4
)
print(list(long_words))
# ['elephant', 'hippopotamus']
```

---

### Level 4 — Chained Iterator

```python
class ChainIterator:
    """
    Chain multiple iterables together, one after another.
    Like itertools.chain — built from scratch!
    """
    def __init__(self, *iterables):
        self._iters = iter(iterables)     # iterator over the iterables
        self._current = iter([])          # start with an empty iterator

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return next(self._current)   # try current iterator
            except StopIteration:
                # current exhausted — move to next iterable
                self._current = iter(next(self._iters))
                # if _iters is also exhausted, StopIteration propagates ✅

# Use it:
chained = ChainIterator([1,2,3], "ABC", range(4,7))
print(list(chained))
# [1, 2, 3, 'A', 'B', 'C', 4, 5, 6]
```

---

## ♾️ Infinite Iterators

> Iterators don't have to stop! They can produce values **forever**.
> Just be careful to break out of them! 🔒

```python
class InfiniteCounter:
    """Count upward forever from start."""
    def __init__(self, start=0, step=1):
        self.current = start
        self.step    = step

    def __iter__(self):
        return self

    def __next__(self):
        value         = self.current
        self.current += self.step
        return value


# Use with take() or break!
counter = InfiniteCounter(1)

# Take first 5:
from itertools import islice
first_five = list(islice(counter, 5))
print(first_five)   # [1, 2, 3, 4, 5]

# Use with break:
counter2 = InfiniteCounter(1)
for n in counter2:
    if n > 8:
        break
    print(n, end=" ")
# 1 2 3 4 5 6 7 8
```

```python
class FibonacciIterator:
    """Generate Fibonacci numbers forever."""
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        value    = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

fib = FibonacciIterator()
first_ten = [next(fib) for _ in range(10)]
print(first_ten)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

```python
class CyclicIterator:
    """Cycle through a sequence forever."""
    def __init__(self, iterable):
        self.data    = list(iterable)
        if not self.data:
            raise ValueError("Cannot cycle over empty iterable")
        self.index   = 0

    def __iter__(self):
        return self

    def __next__(self):
        value      = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return value

seasons = CyclicIterator(["Spring", "Summer", "Autumn", "Winter"])
for _ in range(10):
    print(next(seasons), end=" ")
# Spring Summer Autumn Winter Spring Summer Autumn Winter Spring Summer
```

---

## 🛠️ itertools Module — The Iterator Toolkit

> `itertools` is Python's built-in toolkit of **iterator building blocks**.
> It's fast (C-speed), memory-efficient (lazy), and incredibly powerful.

```python
import itertools
```

### Infinite Iterators

```python
# ─── count(start, step) — count forever ───
counter = itertools.count(1, 2)   # 1, 3, 5, 7, 9 ...
print(list(itertools.islice(counter, 5)))   # [1, 3, 5, 7, 9]

# ─── cycle(iterable) — repeat forever ───
traffic = itertools.cycle(["🔴 Red", "🟡 Yellow", "🟢 Green"])
for _ in range(6):
    print(next(traffic))
# 🔴 Red, 🟡 Yellow, 🟢 Green, 🔴 Red, 🟡 Yellow, 🟢 Green

# ─── repeat(value, n) — repeat n times (or forever) ───
fives = itertools.repeat(5, 4)
print(list(fives))   # [5, 5, 5, 5]

three_pis = itertools.repeat(3.14)   # forever
print(next(three_pis))   # 3.14
```

### Terminating Iterators

```python
# ─── islice(iterable, stop) or (start, stop, step) ───
gen  = (x**2 for x in range(100))
print(list(itertools.islice(gen, 5)))           # [0, 1, 4, 9, 16]
print(list(itertools.islice(range(20), 2, 10, 2))) # [2, 4, 6, 8] start, stop, step

# ─── takewhile(pred, iterable) — take while condition is True ───
nums = [1, 3, 5, 7, 8, 9, 11]   # mostly odd but 8 breaks the streak
odds = list(itertools.takewhile(lambda x: x % 2 != 0, nums))
print(odds)   # [1, 3, 5, 7]   ← stopped when 8 was hit!

# ─── dropwhile(pred, iterable) — skip while condition is True ───
rest = list(itertools.dropwhile(lambda x: x % 2 != 0, nums))
print(rest)   # [8, 9, 11]   ← dropped odds until 8

# ─── filterfalse(pred, iterable) — keep when pred is FALSE ───
evens = list(itertools.filterfalse(lambda x: x%2==1, range(10)))
print(evens)   # [0, 2, 4, 6, 8]

# ─── compress(data, selectors) — keep where selector is True ───
data      = ['a', 'b', 'c', 'd', 'e']
selectors = [1, 0, 1, 0, 1]
kept      = list(itertools.compress(data, selectors))
print(kept)   # ['a', 'c', 'e']

# ─── starmap(func, iterable) — like map but unpacks tuples ───
pairs   = [(2, 3), (4, 2), (3, 3)]
results = list(itertools.starmap(pow, pairs))
print(results)   # [8, 16, 27]   ← 2³, 4², 3³

# ─── chain(*iterables) — join iterables end to end ───
letters = list(itertools.chain("ABC", "DEF", "GH"))
print(letters)   # ['A','B','C','D','E','F','G','H']

combined = list(itertools.chain([1,2], [3,4], [5,6]))
print(combined)  # [1, 2, 3, 4, 5, 6]

# ─── chain.from_iterable — chain from a nested list ───
nested  = [[1,2,3], [4,5,6], [7,8,9]]
flat    = list(itertools.chain.from_iterable(nested))
print(flat)   # [1,2,3,4,5,6,7,8,9]

# ─── zip_longest — zip but pad shorter iterables ───
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c"]
pairs = list(itertools.zip_longest(a, b, fillvalue="?"))
print(pairs)   # [(1,'a'),(2,'b'),(3,'c'),(4,'?'),(5,'?')]

# ─── accumulate — running total ───
import operator
nums  = [1, 2, 3, 4, 5]
running = list(itertools.accumulate(nums))
print(running)  # [1, 3, 6, 10, 15]  ← cumulative sum

products = list(itertools.accumulate(nums, operator.mul))
print(products) # [1, 2, 6, 24, 120] ← running product

maximums = list(itertools.accumulate(nums, max))
print(maximums) # [1, 2, 3, 4, 5]    ← running max
```

### Combinatorial Iterators

```python
# ─── product — cartesian product (nested for loops!) ───
cards = list(itertools.product("AKQJ", ["♠","♥","♦","♣"]))
print(len(cards))    # 16
print(cards[:4])     # [('A','♠'),('A','♥'),('A','♦'),('A','♣')]

# repeat argument:
dice = list(itertools.product(range(1,7), repeat=2))
print(len(dice))     # 36 combinations for 2 dice

# ─── permutations — all orderings ───
perms = list(itertools.permutations("ABC"))
print(perms)   # [('A','B','C'),('A','C','B'),('B','A','C'),...]
print(len(perms))  # 6  (3! = 6)

perms_2 = list(itertools.permutations("ABCD", 2))
print(len(perms_2))  # 12  (4 choices × 3 choices)

# ─── combinations — choose r from n (order doesn't matter) ───
combos = list(itertools.combinations("ABCD", 2))
print(combos)   # [('A','B'),('A','C'),('A','D'),('B','C'),('B','D'),('C','D')]
print(len(combos))  # 6  (4 choose 2 = 6)

# ─── combinations_with_replacement — like combinations but repeats allowed ───
combos_r = list(itertools.combinations_with_replacement("ABC", 2))
print(combos_r)  # [('A','A'),('A','B'),('A','C'),('B','B'),('B','C'),('C','C')]

# ─── groupby — group consecutive elements ───
data = [
    {"name": "Alice",   "dept": "Engineering"},
    {"name": "Bob",     "dept": "Engineering"},
    {"name": "Carol",   "dept": "Marketing"},
    {"name": "Dave",    "dept": "Marketing"},
    {"name": "Eve",     "dept": "Engineering"},  # ← not consecutive with above!
]

# Sort FIRST (groupby only groups consecutive equal keys!)
sorted_data = sorted(data, key=lambda x: x["dept"])

print("Departments:")
for dept, employees in itertools.groupby(sorted_data, key=lambda x: x["dept"]):
    names = [e["name"] for e in employees]
    print(f"  {dept}: {names}")
# Engineering: ['Alice', 'Bob', 'Eve']
# Marketing: ['Carol', 'Dave']
```

---

## 🔗 Chaining and Combining Iterators

```python
# ─── Build a lazy data pipeline ───
data = range(1, 101)   # numbers 1 to 100

# Step 1: filter multiples of 3
step1 = filter(lambda x: x % 3 == 0, data)

# Step 2: square them
step2 = map(lambda x: x**2, step1)

# Step 3: take first 5
step3 = itertools.islice(step2, 5)

# Step 4: collect
result = list(step3)
print(result)   # [9, 36, 81, 144, 225]
# 3²=9, 6²=36, 9²=81, 12²=144, 15²=225

# 🔑 Nothing computed until list() at the end!
# The entire pipeline is lazy. Zero wasted work.
```

```python
# ─── Zip multiple iterators ───
# Interleave two iterators:
odds  = itertools.islice(itertools.count(1, 2), 5)   # 1,3,5,7,9
evens = itertools.islice(itertools.count(2, 2), 5)   # 2,4,6,8,10

interleaved = list(itertools.chain.from_iterable(zip(odds, evens)))
print(interleaved)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## 🔌 Iterator Protocol in Practice

```python
# ─── Making a class support len() AND iteration ───
class Cards:
    """A deck of playing cards — iterable, sized, subscriptable."""

    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self):
        self._cards = [f"{r}{s}" for s in self.SUITS for r in self.RANKS]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]   # this makes it ITERABLE automatically!
    # __getitem__ implements iteration too — Python falls back to index 0,1,2,...!

deck = Cards()
print(len(deck))       # 52
print(deck[0])         # A♠
print(deck[-1])        # K♣

# Iterates via __getitem__ even without __iter__!
top5 = list(itertools.islice(deck, 5))
print(top5)   # ['A♠', '2♠', '3♠', '4♠', '5♠']

# Supports slicing because of __getitem__!
print(deck[48:])   # last 4 cards
```

---

## 💾 Memory: Iterator vs List

```python
import sys

n = 1_000_000

# LIST — stores everything NOW
nums_list = list(range(n))
print(f"List:      {sys.getsizeof(nums_list):>12,} bytes")  # ~8,448,728 bytes

# RANGE — stores only 3 numbers (start, stop, step)
nums_range = range(n)
print(f"Range:     {sys.getsizeof(nums_range):>12,} bytes")  # 48 bytes!

# MAP — stores only the function + source iterator
nums_map = map(lambda x: x**2, range(n))
print(f"Map:       {sys.getsizeof(nums_map):>12,} bytes")    # 56 bytes!

# GENERATOR EXPRESSION — lazy evaluation
nums_gen = (x**2 for x in range(n))
print(f"Generator: {sys.getsizeof(nums_gen):>12,} bytes")   # 104 bytes!
```

```
Memory usage:
  List      : 8,448,728 bytes  🐘🐘🐘🐘🐘🐘🐘🐘
  Range     :        48 bytes  🪶
  Map       :        56 bytes  🪶
  Generator :       104 bytes  🪶

→ 80,000x more memory for the list!
```

---

## 🌍 Real-World Iterator Projects

### Project 1 — Lazy CSV Reader

```python
class CSVIterator:
    """
    Read a CSV file lazily — one row at a time.
    Perfect for files too large to fit in memory!
    """
    def __init__(self, filename, delimiter=",", has_header=True):
        self.filename  = filename
        self.delimiter = delimiter
        self.header    = None
        self._file     = None
        self._iter     = None

    def __iter__(self):
        return self

    def __enter__(self):
        import csv
        self._file   = open(self.filename, "r", newline="", encoding="utf-8")
        self._reader = csv.DictReader(self._file, delimiter=self.delimiter)
        return self

    def __exit__(self, *args):
        if self._file:
            self._file.close()

    def __next__(self):
        try:
            return next(self._reader)
        except StopIteration:
            if self._file:
                self._file.close()
            raise

# Usage:
# with CSVIterator("huge_file.csv") as csv_iter:
#     for row in csv_iter:
#         process(row)   # one row at a time — constant memory!
```

---

### Project 2 — Sliding Window Iterator

```python
class SlidingWindow:
    """
    Produce overlapping windows of size `n` over a sequence.

    Example: SlidingWindow([1,2,3,4,5], 3)
    → (1,2,3), (2,3,4), (3,4,5)
    """
    def __init__(self, iterable, window_size):
        self.data        = list(iterable)
        self.window_size = window_size
        self.index       = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index + self.window_size > len(self.data):
            raise StopIteration
        window      = tuple(self.data[self.index : self.index + self.window_size])
        self.index += 1
        return window

# Usage:
prices     = [100, 102, 101, 105, 110, 108, 112, 115]
windows    = SlidingWindow(prices, 3)

print("3-Day Moving Averages:")
for day, window in enumerate(windows, start=1):
    avg = sum(window) / len(window)
    print(f"  Days {day}-{day+2}: {window} → avg = {avg:.1f}")
```

---

### Project 3 — Paginated API Iterator

```python
class PaginatedResults:
    """
    Iterate over paginated API results transparently.
    Fetches next page automatically when current page is exhausted.
    """
    def __init__(self, base_url, page_size=10):
        self.base_url  = base_url
        self.page_size = page_size
        self.page      = 1
        self.buffer    = []
        self.exhausted = False

    def __iter__(self):
        return self

    def _fetch_page(self):
        """Fetch the next page of results."""
        # Simulated — in real code this would be an HTTP request
        if self.page > 3:    # simulate 3 pages total
            return []
        items = [f"item_{(self.page-1)*self.page_size + i}"
                 for i in range(1, self.page_size + 1)]
        self.page += 1
        return items

    def __next__(self):
        if self.exhausted:
            raise StopIteration

        if not self.buffer:
            self.buffer = self._fetch_page()
            if not self.buffer:
                self.exhausted = True
                raise StopIteration

        return self.buffer.pop(0)

# Usage — caller doesn't know or care about pagination!
results = PaginatedResults("https://api.example.com/items", page_size=5)

for i, item in enumerate(results, 1):
    print(f"  {i:2}. {item}")
# 1. item_1  2. item_2 ...  30. item_30
```

---

## 🚨 Common Mistakes

### Mistake 1 — Thinking an Exhausted Iterator Can Restart

```python
nums  = [1, 2, 3, 4, 5]
it    = iter(nums)

for n in it: print(n)   # 1 2 3 4 5
for n in it: print(n)   # ← prints NOTHING! exhausted!

# ✅ Fix: create a new iterator each time
for n in iter(nums): print(n)  # fresh iterator ✅
for n in nums:       print(n)  # also fine ✅
```

### Mistake 2 — Confusing Iterable with Iterator

```python
# ❌ Wrong assumption — lists don't have __next__!
my_list = [1, 2, 3]
next(my_list)   # TypeError: list object is not an iterator

# ✅ Must call iter() first to get an iterator:
it = iter(my_list)
next(it)   # 1 ✅
```

### Mistake 3 — Modifying Source During Iteration

```python
# ❌ Modifying a list while iterating over it!
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)   # 😱 skips items!
print(nums)   # [1, 3, 5] but missed some!

# ✅ Iterate over a copy, modify the original:
for n in nums[:]:   # nums[:] creates a copy to iterate
    if n % 2 == 0:
        nums.remove(n)

# ✅ Or build a new list:
nums = [n for n in nums if n % 2 != 0]
```

### Mistake 4 — Forgetting StopIteration in Custom Iterator

```python
# ❌ Missing StopIteration — loops forever!
class BadCounter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self): return self

    def __next__(self):
        value = self.i
        self.i += 1
        return value   # ← never stops! infinite loop in for!

# ✅ Always raise StopIteration when done:
class GoodCounter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self): return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration   # ← REQUIRED!
        value = self.i
        self.i += 1
        return value
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔑  THE PROTOCOL
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Iterable  → has __iter__()  (list, str, dict, set, range...)
# Iterator  → has __iter__() + __next__()

# Creating:
it = iter(iterable)      # get iterator from iterable
v  = next(iterator)      # get next value
v  = next(it, default)   # safe: returns default instead of StopIteration

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️  CUSTOM ITERATOR TEMPLATE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class MyIterator:
    def __init__(self, data):
        self._data  = data
        self._index = 0

    def __iter__(self):
        return self             # return self!

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration  # MUST raise this!
        value        = self._data[self._index]
        self._index += 1
        return value

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️  KEY itertools
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import itertools

itertools.count(start, step)           # infinite counter
itertools.cycle(iterable)              # infinite cycler
itertools.repeat(value, n)             # repeat n times
itertools.islice(it, stop)             # take first N
itertools.islice(it, start, stop, step)
itertools.takewhile(pred, it)          # take while True
itertools.dropwhile(pred, it)          # skip while True
itertools.filterfalse(pred, it)        # keep when False
itertools.compress(data, selectors)    # mask-based filter
itertools.chain(*iterables)            # join end to end
itertools.chain.from_iterable(nested)  # flatten one level
itertools.zip_longest(a, b, fillvalue=None)
itertools.accumulate(it, func)         # running result
itertools.starmap(func, pairs)         # map with tuple args
itertools.product(*its, repeat=1)      # cartesian product
itertools.permutations(it, r)          # all orderings of r
itertools.combinations(it, r)          # choose r unordered
itertools.groupby(it, key)             # group consecutive

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧪  CHECK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from collections.abc import Iterator, Iterable
isinstance(obj, Iterable)   # can it be iterated?
isinstance(obj, Iterator)   # is it an iterator?

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡  BUILT-IN ITERATORS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

iter([1,2,3])            # list_iterator
enumerate(lst)           # enumerate object
zip(a, b)                # zip object
map(fn, it)              # map object
filter(fn, it)           # filter object
reversed(lst)            # list_reverseiterator
open("file.txt")         # file object (is its own iterator!)
```

---

## 🎓 Final Summary

```
Iterators in Python:
──────────────────────────────────────────────────────────────
CORE IDEA
  Iterator = object that gives one item at a time,
             remembers its position, raises StopIteration when done.

PROTOCOL (just 2 methods!)
  __iter__(self)  → return self
  __next__(self)  → return next item OR raise StopIteration

ITERABLE vs ITERATOR
  Iterable  = can produce iterators (list, str, dict, set, range)
  Iterator  = stateful, one-pass, position-aware object
  All iterators are also iterables (iter(it) returns itself)
  Not all iterables are iterators

HOW for LOOPS WORK
  it = iter(collection)
  while True:
      try: item = next(it)
      except StopIteration: break

KEY BENEFITS
  ✅ Memory efficient (one item at a time)
  ✅ Lazy evaluation (compute on demand)
  ✅ Works on infinite sequences
  ✅ Composable (chain, filter, map lazily)

GOLDEN RULE
  If you only need to go through data ONCE → use iterator
  If you need to go through it MULTIPLE TIMES → use list/tuple
──────────────────────────────────────────────────────────────
```

---
