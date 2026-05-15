# 🧵 String Concepts — Complete Revision Guide

---

## 1. What is a String?

A **string** is a sequence of characters stored in memory. It can contain letters, digits, symbols, and whitespace.

```python
s = "Hello, World!"
``` 

Strings are:
- **Immutable** in most languages (Python, Java, JavaScript)
- **Mutable** in some (C++ `std::string`, C char arrays)
- **Zero-indexed** — first character is at index `0`

---

## 2. String Representation in Memory

- Stored as an array of characters
- In C: null-terminated `\0` at the end → `"abc"` = `['a', 'b', 'c', '\0']`
- In Python/Java: length is stored separately (no null terminator needed)

---

## 3. Basic String Operations

| Operation         | Description                         | Example                        |
|------------------|-------------------------------------|-------------------------------|
| Length            | Number of characters                | `len("hello")` → 5            |
| Concatenation     | Join two strings                    | `"ab" + "cd"` → `"abcd"`      |
| Repetition        | Repeat string                       | `"ab" * 3` → `"ababab"`       |
| Indexing          | Access character at index           | `"hello"[1]` → `'e'`          |
| Slicing           | Extract substring                   | `"hello"[1:4]` → `"ell"`      |
| Membership        | Check if substring exists           | `"ell" in "hello"` → True     |
| Comparison        | Lexicographic comparison            | `"abc" < "abd"` → True        |

---

## 4. String Traversal

```python
s = "hello"

# Forward
for ch in s:
    print(ch)

# Using index
for i in range(len(s)):
    print(s[i])

# Reverse
for i in range(len(s) - 1, -1, -1):
    print(s[i])
```

---

## 5. Substrings & Slicing

```python
s = "abcdef"

s[1:4]    # "bcd"   → from index 1 to 3 (exclusive 4)
s[:3]     # "abc"   → from start to index 2
s[3:]     # "def"   → from index 3 to end
s[::2]    # "ace"   → every 2nd character
s[::-1]   # "fedcba"→ reverse
```

**Substring check:**
```python
"bc" in "abcdef"   # True
s.find("cd")       # Returns 2 (index), -1 if not found
s.index("cd")      # Returns 2, raises ValueError if not found
```

---

## 6. Common String Methods

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"   — remove leading/trailing spaces
s.lstrip()          # remove left spaces
s.rstrip()          # remove right spaces
s.lower()           # "hello, world!"
s.upper()           # "HELLO, WORLD!"
s.title()           # "Hello, World!"
s.capitalize()      # "Hello, world!"
s.replace("World", "Python")  # "Hello, Python!"
s.split(", ")       # ["Hello", "World!"]
", ".join(["a","b","c"])      # "a, b, c"
s.startswith("He")  # True
s.endswith("!")     # True
s.count("l")        # 3
s.isalpha()         # False (has spaces/punctuation)
s.isdigit()         # False
s.isalnum()         # False
s.isspace()         # False
s.center(20, "*")   # "**Hello, World!***"
s.zfill(5)          # pad with zeros on left
```

---

## 7. String Immutability

```python
s = "hello"
s[0] = 'H'   # ❌ TypeError — strings are immutable in Python

# To modify:
s = 'H' + s[1:]   # ✅ "Hello"
```

---

## 8. String Formatting

```python
name = "Alice"
age = 25

# f-string (recommended)
f"Name: {name}, Age: {age}"

# format()
"Name: {}, Age: {}".format(name, age)

# % formatting (old style)
"Name: %s, Age: %d" % (name, age)
```

---

## 9. ASCII & Character Conversion

```python
ord('A')    # 65  — character to ASCII
chr(65)     # 'A' — ASCII to character
ord('a')    # 97
ord('0')    # 48

# Lowercase check: 97 <= ord(c) <= 122
# Uppercase check: 65 <= ord(c) <= 90
# Digit check: 48 <= ord(c) <= 57
```

---

## 10. String as Character Array

```python
s = "hello"

# Convert to list for mutability
chars = list(s)     # ['h', 'e', 'l', 'l', 'o']
chars[0] = 'H'
result = ''.join(chars)   # "Hello"
```

---

## 11. Palindrome Check

```python
def is_palindrome(s):
    return s == s[::-1]

# Two-pointer approach
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
```

---

## 12. Anagram Check

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Without Counter
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```

---

## 13. Frequency Count

```python
from collections import Counter

s = "aabbccc"
freq = Counter(s)   # Counter({'c': 3, 'a': 2, 'b': 2})

# Manual
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```

---

## 14. Sliding Window on Strings

Used for: longest substring without repeating, minimum window substring, etc.

```python
# Longest substring without repeating characters
def length_of_longest_substring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```

---

## 15. Two-Pointer on Strings

```python
# Reverse a string in-place (as list)
def reverse(s):
    chars = list(s)
    l, r = 0, len(chars) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1
    return ''.join(chars)
```

---

## 16. Pattern Matching

### Naive Approach — O(n × m)
```python
def search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
```

### KMP Algorithm — O(n + m)
- Precompute **LPS (Longest Prefix Suffix)** array
- Avoids re-checking characters already matched

```python
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == m:
            return i - j   # found at index
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```

---

## 17. String Compression

```python
def compress(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i + count] == s[i]:
            count += 1
        result.append(s[i] + (str(count) if count > 1 else ''))
        i += count
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s
```

---

## 18. Reverse Words in a String

```python
s = "  Hello World  "

# Python one-liner
' '.join(s.split()[::-1])

# Manual
words = s.strip().split()
words.reverse()
' '.join(words)
```

---

## 19. String Rotation

```python
# s2 is a rotation of s1 if s2 appears in s1+s1
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
```

---

## 20. Important DSA Problems on Strings

| Problem | Key Technique |
|---|---|
| Longest Substring Without Repeating | Sliding Window + HashMap |
| Minimum Window Substring | Sliding Window |
| Valid Anagram | Frequency Count |
| Group Anagrams | Sorting / Counter as key |
| Longest Palindromic Substring | Expand Around Center / DP |
| Palindromic Substrings Count | Expand Around Center |
| Encode and Decode Strings | Delimiter / Length prefix |
| Find All Anagrams in String | Sliding Window |
| Longest Common Prefix | Vertical scan / Binary search |
| String to Integer (atoi) | Careful parsing |
| Zigzag Conversion | Index math |
| Repeated DNA Sequences | Sliding Window + HashSet |

---

## 21. Time & Space Complexity Summary

| Operation | Time | Space |
|---|---|---|
| Access by index | O(1) | O(1) |
| Substring / Slice | O(k) | O(k) |
| Search (naive) | O(n×m) | O(1) |
| Search (KMP) | O(n+m) | O(m) |
| Sort string | O(n log n) | O(n) |
| Frequency count | O(n) | O(k) — k = unique chars |
| Concatenation loop | O(n²) | Use join instead |

---

## 22. Tips & Tricks

- Use `''.join(list)` instead of `+=` for string building in loops → O(n) vs O(n²)
- Use `Counter` for frequency problems
- `ord(c) - ord('a')` gives 0-based index for lowercase letters
- Sliding window is the go-to for substring problems
- Two pointers work great for palindrome and reversal problems
- For pattern matching in interviews → know KMP conceptually
- Always handle edge cases: empty string, single character, all same characters

---

*Happy Revising! 🚀*