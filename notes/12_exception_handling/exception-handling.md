# 🐍 Python Exception Handling — Zero to Hero
## Every Exception · Every Pattern · Every Technique · Advanced Mastery

> 🧠 **What is an Exception?**
> An exception is Python's way of saying **"Something went wrong!"**
> When Python hits a problem it can't continue from — it STOPS and
> raises an exception. If you don't handle it, your program **crashes** 💥
>
> Exception handling is how you say:
> *"I know something might go wrong here — and here's my plan!"*
>
> ```python
> # Without handling — program DIES 💀
> number = int("hello")     # ValueError: invalid literal
> print("This never runs")  # ← never reached!
>
> # With handling — program SURVIVES 💪
> try:
>     number = int("hello")
> except ValueError:
>     print("That's not a number!")
> print("Program continues!")   # ← this runs! ✅
> ```
>
> Think of it like a **safety net** 🎪 under a tightrope walker.
> You hope you don't need it — but you're VERY glad it's there!

---

## 📚 Table of Contents

1. [The try-except Block](#-the-try-except-block)
2. [Catching Specific Exceptions](#-catching-specific-exceptions)
3. [Multiple except Clauses](#-multiple-except-clauses)
4. [The else Clause](#-the-else-clause)
5. [The finally Clause](#-the-finally-clause)
6. [The Full try-except-else-finally](#-the-full-try-except-else-finally)
7. [Exception Object — as e](#-exception-object--as-e)
8. [Raising Exceptions — raise](#-raising-exceptions--raise)
9. [Re-raising Exceptions](#-re-raising-exceptions)
10. [Exception Chaining — from](#-exception-chaining--from)
11. [Built-in Exceptions — Complete Hierarchy](#-built-in-exceptions--complete-hierarchy)
12. [Custom Exceptions](#-custom-exceptions)
13. [Context Managers & Exceptions](#-context-managers--exceptions)
14. [Warnings](#-warnings)
15. [Logging Exceptions](#-logging-exceptions)
16. [Exception Handling Patterns](#-exception-handling-patterns)
17. [Real-World Projects](#-real-world-projects)
18. [Common Mistakes](#-common-mistakes)
19. [Cheat Sheet](#-cheat-sheet)

---

## 🛡️ The try-except Block

> The most fundamental tool: **try the risky code, catch the problem**.

```python
# Syntax:
try:
    # risky code goes here
    # if ANY line raises an exception → jump to except
except:
    # runs ONLY if an exception occurred in try
    # handles the problem gracefully
```

```python
# ─── The simplest example ───
try:
    result = 10 / 0          # 💥 ZeroDivisionError!
    print("Never reached")
except:
    print("Oops! Division by zero!")

print("Program continues...")   # ✅ this still runs!

# Output:
# Oops! Division by zero!
# Program continues...
```

```python
# ─── Without exception handling ───
x = int("abc")     # 💀 crash — program stops here
print("Never")     # never runs

# ─── With exception handling ───
try:
    x = int("abc")
    print("Converted!")
except:
    print("⚠️  Conversion failed!")
print("Moving on...")   # ✅ runs!
```

> ⚠️ **Bare `except:` catches EVERYTHING** — including system exits!
> Almost always a bad idea. Use specific exceptions instead (next section).

---

## 🎯 Catching Specific Exceptions

> Always catch the **most specific** exception you expect.
> This prevents hiding unexpected bugs!

```python
# Syntax:
try:
    risky_code()
except SpecificException:
    handle_it()
```

```python
# ─── Common specific exceptions ───

# ValueError — wrong VALUE type
try:
    age = int("twenty")
except ValueError:
    print("⚠️  Please enter a number, not text!")

# ZeroDivisionError — divide by zero
try:
    result = 100 / 0
except ZeroDivisionError:
    print("⚠️  Cannot divide by zero!")

# IndexError — list index out of range
try:
    items = [1, 2, 3]
    print(items[10])
except IndexError:
    print("⚠️  That index doesn't exist!")

# KeyError — dictionary key not found
try:
    data = {"name": "Alice"}
    print(data["age"])
except KeyError:
    print("⚠️  Key 'age' not found in dictionary!")

# TypeError — wrong TYPE for operation
try:
    result = "hello" + 42
except TypeError:
    print("⚠️  Can't add string and integer!")

# AttributeError — object has no such attribute
try:
    x = None
    x.upper()
except AttributeError:
    print("⚠️  None has no .upper() method!")

# FileNotFoundError — file doesn't exist
try:
    with open("ghost.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("⚠️  File not found!")

# NameError — variable not defined
try:
    print(undefined_variable)
except NameError:
    print("⚠️  Variable not defined!")
```

---

## 🔀 Multiple except Clauses

> Handle different exceptions **differently** — like different error messages.

```python
# Syntax:
try:
    risky_code()
except ExceptionA:
    handle_a()
except ExceptionB:
    handle_b()
except ExceptionC:
    handle_c()
```

```python
# ─── User input validator ───
def process_input(raw):
    try:
        number = int(raw)
        result = 100 / number
        items  = [1, 2, 3]
        value  = items[number]
        return result, value

    except ValueError:
        print("  ❌ Not a number! Enter digits only.")
    except ZeroDivisionError:
        print("  ❌ Zero is not allowed — division by zero!")
    except IndexError:
        print("  ❌ Number too large — index out of range!")

process_input("hello")   # ValueError
process_input("0")       # ZeroDivisionError
process_input("99")      # IndexError
process_input("2")       # ✅ works: (50.0, 3)
```

```python
# ─── Catching multiple exceptions in ONE clause ───
try:
    value = int(input("Enter number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError):
    print("⚠️  Invalid input or division by zero!")
```

```python
# ─── Hierarchy: specific FIRST, broad LAST ───
try:
    risky_operation()
except FileNotFoundError:        # most specific ← first
    print("File missing!")
except PermissionError:          # still specific
    print("No permission!")
except OSError:                  # broader — catches both above if not caught
    print("OS error!")
except Exception:                # very broad — catch-all for unexpected
    print("Unexpected error!")
# except BaseException:          # catches KeyboardInterrupt, SystemExit too!
```

---

## ✅ The else Clause

> `else` runs **only if NO exception occurred** in the `try` block.
> Use it for code that should run on success — keeps logic clean!

```python
# Syntax:
try:
    risky_code()
except SomeError:
    handle_error()
else:
    # runs ONLY if try succeeded — no exception!
    success_code()
```

```python
# ─── File reading with else ───
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("  ❌ File not found!")
    content = ""
else:
    # ONLY runs if file was opened successfully
    print(f"  ✅ File read! {len(content)} characters")
    print(f"  Preview: {content[:50]}...")
```

```python
# ─── Database query style ───
def find_user(user_id):
    database = {1: "Alice", 2: "Bob", 3: "Charlie"}

    try:
        user = database[user_id]
    except KeyError:
        print(f"  ❌ User #{user_id} not found!")
        return None
    else:
        # success path — clean separation from error path
        print(f"  ✅ Found user: {user}")
        return user

find_user(2)    # ✅ Found user: Bob
find_user(99)   # ❌ User #99 not found!
```

```python
# ─── Why else is better than putting code in try ───

# ❌ Bad: everything in try — hides potential errors!
try:
    user = get_user(id)
    email = user.send_welcome_email()   # ← if THIS fails, caught by except!
    log_signup(user)                    # ← and this too!
except KeyError:
    print("User not found")            # ← but we might catch wrong errors!

# ✅ Good: only risky code in try, success code in else
try:
    user = get_user(id)     # ONLY this might raise KeyError
except KeyError:
    print("User not found")
else:
    email = user.send_welcome_email()  # errors here NOT caught by KeyError
    log_signup(user)                   # clean separation ✅
```

---

## 🔐 The finally Clause

> `finally` runs **ALWAYS** — whether exception occurred or not.
> Perfect for **cleanup** — close files, release connections, free resources.

```python
# Syntax:
try:
    risky_code()
except SomeError:
    handle_error()
finally:
    # ALWAYS runs — with exception OR without!
    cleanup_code()
```

```python
# ─── Always runs — proof ───
def demo(x):
    try:
        result = 10 / x
        print(f"  Result: {result}")
    except ZeroDivisionError:
        print("  ❌ Division by zero!")
    finally:
        print("  🔐 finally ALWAYS runs!\n")

demo(2)   # Result: 5.0 → finally runs
demo(0)   # Error!      → finally runs
```

```python
# ─── Real use: always close database connection ───
connection = None
try:
    connection = open_database()
    data       = connection.query("SELECT * FROM users")
    process(data)
except DatabaseError as e:
    print(f"  ❌ Database error: {e}")
finally:
    if connection:
        connection.close()    # ALWAYS close — no memory leaks!
        print("  🔐 Connection closed.")
```

```python
# ─── finally with return — tricky! ───
def tricky():
    try:
        return "from try"
    finally:
        return "from finally"   # ← this OVERRIDES the try return!

print(tricky())   # "from finally"  ← surprising!

# ─── finally runs even with return ───
def test():
    try:
        print("In try")
        return 42
    finally:
        print("In finally")   # runs BEFORE the return!

result = test()
# In try
# In finally
print(result)   # 42
```

---

## 🎭 The Full try-except-else-finally

> All four clauses together — the complete exception handling toolkit!

```python
# Full syntax:
try:
    # 1️⃣ Attempt the risky operation
    risky_code()

except SpecificError as e:
    # 2️⃣ Handle specific expected error
    handle_specific(e)

except AnotherError as e:
    # 3️⃣ Handle another expected error
    handle_another(e)

except Exception as e:
    # 4️⃣ Catch-all for unexpected errors
    handle_unexpected(e)

else:
    # 5️⃣ Runs ONLY if try succeeded (no exception)
    success_code()

finally:
    # 6️⃣ ALWAYS runs — cleanup here
    cleanup_code()
```

```python
# ─── Real example: safe file processor ───
def process_file(filename):
    """Read, process, and report on a file safely."""
    file_handle = None

    try:
        print(f"  📂 Opening {filename}...")
        file_handle = open(filename, "r", encoding="utf-8")
        content = file_handle.read()

        if not content.strip():
            raise ValueError("File is empty!")

        word_count = len(content.split())
        print(f"  📊 Processing {word_count} words...")

    except FileNotFoundError:
        print(f"  ❌ File '{filename}' doesn't exist!")
        return None

    except PermissionError:
        print(f"  🔒 No permission to read '{filename}'!")
        return None

    except ValueError as e:
        print(f"  ⚠️  Content problem: {e}")
        return None

    except Exception as e:
        print(f"  💥 Unexpected error: {type(e).__name__}: {e}")
        return None

    else:
        # Only runs if ALL of try succeeded
        print(f"  ✅ File processed successfully!")
        return {
            "words":   word_count,
            "chars":   len(content),
            "lines":   content.count("\n") + 1,
        }

    finally:
        # Always runs — close file if it was opened
        if file_handle and not file_handle.closed:
            file_handle.close()
            print(f"  🔐 File handle closed.")


result = process_file("data.txt")
if result:
    print(f"\n  📈 Stats: {result}")
```

---

## 🔍 Exception Object — as e

> Catching the exception AS a variable gives you details about what went wrong!

```python
# Syntax:
try:
    risky()
except SomeException as e:
    print(e)           # the error message
    print(type(e))     # the exception class
    print(repr(e))     # detailed representation
```

```python
# ─── Exploring the exception object ───
try:
    result = int("not_a_number")
except ValueError as e:
    print(f"Message : {e}")
    print(f"Type    : {type(e)}")
    print(f"Type name: {type(e).__name__}")
    print(f"Args    : {e.args}")
    print(f"Repr    : {repr(e)}")

# Message : invalid literal for int() with base 10: 'not_a_number'
# Type    : <class 'ValueError'>
# Type name: ValueError
# Args    : ("invalid literal for int() with base 10: 'not_a_number'",)
# Repr    : ValueError("invalid literal for int() with base 10: 'not_a_number'")
```

```python
# ─── Using exception info for better error messages ───
def safe_convert(value, to_type):
    try:
        return to_type(value)
    except (ValueError, TypeError) as e:
        print(f"  ❌ Cannot convert {value!r} to {to_type.__name__}: {e}")
        return None

safe_convert("abc", int)        # ❌ Cannot convert 'abc' to int: ...
safe_convert([1,2,3], float)    # ❌ Cannot convert [1,2,3] to float: ...
safe_convert("3.14", float)     # ✅ 3.14
```

```python
# ─── Full exception info with traceback ───
import traceback

def risky_operation():
    data  = {"key": "value"}
    return data["missing_key"]

try:
    risky_operation()
except KeyError as e:
    print(f"  Error type   : {type(e).__name__}")
    print(f"  Error message: {e}")
    print(f"  Full traceback:")
    traceback.print_exc()          # print to stderr
    tb_str = traceback.format_exc()  # get as string
    print(tb_str)
```

```python
# ─── Inspecting exception attributes ───
try:
    with open("ghost.txt") as f: pass
except OSError as e:
    print(f"  errno    : {e.errno}")       # OS error number
    print(f"  strerror : {e.strerror}")    # human readable message
    print(f"  filename : {e.filename}")    # which file

# errno    : 2
# strerror : No such file or directory
# filename : ghost.txt
```

---

## 🚀 Raising Exceptions — raise

> Sometimes YOU need to signal that something went wrong.
> Use `raise` to throw exceptions intentionally!

```python
# Syntax:
raise ExceptionType("error message")
raise ExceptionType("message") from original_exception
raise   # re-raise the current exception (inside except block)
```

```python
# ─── Basic raise ───
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"  ❌ {e}")   # ❌ Cannot divide by zero!
```

```python
# ─── Validate inputs with raise ───
def create_user(name, age, email):
    """Create a user with full validation."""

    # Validate name
    if not name or not isinstance(name, str):
        raise TypeError("Name must be a non-empty string")
    if len(name.strip()) < 2:
        raise ValueError(f"Name too short: '{name}' (min 2 chars)")

    # Validate age
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if not (0 < age < 150):
        raise ValueError(f"Age {age} is out of valid range (1-149)")

    # Validate email
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError(f"Invalid email address: {email!r}")

    return {"name": name.strip(), "age": age, "email": email}

# Test validations:
tests = [
    ("", 25, "a@b.com"),
    ("Alice", -5, "a@b.com"),
    ("Bob", 30, "not-an-email"),
    ("Charlie", 22, "charlie@example.com"),  # ✅
]

for name, age, email in tests:
    try:
        user = create_user(name, age, email)
        print(f"  ✅ Created: {user}")
    except (ValueError, TypeError) as e:
        print(f"  ❌ {type(e).__name__}: {e}")
```

```python
# ─── raise inside except (conditional re-raise) ───
def safe_parse(text):
    try:
        value = int(text)
        if value < 0:
            raise ValueError(f"Value must be positive, got {value}")
        return value
    except ValueError as e:
        if "invalid literal" in str(e):
            # It's not a number at all
            raise ValueError(f"'{text}' is not a number") from None
        raise   # re-raise: it IS a number but negative — let it propagate
```

---

## 🔁 Re-raising Exceptions

```python
# ─── Bare raise — re-raise the current exception ───
def process(data):
    try:
        result = complex_operation(data)
    except ValueError as e:
        print(f"  📋 Logging error: {e}")   # log it
        raise                               # re-raise unchanged

# ─── Re-raise as different type ───
def load_config(path):
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError:
        raise RuntimeError(f"Config file missing: {path}")
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Config file corrupt: {e}")
```

---

## 🔗 Exception Chaining — from

> When you raise an exception because of another, use `from` to
> **link them** — preserves the original cause for debugging!

```python
# Syntax:
raise NewException("message") from original_exception
raise NewException("message") from None   # suppress original
```

```python
# ─── Exception chaining ───
def connect_database(host, port):
    try:
        import socket
        sock = socket.create_connection((host, port), timeout=2)
    except ConnectionRefusedError as e:
        raise RuntimeError(
            f"Cannot connect to database at {host}:{port}"
        ) from e    # ← chain: original cause preserved!

try:
    connect_database("localhost", 5432)
except RuntimeError as e:
    print(f"  ❌ {e}")
    print(f"  Caused by: {e.__cause__}")   # shows original error!
```

```python
# ─── from None — suppress the chain ───
def get_config_value(key):
    config = {"host": "localhost", "port": "8080"}
    try:
        return config[key]
    except KeyError:
        # The KeyError is an implementation detail — hide it!
        raise ValueError(f"Unknown config key: {key!r}") from None

try:
    get_config_value("timeout")
except ValueError as e:
    print(f"  ❌ {e}")
    # No messy "During handling of the above exception..." message!
```

```python
# ─── Inspecting the chain ───
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("Bad calculation") from e
except ValueError as e:
    print(f"  Exception     : {e}")
    print(f"  Cause (__cause__): {e.__cause__}")
    print(f"  Context(__context__): {e.__context__}")
```

---

## 🌳 Built-in Exceptions — Complete Hierarchy

```
BaseException                          ← catches EVERYTHING (even Ctrl+C)
├── SystemExit                         ← sys.exit() called
├── KeyboardInterrupt                  ← Ctrl+C pressed
├── GeneratorExit                      ← generator closed
└── Exception                         ← almost everything else
    ├── StopIteration                  ← iterator exhausted
    ├── StopAsyncIteration             ← async iterator done
    ├── ArithmeticError
    │   ├── ZeroDivisionError          ← x / 0
    │   ├── FloatingPointError         ← float operation failed
    │   └── OverflowError              ← number too large
    ├── LookupError
    │   ├── IndexError                 ← list[99] out of range
    │   └── KeyError                   ← dict["missing"]
    ├── TypeError                      ← wrong type: "a" + 1
    ├── ValueError                     ← right type, wrong value: int("abc")
    ├── NameError                      ← undefined variable
    │   └── UnboundLocalError          ← local var used before assigned
    ├── AttributeError                 ← obj.missing_attr
    ├── ImportError                    ← import failed
    │   └── ModuleNotFoundError        ← module doesn't exist
    ├── OSError (= IOError = EnvironmentError)
    │   ├── FileNotFoundError          ← file doesn't exist
    │   ├── PermissionError            ← access denied
    │   ├── FileExistsError            ← file already exists
    │   ├── IsADirectoryError          ← expected file, got dir
    │   ├── NotADirectoryError         ← expected dir, got file
    │   ├── InterruptedError           ← system call interrupted
    │   └── TimeoutError               ← operation timed out
    ├── RuntimeError                   ← general runtime error
    │   ├── RecursionError             ← max recursion exceeded
    │   └── NotImplementedError        ← abstract method not implemented
    ├── MemoryError                    ← out of memory
    ├── SyntaxError                    ← invalid Python syntax
    │   └── IndentationError           ← bad indentation
    ├── UnicodeError
    │   ├── UnicodeDecodeError         ← decode failed
    │   ├── UnicodeEncodeError         ← encode failed
    │   └── UnicodeTranslateError      ← translate failed
    └── Warning
        ├── DeprecationWarning
        ├── UserWarning
        ├── FutureWarning
        └── RuntimeWarning
```

```python
# ─── Hierarchy in practice — catching parent catches children ───
try:
    items = [1, 2, 3]
    print(items[10])
except LookupError:             # catches BOTH IndexError AND KeyError
    print("Lookup failed!")

try:
    with open("x.txt") as f: pass
except OSError:                 # catches FileNotFoundError, PermissionError, etc.
    print("OS error!")

# ─── Catching Exception vs BaseException ───
try:
    pass
except Exception:
    # catches almost everything EXCEPT:
    # KeyboardInterrupt, SystemExit, GeneratorExit
    pass

try:
    pass
except BaseException:
    # catches EVERYTHING including Ctrl+C and sys.exit()!
    # Almost never do this
    pass
```

---

## 🎨 Custom Exceptions

> Create your own exceptions to describe **domain-specific** problems.
> This makes errors much more meaningful and easier to handle!

```python
# ─── Simplest custom exception ───
class MyError(Exception):
    """A simple custom exception."""
    pass

raise MyError("Something went wrong!")
```

```python
# ─── Custom exception with message ───
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class DatabaseError(Exception):
    """Raised for database-related failures."""
    pass

class NetworkError(Exception):
    """Raised for network-related failures."""
    pass

# Use them:
def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError(f"Age must be int, got {type(age).__name__}")
    if not (0 < age < 150):
        raise ValidationError(f"Age {age} out of range (1-149)")
    return age
```

```python
# ─── Rich custom exception with extra attributes ───
class InsufficientFundsError(Exception):
    """
    Raised when a withdrawal exceeds account balance.

    Attributes:
        account_id (str): The account ID.
        balance    (float): Current balance.
        amount     (float): Requested withdrawal amount.
        shortfall  (float): How much is missing.
    """
    def __init__(self, account_id, balance, amount):
        self.account_id = account_id
        self.balance    = balance
        self.amount     = amount
        self.shortfall  = amount - balance
        super().__init__(
            f"Account {account_id}: Cannot withdraw ₹{amount:,.2f}. "
            f"Balance: ₹{balance:,.2f}. "
            f"Shortfall: ₹{self.shortfall:,.2f}"
        )

# Use it:
try:
    raise InsufficientFundsError("ACC001", 5000.00, 8000.00)
except InsufficientFundsError as e:
    print(f"  ❌ {e}")
    print(f"  Account  : {e.account_id}")
    print(f"  Shortfall: ₹{e.shortfall:,.2f}")
```

```python
# ─── Exception hierarchy for a project ───

# Base exception for the whole app
class AppError(Exception):
    """Base exception for MyApp."""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code    = code
        self.message = message

    def __str__(self):
        if self.code:
            return f"[{self.code}] {self.message}"
        return self.message


# Domain-specific exceptions
class UserError(AppError):
    """User-related errors."""
    pass

class UserNotFoundError(UserError):
    """User does not exist."""
    def __init__(self, user_id):
        super().__init__(
            f"User with ID {user_id!r} not found",
            code="USR_001"
        )
        self.user_id = user_id

class UserPermissionError(UserError):
    """User lacks required permission."""
    def __init__(self, user_id, required_role):
        super().__init__(
            f"User {user_id!r} lacks permission: requires '{required_role}'",
            code="USR_002"
        )
        self.user_id      = user_id
        self.required_role = required_role


class DataError(AppError):
    """Data-related errors."""
    pass

class ValidationError(DataError):
    """Data validation failed."""
    def __init__(self, field, value, reason):
        super().__init__(
            f"Validation failed for '{field}' = {value!r}: {reason}",
            code="DAT_001"
        )
        self.field  = field
        self.value  = value
        self.reason = reason

class DuplicateError(DataError):
    """Duplicate record found."""
    def __init__(self, entity, key, value):
        super().__init__(
            f"Duplicate {entity}: {key}={value!r} already exists",
            code="DAT_002"
        )


# Usage:
def get_user(user_id, requesting_user_role):
    users = {1: {"name": "Alice", "role": "admin"}}

    if user_id not in users:
        raise UserNotFoundError(user_id)

    if requesting_user_role != "admin":
        raise UserPermissionError(requesting_user_role, "admin")

    return users[user_id]

for uid, role in [(1, "admin"), (99, "admin"), (1, "viewer")]:
    try:
        user = get_user(uid, role)
        print(f"  ✅ Got user: {user}")
    except UserNotFoundError as e:
        print(f"  ❌ Not found: {e}")
    except UserPermissionError as e:
        print(f"  🔒 Permission: {e}")
    except AppError as e:
        print(f"  ⚠️  App error [{e.code}]: {e}")
```

---

## 🔄 Context Managers & Exceptions

```python
# ─── with statement handles exceptions automatically ───
# The __exit__ method receives exception info

class ManagedResource:
    def __enter__(self):
        print("  🔓 Resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  🔐 Resource released")
        if exc_type is not None:
            print(f"  ⚠️  Exception occurred: {exc_type.__name__}: {exc_val}")
        # Return True to SUPPRESS the exception
        # Return False (or None) to let it PROPAGATE
        return False   # don't suppress

with ManagedResource() as r:
    print("  📋 Doing work...")
    raise ValueError("Something went wrong")
# 🔓 Resource acquired
# 📋 Doing work...
# 🔐 Resource released
# ⚠️  Exception occurred: ValueError: Something went wrong
# ValueError: Something went wrong  ← propagated because we returned False
```

```python
# ─── contextlib.suppress — suppress specific exceptions ───
from contextlib import suppress

# Instead of:
try:
    import ujson as json
except ImportError:
    import json

# Use:
with suppress(ImportError):
    import ujson as json   # silently skip if not installed

# Delete file if it exists, silently:
import os
with suppress(FileNotFoundError):
    os.remove("temp.txt")   # no error if file doesn't exist ✅
```

```python
# ─── contextlib.contextmanager with exception handling ───
from contextlib import contextmanager

@contextmanager
def transaction(db):
    """Database transaction context manager."""
    db.begin()
    try:
        yield db
        db.commit()
        print("  ✅ Transaction committed")
    except Exception as e:
        db.rollback()
        print(f"  ❌ Transaction rolled back: {e}")
        raise   # re-raise after rollback

# with transaction(db) as conn:
#     conn.execute("INSERT INTO users VALUES ...")
#     conn.execute("UPDATE accounts SET balance = ...")
# If anything fails → rollback, then exception propagates
```

---

## ⚠️ Warnings

> Warnings are for **"this might be a problem"** — not crashes.

```python
import warnings

# ─── Issue a warning ───
warnings.warn("This feature is deprecated!", DeprecationWarning)
warnings.warn("Low memory!", ResourceWarning)
warnings.warn("Check your data!", UserWarning)

# ─── Warning categories ───
warnings.warn("Old function", DeprecationWarning,  stacklevel=2)
warnings.warn("Future change", FutureWarning)
warnings.warn("Slow operation", RuntimeWarning)

# ─── Filter warnings ───
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("error",  category=UserWarning)  # turn into exceptions!
warnings.filterwarnings("once")   # show each warning only once
warnings.resetwarnings()          # reset all filters

# ─── Catch warnings as exceptions ───
with warnings.catch_warnings():
    warnings.simplefilter("error")
    try:
        warnings.warn("Watch out!", UserWarning)
    except UserWarning as e:
        print(f"  ⚠️  Caught warning: {e}")
```

```python
# ─── Custom warning class ───
class PerformanceWarning(UserWarning):
    """Warn about potentially slow operations."""
    pass

def slow_function(n):
    if n > 1000:
        warnings.warn(
            f"Processing {n} items may be slow. Consider batching.",
            PerformanceWarning,
            stacklevel=2
        )
    return list(range(n))

slow_function(5000)   # ⚠️ PerformanceWarning: Processing 5000 items may be slow...
```

---

## 📋 Logging Exceptions

> In production, you want to **log** exceptions — not just print them!

```python
import logging
import traceback

# ─── Set up logging ───
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
```

```python
# ─── Log exceptions ───
def process_payment(amount, card_number):
    try:
        if amount <= 0:
            raise ValueError(f"Invalid amount: {amount}")
        logger.info(f"Processing payment of ₹{amount}")
        # ... payment processing ...
        logger.info("Payment successful")
        return True

    except ValueError as e:
        logger.warning(f"Invalid payment data: {e}")
        return False

    except Exception as e:
        logger.error(f"Payment failed: {e}", exc_info=True)
        # exc_info=True → logs the full traceback!
        return False
```

```python
# ─── logger.exception() — logs error + full traceback ───
def risky_operation():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        logger.exception("Zero division in risky_operation")
        # logs: ERROR — Zero division in risky_operation
        #       Traceback (most recent call last):
        #         File "...", line ..., in risky_operation
        #       ZeroDivisionError: division by zero
```

```python
# ─── Structured exception logging ───
import json
from datetime import datetime

def log_exception(exc, context=None):
    """Log exception with structured metadata."""
    error_data = {
        "timestamp"     : datetime.now().isoformat(),
        "exception_type": type(exc).__name__,
        "message"       : str(exc),
        "traceback"     : traceback.format_exc(),
        "context"       : context or {},
    }
    logger.error(json.dumps(error_data, indent=2))

try:
    result = int("abc")
except ValueError as e:
    log_exception(e, context={"input": "abc", "function": "process_input"})
```

---

## 🏗️ Exception Handling Patterns

---

### Pattern 1 — EAFP vs LBYL

```python
# LBYL — Look Before You Leap (check first, then do)
# Common in Java/C — NOT the Python way

def lbyl_divide(a, b):
    if b != 0:                    # CHECK
        return a / b              # then DO
    return None

def lbyl_get_key(d, key):
    if key in d:                  # CHECK
        return d[key]             # then DO
    return None

# EAFP — Easier to Ask Forgiveness than Permission (Python style! ⭐)
# Just try it, handle failure if it happens

def eafp_divide(a, b):
    try:
        return a / b              # just DO it
    except ZeroDivisionError:
        return None               # handle failure

def eafp_get_key(d, key):
    try:
        return d[key]             # just DO it
    except KeyError:
        return None               # handle failure

# EAFP is more Pythonic and often faster when success is common!
```

---

### Pattern 2 — Guard Clauses

```python
# Validate inputs early, fail fast — no deep nesting!

# ❌ Deep nesting (hard to read)
def process_order(order):
    if order:
        if order.get("items"):
            if len(order["items"]) > 0:
                if order.get("user_id"):
                    # actual logic starts here...
                    pass

# ✅ Guard clauses (flat, readable)
def process_order(order):
    if not order:
        raise ValueError("Order cannot be empty")
    if not order.get("items"):
        raise ValueError("Order must have items")
    if len(order["items"]) == 0:
        raise ValueError("Order items list is empty")
    if not order.get("user_id"):
        raise ValueError("Order must have a user_id")

    # actual logic — no nesting! clean and clear
    return fulfill_order(order)
```

---

### Pattern 3 — Default Value on Error

```python
# Return a sensible default when an operation fails

def safe_int(value, default=0):
    """Convert to int, return default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_get(dictionary, key, default=None):
    """Get dict value, return default if missing."""
    try:
        return dictionary[key]
    except (KeyError, TypeError):
        return default

def safe_read_file(path, default=""):
    """Read file, return default if it fails."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (OSError, IOError):
        return default

# Usage:
print(safe_int("42"))        # 42
print(safe_int("abc"))       # 0
print(safe_int("abc", -1))   # -1
print(safe_int(None))        # 0
```

---

### Pattern 4 — Retry on Failure

```python
import time
import functools

def retry(max_attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,)):
    """
    Decorator to retry a function on failure.

    Args:
        max_attempts (int):   Maximum number of attempts.
        delay        (float): Initial delay between retries (seconds).
        backoff      (float): Multiplier for delay after each attempt.
        exceptions   (tuple): Exception types to catch and retry on.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    last_exception = e
                    if attempt == max_attempts:
                        print(f"  ❌ All {max_attempts} attempts failed!")
                        raise

                    print(f"  ⚠️  Attempt {attempt}/{max_attempts} failed: {e}")
                    print(f"     Retrying in {current_delay:.1f}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper
    return decorator

import random

@retry(max_attempts=3, delay=0.1, exceptions=(ConnectionError, TimeoutError))
def fetch_data(url):
    """Simulate a flaky network request."""
    if random.random() < 0.7:
        raise ConnectionError(f"Connection failed for {url}")
    return {"data": "success", "url": url}

try:
    result = fetch_data("https://api.example.com/data")
    print(f"  ✅ Got: {result}")
except ConnectionError:
    print("  ❌ Could not fetch data after all retries")
```

---

### Pattern 5 — Exception Groups (Python 3.11+)

```python
# Handle multiple unrelated exceptions at once!

# Raise multiple exceptions simultaneously:
try:
    raise ExceptionGroup("multiple errors", [
        ValueError("bad value"),
        TypeError("wrong type"),
        KeyError("missing key"),
    ])
except* ValueError as eg:
    print(f"  ValueError(s): {eg.exceptions}")
except* TypeError as eg:
    print(f"  TypeError(s):  {eg.exceptions}")
except* KeyError as eg:
    print(f"  KeyError(s):   {eg.exceptions}")
```

---

### Pattern 6 — Null Object Pattern

```python
# Return a "safe" null object instead of None to avoid AttributeErrors

class NullUser:
    """A null object that safely handles any attribute access."""
    name     = ""
    email    = ""
    is_valid = False

    def save(self): return False
    def delete(self): return False
    def __bool__(self): return False
    def __repr__(self): return "NullUser()"

def find_user(user_id):
    users = {1: {"name": "Alice", "email": "alice@example.com", "is_valid": True}}
    return users.get(user_id, NullUser())

user = find_user(99)
if user:
    print(user.name)   # works without try/except!
else:
    print("  No user found")
```

---

### Pattern 7 — Result Type Pattern

```python
# Wrap success/failure in an object — no exceptions needed!

class Result:
    """Represents either a success or failure."""

    def __init__(self, value=None, error=None):
        self._value = value
        self._error = error
        self.ok     = error is None

    @classmethod
    def success(cls, value):
        return cls(value=value)

    @classmethod
    def failure(cls, error):
        return cls(error=error)

    @property
    def value(self):
        if not self.ok:
            raise RuntimeError(f"Cannot get value from failure: {self._error}")
        return self._value

    @property
    def error(self):
        return self._error

    def __repr__(self):
        if self.ok:
            return f"Result.success({self._value!r})"
        return f"Result.failure({self._error!r})"


def safe_divide(a, b):
    if b == 0:
        return Result.failure("Division by zero")
    return Result.success(a / b)

# Usage — no try/except needed at call site!
for a, b in [(10, 2), (10, 0), (9, 3)]:
    result = safe_divide(a, b)
    if result.ok:
        print(f"  ✅ {a}/{b} = {result.value}")
    else:
        print(f"  ❌ {a}/{b} — {result.error}")
```

---

---

## 🌍 Real-World Projects

---

### Project 1 — Robust API Client

```python
import json
import time
import logging
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

logger = logging.getLogger(__name__)

class APIError(Exception):
    """Base API exception."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response    = response

class APINotFoundError(APIError):
    """Resource not found (404)."""
    pass

class APIAuthError(APIError):
    """Authentication failed (401/403)."""
    pass

class APIRateLimitError(APIError):
    """Rate limit exceeded (429)."""
    def __init__(self, retry_after=60):
        super().__init__(f"Rate limit exceeded. Retry after {retry_after}s", 429)
        self.retry_after = retry_after

class APIClient:
    """Robust API client with retry, error handling, and logging."""

    def __init__(self, base_url, api_key=None, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.api_key  = api_key
        self.timeout  = timeout

    def get(self, endpoint, retries=3):
        """Make a GET request with automatic retry on transient errors."""
        url     = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        last_error = None

        for attempt in range(1, retries + 1):
            try:
                logger.debug(f"GET {url} (attempt {attempt}/{retries})")
                req      = Request(url, headers=headers)
                response = urlopen(req, timeout=self.timeout)
                data     = json.loads(response.read().decode())
                logger.info(f"GET {url} → 200 OK")
                return data

            except HTTPError as e:
                if e.code == 404:
                    raise APINotFoundError(
                        f"Resource not found: {endpoint}", 404
                    ) from e
                elif e.code in (401, 403):
                    raise APIAuthError(
                        f"Authentication failed: {e.reason}", e.code
                    ) from e
                elif e.code == 429:
                    retry_after = int(e.headers.get("Retry-After", 60))
                    raise APIRateLimitError(retry_after) from e
                elif e.code >= 500 and attempt < retries:
                    logger.warning(f"Server error {e.code}, retry {attempt}/{retries}")
                    time.sleep(2 ** attempt)   # exponential backoff
                    last_error = e
                    continue
                else:
                    raise APIError(f"HTTP {e.code}: {e.reason}", e.code) from e

            except URLError as e:
                if attempt < retries:
                    logger.warning(f"Network error, retry {attempt}/{retries}: {e}")
                    time.sleep(1 * attempt)
                    last_error = e
                    continue
                raise APIError(f"Network error: {e.reason}") from e

            except json.JSONDecodeError as e:
                raise APIError(f"Invalid JSON response: {e}") from e

            except Exception as e:
                logger.error(f"Unexpected error: {e}", exc_info=True)
                raise APIError(f"Unexpected error: {e}") from e

        raise APIError(f"All {retries} attempts failed") from last_error
```

---

### Project 2 — Form Validator with Custom Exceptions

```python
import re
from dataclasses import dataclass, field
from typing import List, Optional

# ─── Custom exception hierarchy ───
class FormError(Exception):
    """Base form validation error."""
    pass

class FieldError(FormError):
    """Error for a specific field."""
    def __init__(self, field_name, message):
        super().__init__(f"Field '{field_name}': {message}")
        self.field_name = field_name
        self.message    = message

class MultiFieldError(FormError):
    """Multiple validation errors at once."""
    def __init__(self, errors: List[FieldError]):
        messages = "\n".join(f"  • {e}" for e in errors)
        super().__init__(f"Validation failed:\n{messages}")
        self.errors = errors

    def get_field_errors(self, field_name):
        return [e for e in self.errors if e.field_name == field_name]


# ─── Validators ───
def validate_required(field, value):
    if not value or (isinstance(value, str) and not value.strip()):
        raise FieldError(field, "This field is required")

def validate_min_length(field, value, min_len):
    if len(str(value)) < min_len:
        raise FieldError(field, f"Minimum length is {min_len} characters")

def validate_max_length(field, value, max_len):
    if len(str(value)) > max_len:
        raise FieldError(field, f"Maximum length is {max_len} characters")

def validate_email(field, value):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(pattern, value):
        raise FieldError(field, f"'{value}' is not a valid email address")

def validate_range(field, value, min_val, max_val):
    if not (min_val <= value <= max_val):
        raise FieldError(field, f"Must be between {min_val} and {max_val}")


# ─── Registration form validator ───
def validate_registration(data):
    """Validate all fields — collect ALL errors before reporting."""
    errors = []

    # Name
    try:
        validate_required("name", data.get("name"))
        validate_min_length("name", data.get("name",""), 2)
        validate_max_length("name", data.get("name",""), 50)
    except FieldError as e:
        errors.append(e)

    # Email
    try:
        validate_required("email", data.get("email"))
        validate_email("email", data.get("email",""))
    except FieldError as e:
        errors.append(e)

    # Age
    try:
        validate_required("age", data.get("age"))
        age = int(data.get("age", 0))
        validate_range("age", age, 18, 120)
    except (FieldError, ValueError) as e:
        if isinstance(e, ValueError):
            errors.append(FieldError("age", "Must be a valid number"))
        else:
            errors.append(e)

    # Password
    try:
        validate_required("password", data.get("password"))
        validate_min_length("password", data.get("password",""), 8)
        pwd = data.get("password","")
        if not any(c.isupper() for c in pwd):
            raise FieldError("password", "Must contain at least one uppercase letter")
        if not any(c.isdigit() for c in pwd):
            raise FieldError("password", "Must contain at least one number")
    except FieldError as e:
        errors.append(e)

    if errors:
        raise MultiFieldError(errors)

    return True


# ─── Test it ───
test_cases = [
    {
        "name":     "A",
        "email":    "not-an-email",
        "age":      "15",
        "password": "weak",
    },
    {
        "name":     "Alice Smith",
        "email":    "alice@example.com",
        "age":      "25",
        "password": "Secure123!",
    },
]

for i, data in enumerate(test_cases, 1):
    print(f"\n  Test {i}: {data['name']}")
    print(f"  {'─'*40}")
    try:
        validate_registration(data)
        print(f"  ✅ Registration valid!")
    except MultiFieldError as e:
        print(f"  ❌ {len(e.errors)} validation error(s):")
        for err in e.errors:
            print(f"     • {err.field_name}: {err.message}")
    except FormError as e:
        print(f"  ❌ Form error: {e}")
```

---

### Project 3 — Exception-Safe Data Pipeline

```python
import csv, json, os
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

@dataclass
class PipelineError:
    """Represents a non-fatal error during pipeline processing."""
    row_num : int
    field   : str
    value   : Any
    message : str
    exception: Exception

@dataclass
class PipelineResult:
    """Result of running the pipeline."""
    processed : List[Dict] = field(default_factory=list)
    failed    : List[PipelineError] = field(default_factory=list)
    skipped   : int = 0

    @property
    def success_rate(self):
        total = len(self.processed) + len(self.failed)
        return (len(self.processed) / total * 100) if total > 0 else 0

def parse_row(row: Dict, row_num: int, errors: List) -> Optional[Dict]:
    """Parse and validate a CSV row, collecting errors."""
    result = {}

    # Parse name
    try:
        name = row["name"].strip()
        if not name:
            raise ValueError("Name is empty")
        result["name"] = name.title()
    except (KeyError, ValueError) as e:
        errors.append(PipelineError(row_num, "name", row.get("name"), str(e), e))
        return None

    # Parse age
    try:
        age = int(row["age"])
        if not (0 < age < 150):
            raise ValueError(f"Age {age} out of range")
        result["age"] = age
    except (KeyError, ValueError) as e:
        errors.append(PipelineError(row_num, "age", row.get("age"), str(e), e))

    # Parse score (non-fatal — default to 0)
    try:
        result["score"] = float(row.get("score", 0))
    except ValueError:
        result["score"] = 0.0
        errors.append(PipelineError(
            row_num, "score", row.get("score"),
            "Invalid score, defaulting to 0", ValueError()
        ))

    return result


def run_pipeline(input_csv: str, output_json: str) -> PipelineResult:
    """
    Process CSV → validate → transform → save as JSON.
    Collects ALL errors without stopping.
    """
    result = PipelineResult()

    # 1. Read CSV
    try:
        with open(input_csv, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows   = list(reader)
    except FileNotFoundError:
        raise RuntimeError(f"Input file not found: {input_csv}")
    except csv.Error as e:
        raise RuntimeError(f"CSV parse error: {e}")

    print(f"\n  📂 Processing {len(rows)} rows from {input_csv}")

    # 2. Process each row
    for row_num, row in enumerate(rows, start=1):
        parsed = parse_row(row, row_num, result.failed)

        if parsed is None:
            result.skipped += 1
            continue

        # Transform
        parsed["grade"] = (
            "A" if parsed["score"] >= 90 else
            "B" if parsed["score"] >= 80 else
            "C" if parsed["score"] >= 70 else
            "F"
        )
        result.processed.append(parsed)

    # 3. Save output
    try:
        Path(output_json).parent.mkdir(parents=True, exist_ok=True)
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(result.processed, f, indent=2)
    except OSError as e:
        raise RuntimeError(f"Cannot write output: {e}")

    # 4. Report
    print(f"  ✅ Processed : {len(result.processed)}")
    print(f"  ❌ Failed    : {len(result.failed)}")
    print(f"  ⏭️  Skipped   : {result.skipped}")
    print(f"  📊 Success   : {result.success_rate:.1f}%")

    if result.failed:
        print(f"\n  ⚠️  Errors:")
        for err in result.failed:
            print(f"     Row {err.row_num:3}: [{err.field}] {err.message}")

    return result
```

---

## 🚨 Common Mistakes

### 1. Catching Exception Too Broadly

```python
# ❌ Hides ALL bugs — even ones you didn't expect!
try:
    result = complex_operation()
except Exception:
    print("Something went wrong")   # which thing?? 🤷

# ✅ Catch specifically what you expect
try:
    result = complex_operation()
except ValueError as e:
    print(f"Bad value: {e}")
except ConnectionError as e:
    print(f"Network issue: {e}")
# Let other exceptions propagate — they're bugs!
```

### 2. Silent Exception — swallowing errors

```python
# ❌ Swallowing exceptions — bugs disappear silently!
try:
    important_operation()
except Exception:
    pass    # 😱 error completely hidden!

# ✅ At minimum, log it!
try:
    important_operation()
except Exception as e:
    logger.exception(f"Operation failed: {e}")
    # or: raise, or: return default, but NEVER silent pass!
```

### 3. Using Exceptions for Flow Control

```python
# ❌ Slow and unreadable
def find_item(lst, target):
    try:
        return lst.index(target)
    except ValueError:
        return -1   # using exception as "not found" check

# ✅ Check first
def find_item(lst, target):
    if target in lst:
        return lst.index(target)
    return -1

# ✅ Or even cleaner
def find_item(lst, target):
    try:
        return lst.index(target)
    except ValueError:
        return -1   # OK here — truly exceptional case
```

### 4. Catching in Wrong Order (Broad Before Specific)

```python
# ❌ FileNotFoundError never caught — OSError catches first!
try:
    open("x.txt")
except OSError:              # too broad — catches FileNotFoundError!
    print("OS error")
except FileNotFoundError:    # never reached!
    print("Not found")

# ✅ Specific FIRST, broad LAST
try:
    open("x.txt")
except FileNotFoundError:    # specific first ✅
    print("Not found")
except OSError:              # broad last
    print("Other OS error")
```

### 5. Forgetting to Re-raise

```python
# ❌ Error logged but silently swallowed
def process():
    try:
        risky()
    except Exception as e:
        logger.error(f"Error: {e}")
        # forgot to raise! caller thinks everything is fine 😱

# ✅ Log AND re-raise
def process():
    try:
        risky()
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        raise   # let it propagate ✅
```

### 6. Modifying Loop Variable in except

```python
# ❌ Continues with bad state
items = [1, 0, 3, 0, 5]
total = 0
for item in items:
    try:
        total += 100 / item
    except ZeroDivisionError:
        item = 1    # ❌ modifying loop var does nothing!

# ✅ Skip the bad item
total = 0
for item in items:
    try:
        total += 100 / item
    except ZeroDivisionError:
        continue    # ✅ skip this iteration
```

---

## 📝 Cheat Sheet

```python
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏗️  BASIC STRUCTURE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

try:
    risky()                    # attempt
except SpecificError as e:     # handle known error
    handle(e)
except (ErrA, ErrB) as e:     # handle multiple
    handle(e)
except Exception as e:         # catch-all (last resort)
    log(e); raise
else:
    success()                  # runs ONLY if no exception
finally:
    cleanup()                  # ALWAYS runs

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀  RAISING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

raise ValueError("bad value")
raise TypeError("wrong type") from original
raise ValueError("msg") from None  # suppress chain
raise                               # re-raise current

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨  CUSTOM EXCEPTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class MyError(Exception):
    """Base app error."""
    pass

class SpecificError(MyError):
    def __init__(self, msg, code=None):
        super().__init__(msg)
        self.code = code

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔧  USEFUL BUILT-INS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Most common exceptions:
ValueError          # wrong value: int("abc")
TypeError           # wrong type:  "a" + 1
KeyError            # dict["missing"]
IndexError          # list[99]
AttributeError      # obj.missing
FileNotFoundError   # open("ghost.txt")
PermissionError     # access denied
ZeroDivisionError   # 1 / 0
NameError           # undefined variable
ImportError         # failed import
RuntimeError        # general runtime error
NotImplementedError # abstract method
RecursionError      # too deep
OverflowError       # number too large
StopIteration       # iterator exhausted

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔇  SUPPRESS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("temp.txt")     # silently skip if not found

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📋  TRACEBACK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import traceback
traceback.print_exc()          # print to stderr
s = traceback.format_exc()     # get as string

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊  EXCEPTION ATTRIBUTES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

except Exception as e:
    str(e)             # message
    type(e).__name__   # class name
    e.args             # tuple of args
    e.__cause__        # exception it was raised from
    e.__context__      # exception during whose handling

# OSError extras:
    e.errno            # error number
    e.strerror         # human message
    e.filename         # which file
```

---

## 🎓 Final Summary

```
Exception Handling in Python:
──────────────────────────────────────────────────────────────
GOLDEN RULES:
  1. Catch SPECIFIC exceptions — not bare except
  2. Never silently swallow exceptions (no empty except: pass)
  3. Use finally for cleanup — always runs!
  4. Use else for success code — not in try block
  5. Catch specific BEFORE broad (FileNotFoundError before OSError)
  6. Use EAFP style — just try it!

STRUCTURE:
  try      → risky code
  except   → handle specific errors
  else     → runs only on success
  finally  → always runs (cleanup)

RAISE:
  raise ExceptionType("message")         # new exception
  raise ExceptionType("msg") from e      # chain to original
  raise ExceptionType("msg") from None   # suppress chain
  raise                                  # re-raise current

CUSTOM EXCEPTIONS:
  class MyError(Exception): pass
  → Inherit from Exception (or more specific base)
  → Add attributes for context in __init__
  → Build hierarchy: AppError → UserError → UserNotFoundError

PATTERNS:
  EAFP       → try first, handle failure (Pythonic!)
  Guard      → validate early, fail fast
  Default    → return safe value on error
  Retry      → decorator for transient failures
  Result     → wrap success/failure in object
  Suppress   → contextlib.suppress for expected failures

LOGGING:
  logger.exception("msg")  → logs error + full traceback
  exc_info=True             → add traceback to any log level
──────────────────────────────────────────────────────────────
```

---
