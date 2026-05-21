# 🐍 Python OOP: Zero to Hero
### 👨‍🏫 *By Your 30-Year Experienced Python Professor*
> *"Object-Oriented Programming is not just a feature of Python — it's a way of THINKING. Once you master OOP, you'll never look at code the same way again!"* — Prof. 🎓

---

## 📚 Table of Contents

1. [🌱 What is OOP?](#1--what-is-oop)
2. [🏗️ Classes & Objects](#2--classes--objects)
3. [🔧 The `__init__` Constructor](#3--the-__init__-constructor)
4. [🎭 Instance, Class & Static Methods](#4--instance-class--static-methods)
5. [📦 Encapsulation](#5--encapsulation)
6. [👨‍👦 Inheritance](#6--inheritance)
7. [🎨 Polymorphism](#7--polymorphism)
8. [🪄 Abstraction](#8--abstraction)
9. [✨ Magic / Dunder Methods](#9--magic--dunder-methods)
10. [🏠 Properties — `@property`](#10--properties--property)
11. [🔗 Composition vs Inheritance](#11--composition-vs-inheritance)
12. [📐 SOLID Principles](#12--solid-principles)
13. [🧩 Design Patterns in Python](#13--design-patterns-in-python)
14. [🚀 Advanced OOP Concepts](#14--advanced-oop-concepts)
15. [🎯 Sample Projects to Build](#15--sample-projects-to-build)

---

## 1. 🌱 What is OOP?

> 💡 **Professor's Analogy:** *"Imagine the real world. A 'Car' is a blueprint (class). Your red Honda is an actual car (object). Every car has properties (color, speed) and behaviors (drive, brake). OOP models the real world in code!"*

**OOP = Object-Oriented Programming** — organizing code into **objects** that bundle **data (attributes)** and **behavior (methods)** together.

### 4 Pillars of OOP 🏛️

```
┌──────────────────────────────────────────────┐
│              4 PILLARS OF OOP                │
│                                              │
│  🔒 Encapsulation  →  Hide internal details  │
│  👨‍👦 Inheritance    →  Reuse & extend code    │
│  🎨 Polymorphism   →  One interface, many    │
│                        forms                 │
│  🪄 Abstraction    →  Show only essentials   │
└──────────────────────────────────────────────┘
```

### Procedural vs OOP

```python
# 🙁 Procedural Style — data and functions are separate
name = "Alice"
balance = 1000

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount

# 😎 OOP Style — data and behavior live TOGETHER
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
```

---

## 2. 🏗️ Classes & Objects

> 🧑‍🏫 *"A CLASS is the blueprint/template. An OBJECT is the actual thing built from that blueprint. You can create a million objects from one class!"*

### Defining a Class

```python
class Dog:
    # Class attribute — shared by ALL instances
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, age):
        # Instance attributes — unique to each object
        self.name  = name
        self.breed = breed
        self.age   = age

    def bark(self):
        return f"{self.name} says: Woof! 🐕"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"
```

### Creating Objects (Instantiation)

```python
# Creating objects from the Dog class
dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max",   "Poodle",   5)
dog3 = Dog("Luna",  "Husky",    2)

print(dog1.bark())       # Buddy says: Woof! 🐕
print(dog2.describe())   # Max is a 5-year-old Poodle
print(dog3.name)         # Luna

# Class attribute accessed by all
print(dog1.species)      # Canis lupus familiaris
print(Dog.species)       # Same! Accessed via class name
```

### Understanding `self` 🤔

```python
class Counter:
    def __init__(self):
        self.count = 0  # 'self' refers to THIS specific object

    def increment(self):
        self.count += 1  # Modifies THIS object's count

    def reset(self):
        self.count = 0

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.count)  # 2 — c1's own count
print(c2.count)  # 1 — c2's own count (independent!)
```

> 🧑‍🏫 *"`self` is just a convention — you could name it anything, but PLEASE don't! `self` is sacred in Python."*

### Class vs Instance Attributes

```python
class Car:
    # Class attribute — same for ALL cars
    wheels = 4

    def __init__(self, brand, color):
        # Instance attributes — unique per car
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("Honda",  "Blue")

# Modifying CLASS attribute affects ALL instances
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6

# But if you set on an INSTANCE, it creates a local copy
car1.wheels = 4     # Now car1 has its OWN wheels attr
print(car1.wheels)  # 4  (instance attribute shadows class attr)
print(car2.wheels)  # 6  (still class attribute)
print(Car.wheels)   # 6
```

---

## 3. 🔧 The `__init__` Constructor

```python
class Person:
    """Represents a person. 👤"""

    def __init__(self, name: str, age: int, email: str = "N/A"):
        """
        Constructor — called automatically when object is created.
        Think of it as the 'birth certificate' of an object!
        """
        self.name  = name
        self.age   = age
        self.email = email
        self._id   = id(self)  # unique object identifier

    def __str__(self):
        """Human-readable string representation."""
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Person('{self.name}', {self.age}, '{self.email}')"

p1 = Person("Alice", 30, "alice@example.com")
p2 = Person("Bob",   25)  # email defaults to "N/A"

print(p1)        # Person(name=Alice, age=30)
print(repr(p2))  # Person('Bob', 25, 'N/A')
```

### Multiple Constructors using `@classmethod`

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor from Fahrenheit."""
        return cls((fahrenheit - 32) * 5/9)

    @classmethod
    def from_kelvin(cls, kelvin):
        """Alternative constructor from Kelvin."""
        return cls(kelvin - 273.15)

    def __str__(self):
        return f"{self.celsius:.2f}°C"

t1 = Temperature(100)                     # From Celsius
t2 = Temperature.from_fahrenheit(212)     # From Fahrenheit
t3 = Temperature.from_kelvin(373.15)      # From Kelvin

print(t1)  # 100.00°C
print(t2)  # 100.00°C
print(t3)  # 100.00°C ✨
```

---

## 4. 🎭 Instance, Class & Static Methods

```python
class MathUtils:
    # Class variable
    PI = 3.14159

    def __init__(self, value):
        self.value = value

    # 1️⃣ INSTANCE METHOD — has access to 'self' (the object)
    def double(self):
        return self.value * 2

    # 2️⃣ CLASS METHOD — has access to 'cls' (the class itself)
    @classmethod
    def circle_area(cls, radius):
        return cls.PI * radius ** 2  # Uses class variable

    # 3️⃣ STATIC METHOD — no access to self or cls
    @staticmethod
    def add(a, b):
        return a + b  # Just a regular function inside the class


m = MathUtils(10)

print(m.double())               # 20 — instance method
print(MathUtils.circle_area(5)) # 78.53... — class method
print(MathUtils.add(3, 4))      # 7 — static method
print(m.add(3, 4))              # 7 — also works from instance
```

### When to Use What? 🤔

```
┌────────────────┬────────────┬───────────────────────────────┐
│ Method Type    │ Decorator  │ Use When...                   │
├────────────────┼────────────┼───────────────────────────────┤
│ Instance       │ (none)     │ Needs object state (self)     │
│ Class          │ @classmethod│ Needs class state, alt       │
│                │            │ constructors, factory methods  │
│ Static         │ @staticmethod│ Utility function related to  │
│                │            │ the class, no state needed    │
└────────────────┴────────────┴───────────────────────────────┘
```

---

## 5. 📦 Encapsulation

> 💡 *"Encapsulation = data hiding. You control what the outside world can see and touch. It's like a TV remote — you press buttons (public interface) but you don't need to see the circuit board inside!"*

### Public, Protected, Private

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner        = owner       # 🟢 Public  — accessible anywhere
        self._account_num = "ACC123"    # 🟡 Protected — convention: don't touch directly
        self.__balance    = balance     # 🔴 Private  — name mangled, hard to access outside

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}. Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"💸 Withdrew ₹{amount}. Balance: ₹{self.__balance}")
        else:
            print("❌ Insufficient funds or invalid amount!")

    def get_balance(self):  # Controlled access via method (getter)
        return self.__balance


acc = BankAccount("Alice", 1000)

print(acc.owner)         # ✅ Alice — public
print(acc._account_num)  # ⚠️ ACC123 — works but conventionally private

# print(acc.__balance)   # ❌ AttributeError! Private!

# BUT Python does name mangling — not truly private:
print(acc._BankAccount__balance)  # 1000 (name mangled access — don't do this!)

acc.deposit(500)   # ✅ Deposited ₹500. Balance: ₹1500
acc.withdraw(200)  # 💸 Withdrew ₹200. Balance: ₹1300
print(acc.get_balance())  # 1300
```

### Name Mangling Explained

```python
class MyClass:
    def __init__(self):
        self.__secret = "hidden"  # stored as _MyClass__secret

obj = MyClass()
# obj.__secret          → AttributeError
# obj._MyClass__secret  → "hidden" (bypass, avoid this!)
print(dir(obj))  # You'll see '_MyClass__secret' in the list
```

---

## 6. 👨‍👦 Inheritance

> 🎓 *"Inheritance is the 'is-a' relationship. A Dog IS-A Animal. A Car IS-A Vehicle. Don't repeat yourself — inherit and extend!"*

### Single Inheritance

```python
class Animal:
    """Base class / Parent class / Superclass"""

    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound
        self.alive = True

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def breathe(self):
        return f"{self.name} is breathing 💨"

    def __str__(self):
        return f"Animal({self.name})"


class Dog(Animal):
    """Child class / Subclass — inherits from Animal"""

    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # Call parent's __init__
        self.breed = breed

    def fetch(self):  # New method — only for Dog
        return f"{self.name} fetches the ball! 🎾"

    def speak(self):  # OVERRIDE parent's speak
        return f"{self.name} barks: WOOF WOOF! 🐕"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs... 😸"

    def speak(self):
        return f"{self.name} meows: Meow~ 🐱"


d = Dog("Buddy", "Labrador")
c = Cat("Whiskers")

print(d.speak())    # Buddy barks: WOOF WOOF! 🐕  (overridden)
print(d.breathe())  # Buddy is breathing 💨         (inherited)
print(d.fetch())    # Buddy fetches the ball! 🎾    (new)
print(c.speak())    # Whiskers meows: Meow~ 🐱
print(c.purr())     # Whiskers purrs... 😸

# isinstance() checks
print(isinstance(d, Dog))     # True
print(isinstance(d, Animal))  # True — Dog IS-A Animal!
print(isinstance(c, Dog))     # False
```

### Multi-Level Inheritance

```python
class Vehicle:
    def __init__(self, make, model):
        self.make  = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def honk(self):
        return "Beep beep! 📯"

class ElectricCar(Car):
    def __init__(self, make, model, doors, battery_kWh):
        super().__init__(make, model, doors)
        self.battery = battery_kWh

    def charge(self):
        return f"⚡ {self.info()} charging with {self.battery} kWh battery"

tesla = ElectricCar("Tesla", "Model 3", 4, 75)
print(tesla.info())    # Tesla Model 3       (from Vehicle)
print(tesla.honk())    # Beep beep! 📯       (from Car)
print(tesla.charge())  # ⚡ Tesla Model 3... (from ElectricCar)
```

### Multiple Inheritance & MRO

```python
class Flyable:
    def fly(self):
        return "Flying! ✈️"

class Swimmable:
    def swim(self):
        return "Swimming! 🏊"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack! 🦆"

donald = Duck()
print(donald.fly())   # Flying! ✈️
print(donald.swim())  # Swimming! 🏊
print(donald.quack()) # Quack! 🦆

# Method Resolution Order (MRO) — which class is checked first?
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyable'>, <class 'Swimmable'>, <class 'object'>)
```

### `super()` Deep Dive

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        super().greet()      # Calls A's greet
        print("Hello from B")

class C(A):
    def greet(self):
        super().greet()      # Calls A's greet
        print("Hello from C")

class D(B, C):
    def greet(self):
        super().greet()      # Follows MRO: D → B → C → A
        print("Hello from D")

d = D()
d.greet()
# Hello from A
# Hello from C
# Hello from B
# Hello from D
```

---

## 7. 🎨 Polymorphism

> 🎓 *"Polymorphism = 'many forms'. Same method name, different behavior. It's what makes code flexible and extensible!"*

### Method Overriding (Runtime Polymorphism)

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        return f"I am a {type(self).__name__} with area {self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# 🌟 Polymorphism in action!
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(shape.describe())  # Same method call, different behavior!

# Output:
# I am a Circle with area 78.54
# I am a Rectangle with area 24.00
# I am a Triangle with area 12.00
```

### Duck Typing 🦆

```python
# "If it walks like a duck and quacks like a duck, it's a duck!"
# Python doesn't care about TYPE, only about BEHAVIOR

class Duck:
    def sound(self):
        return "Quack! 🦆"

class Person:
    def sound(self):
        return "I'm quacking like a duck! 👤"

class Robot:
    def sound(self):
        return "BEEP BOOP QUACK 🤖"

def make_it_quack(thing):
    print(thing.sound())  # Doesn't check type — just calls sound()!

make_it_quack(Duck())    # Quack! 🦆
make_it_quack(Person())  # I'm quacking like a duck! 👤
make_it_quack(Robot())   # BEEP BOOP QUACK 🤖
```

### Operator Overloading (A form of Polymorphism)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):     # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):     # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):    # v * 3
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):      # v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(v1 + v2)   # Vector(3, 7)
print(v1 - v2)   # Vector(1, -1)
print(v1 * 3)    # Vector(6, 9)
print(v1 == v2)  # False
```

---

## 8. 🪄 Abstraction

> 🎓 *"Abstraction = hide the complexity, show only what's necessary. When you drive a car, you use the steering wheel — you don't rewire the engine!"*

### Abstract Classes with `abc`

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstract base class for any database connection."""

    @abstractmethod
    def connect(self):
        """Must be implemented by subclass."""
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query: str):
        pass

    # Concrete method — shared by all subclasses
    def log(self, message):
        print(f"[LOG] {message}")


class MySQLConnection(DatabaseConnection):
    def connect(self):
        self.log("Connecting to MySQL... 🐬")
        return True

    def disconnect(self):
        self.log("Disconnecting from MySQL.")

    def execute_query(self, query):
        self.log(f"MySQL executing: {query}")
        return [{"id": 1, "name": "Alice"}]


class MongoDBConnection(DatabaseConnection):
    def connect(self):
        self.log("Connecting to MongoDB... 🍃")
        return True

    def disconnect(self):
        self.log("Disconnecting from MongoDB.")

    def execute_query(self, query):
        self.log(f"MongoDB executing: {query}")
        return {"result": "success"}


# ❌ Can't instantiate abstract class!
# db = DatabaseConnection()  # TypeError!

# ✅ Can only instantiate concrete subclasses
mysql = MySQLConnection()
mysql.connect()
result = mysql.execute_query("SELECT * FROM users")
print(result)
mysql.disconnect()
```

---

## 9. ✨ Magic / Dunder Methods

> 🎓 *"Dunder = Double UNDERscore. These are Python's hooks — implement them to make your objects behave like built-in types. This is pure Python magic!"*

### The Essential Dunders

```python
class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    # String representations
    def __str__(self):
        """For users — print(book)"""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """For developers — repr(book), debug"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # Comparison operators
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    # Arithmetic
    def __add__(self, other):
        """Combine two books into a collection."""
        return [self, other]

    # Container behavior
    def __len__(self):
        return self.pages

    def __contains__(self, word):
        """'word' in book — checks if word is in title."""
        return word.lower() in self.title.lower()

    # Make object callable
    def __call__(self, chapter):
        return f"📖 Reading chapter {chapter} of '{self.title}'..."

    # Context Manager (with statement)
    def __enter__(self):
        print(f"📚 Opening '{self.title}'")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"📕 Closing '{self.title}'")
        return False  # Don't suppress exceptions

    # Hashing (needed if you define __eq__)
    def __hash__(self):
        return hash((self.title, self.author))


b1 = Book("Python Crash Course", "Eric Matthes", 544)
b2 = Book("Fluent Python",       "Luciano",       792)
b3 = Book("Python Crash Course", "Eric Matthes",  544)

print(b1)             # "Python Crash Course" by Eric Matthes
print(repr(b1))       # Book('Python Crash Course', 'Eric Matthes', 544)
print(b1 == b3)       # True ✅
print(b1 < b2)        # True (544 < 792)
print(len(b1))        # 544
print("Python" in b1) # True
print(b1(3))          # 📖 Reading chapter 3 of 'Python Crash Course'...

# Context manager
with b1 as book:
    print(f"Reading {len(book)} pages")
# 📚 Opening 'Python Crash Course'
# Reading 544 pages
# 📕 Closing 'Python Crash Course'

# Sorting books by pages (uses __lt__)
library = [b2, b1]
print(sorted(library))  # Sorted by pages ascending
```

### Complete Dunder Methods Reference 📋

```python
# 🔢 Numeric Operations
__add__(self, other)      # +
__sub__(self, other)      # -
__mul__(self, other)      # *
__truediv__(self, other)  # /
__floordiv__(self, other) # //
__mod__(self, other)      # %
__pow__(self, other)      # **
__neg__(self)             # -obj (unary minus)
__abs__(self)             # abs(obj)

# 🔗 In-place operators
__iadd__(self, other)     # +=
__isub__(self, other)     # -=
__imul__(self, other)     # *=

# 📊 Comparison
__eq__(self, other)       # ==
__ne__(self, other)       # !=
__lt__(self, other)       # <
__le__(self, other)       # <=
__gt__(self, other)       # >
__ge__(self, other)       # >=

# 📦 Container
__len__(self)             # len(obj)
__getitem__(self, key)    # obj[key]
__setitem__(self, key, v) # obj[key] = v
__delitem__(self, key)    # del obj[key]
__contains__(self, item)  # item in obj
__iter__(self)            # for x in obj
__next__(self)            # next(obj)

# 🔠 String
__str__(self)             # str(obj), print(obj)
__repr__(self)            # repr(obj)
__format__(self, spec)    # format(obj, spec)

# 🧠 Object Lifecycle
__init__(self, ...)       # Constructor
__new__(cls, ...)         # Object creation (before init)
__del__(self)             # Destructor (when GC collects)

# 📞 Callable
__call__(self, ...)       # obj()

# 🔍 Attribute Access
__getattr__(self, name)   # obj.name (fallback)
__setattr__(self, name, v)# obj.name = v
__delattr__(self, name)   # del obj.name

# 🔑 Hashing
__hash__(self)            # hash(obj), used in sets/dicts

# 📂 Context Manager
__enter__(self)           # with obj as x:
__exit__(self, ...)       # end of with block
```

---

## 10. 🏠 Properties — `@property`

> 🎓 *"Properties let you add logic to attribute access without changing the public interface. Best of both worlds: simple attribute syntax + method power!"*

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Store privately

    @property
    def radius(self):
        """Getter — called when you read obj.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter — called when you write obj.radius = x"""
        if value < 0:
            raise ValueError("❌ Radius cannot be negative!")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter — called when you do del obj.radius"""
        print("Deleting radius...")
        del self._radius

    @property
    def diameter(self):
        """Computed property — no setter needed (read-only)"""
        return self._radius * 2

    @property
    def area(self):
        return 3.14159 * self._radius ** 2


c = Circle(5)
print(c.radius)    # 5  (calls getter)
print(c.diameter)  # 10 (computed)
print(c.area)      # 78.53...

c.radius = 10      # Calls setter
print(c.radius)    # 10

# c.radius = -5    # ❌ ValueError: Radius cannot be negative!
# c.diameter = 20  # ❌ AttributeError: can't set attribute (read-only)
```

### Real-World Property Example

```python
class Employee:
    def __init__(self, first, last, salary):
        self.first  = first
        self.last   = last
        self.salary = salary

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        parts = name.split(" ", 1)
        self.first = parts[0]
        self.last  = parts[1] if len(parts) > 1 else ""

    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    @property
    def annual_salary(self):
        return self.salary * 12

    @annual_salary.setter
    def annual_salary(self, value):
        self.salary = value / 12


emp = Employee("John", "Doe", 5000)
print(emp.full_name)       # John Doe
print(emp.email)           # john.doe@company.com
print(emp.annual_salary)   # 60000

emp.full_name = "Jane Smith"
print(emp.first)  # Jane
print(emp.email)  # jane.smith@company.com 🎉
```

---

## 11. 🔗 Composition vs Inheritance

> 🎓 *"Inheritance = IS-A relationship. Composition = HAS-A relationship. The golden rule: FAVOR COMPOSITION OVER INHERITANCE when in doubt!"*

```python
# ❌ Inheritance misuse: Robot IS-A Battery? No!
class Battery:
    def charge(self): ...

class Robot(Battery):  # Wrong! Robot is NOT a Battery
    pass

# ✅ Composition: Robot HAS-A Battery ✓
class Battery:
    def __init__(self, capacity_mAh):
        self.capacity  = capacity_mAh
        self.charge_pct = 100

    def drain(self, amount):
        self.charge_pct = max(0, self.charge_pct - amount)

    def recharge(self):
        self.charge_pct = 100
        print("⚡ Battery recharged!")

    def status(self):
        return f"Battery: {self.charge_pct}%"


class Motor:
    def __init__(self, power_watts):
        self.power = power_watts

    def run(self):
        return f"Motor running at {self.power}W 🔄"


class Camera:
    def __init__(self, megapixels):
        self.mp = megapixels

    def capture(self):
        return f"📸 Captured {self.mp}MP photo!"


class Robot:
    """Robot HAS-A Battery, Motor, and Camera"""

    def __init__(self, name):
        self.name    = name
        self.battery = Battery(5000)     # Composition!
        self.motor   = Motor(100)
        self.camera  = Camera(12)

    def move(self):
        if self.battery.charge_pct > 10:
            self.battery.drain(5)
            return self.motor.run()
        return "❌ Low battery! Can't move."

    def take_photo(self):
        self.battery.drain(2)
        return self.camera.capture()

    def status(self):
        return f"🤖 {self.name} | {self.battery.status()}"


r2d2 = Robot("R2-D2")
print(r2d2.move())       # Motor running at 100W 🔄
print(r2d2.take_photo()) # 📸 Captured 12MP photo!
print(r2d2.status())     # 🤖 R2-D2 | Battery: 93%
```

---

## 12. 📐 SOLID Principles

> 🎓 *"SOLID is the Bible of OOP design. Every senior developer lives by these. Master these and you'll write code that's maintainable for YEARS!"*

### S — Single Responsibility Principle

```python
# ❌ BAD — class does too many things
class User:
    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def save_to_database(self): ...  # Persistence — not User's job!
    def send_email(self): ...        # Email — not User's job!
    def validate_email(self): ...    # Validation — not User's job!

# ✅ GOOD — each class has ONE reason to change
class User:
    def __init__(self, name, email):
        self.name  = name
        self.email = email

class UserRepository:
    def save(self, user): ...       # Only handles persistence

class EmailService:
    def send(self, user, msg): ...  # Only handles email

class UserValidator:
    def validate(self, user): ...   # Only handles validation
```

### O — Open/Closed Principle

```python
# Open for EXTENSION, closed for MODIFICATION
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price): pass

class NoDiscount(Discount):
    def apply(self, price):
        return price

class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

# ✅ Adding new discount type = new class, NO modification of existing code!
class BuyOneGetOne(Discount):
    def apply(self, price):
        return price / 2

def checkout(price, discount: Discount):
    return discount.apply(price)

print(checkout(1000, PercentageDiscount(10)))  # 900.0
print(checkout(1000, FixedDiscount(150)))       # 850
print(checkout(1000, BuyOneGetOne()))           # 500.0
```

### L — Liskov Substitution Principle

```python
# ✅ Subclasses must be usable wherever the parent is used

class Bird:
    def fly(self):
        return "Flying! 🦅"

class Eagle(Bird):
    def fly(self):
        return "Eagle soaring high! 🦅"  # ✅ Substitutable

# ❌ Penguin is a Bird but CANNOT fly — violates LSP!
class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly! 🐧")

# ✅ Better design using proper abstraction
class FlyingBird:
    def fly(self): ...

class FlightlessBird:
    def swim(self): ...

class Eagle(FlyingBird):
    def fly(self):
        return "Eagle soaring! 🦅"

class Penguin(FlightlessBird):
    def swim(self):
        return "Penguin swimming! 🐧"
```

### I — Interface Segregation Principle

```python
# ❌ BAD — fat interface forces classes to implement useless methods
class Worker(ABC):
    @abstractmethod
    def work(self): pass

    @abstractmethod
    def eat(self): pass     # Robots don't eat!

    @abstractmethod
    def sleep(self): pass   # Robots don't sleep!

# ✅ GOOD — small, focused interfaces
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self): pass

class HumanWorker(Workable, Eatable, Sleepable):
    def work(self): return "Human working 👷"
    def eat(self):  return "Human eating 🍕"
    def sleep(self):return "Human sleeping 😴"

class RobotWorker(Workable):
    def work(self): return "Robot working 🤖"
    # No eat or sleep — not needed! ✅
```

### D — Dependency Inversion Principle

```python
# ❌ BAD — high-level depends on low-level
class LightBulb:
    def turn_on(self): print("💡 Bulb ON")
    def turn_off(self): print("💡 Bulb OFF")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()  # Tightly coupled! ❌

    def operate(self):
        self.bulb.turn_on()

# ✅ GOOD — depend on abstractions, not concretions
class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass
    @abstractmethod
    def turn_off(self): pass

class LightBulb(Switchable):
    def turn_on(self):  print("💡 Bulb ON")
    def turn_off(self): print("💡 Bulb OFF")

class Fan(Switchable):
    def turn_on(self):  print("🌀 Fan ON")
    def turn_off(self): print("🌀 Fan OFF")

class Switch:
    def __init__(self, device: Switchable):  # Depends on abstraction ✅
        self.device = device

    def operate(self, on: bool):
        self.device.turn_on() if on else self.device.turn_off()

switch1 = Switch(LightBulb())
switch2 = Switch(Fan())
switch1.operate(True)   # 💡 Bulb ON
switch2.operate(True)   # 🌀 Fan ON
```

---

## 13. 🧩 Design Patterns in Python

> 🎓 *"Design patterns are proven solutions to recurring problems. Learn them — they'll save you YEARS of trial and error!"*

### 🏭 Singleton Pattern

```python
class Singleton:
    """Only ONE instance can ever exist."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class AppConfig(Singleton):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.debug = False
            self.db_url = "localhost:5432"
            self.initialized = True

c1 = AppConfig()
c2 = AppConfig()
print(c1 is c2)  # True — same object! ✅
```

### 🏗️ Factory Pattern

```python
class Animal(ABC):
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    def speak(self): return "Woof! 🐕"

class Cat(Animal):
    def speak(self): return "Meow! 🐱"

class AnimalFactory:
    @staticmethod
    def create(animal_type: str) -> Animal:
        animals = {"dog": Dog, "cat": Cat}
        if animal_type not in animals:
            raise ValueError(f"Unknown animal: {animal_type}")
        return animals[animal_type]()

pet = AnimalFactory.create("dog")
print(pet.speak())  # Woof! 🐕
```

### 👀 Observer Pattern

```python
class EventSystem:
    """Simple observer / pub-sub pattern."""

    def __init__(self):
        self._listeners = {}

    def subscribe(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def publish(self, event, data=None):
        for cb in self._listeners.get(event, []):
            cb(data)

events = EventSystem()

# Subscribers
events.subscribe("user_login", lambda d: print(f"📧 Sending welcome email to {d}"))
events.subscribe("user_login", lambda d: print(f"📊 Logging login for {d}"))
events.subscribe("user_login", lambda d: print(f"🔔 Sending push notification to {d}"))

# Publisher
events.publish("user_login", "Alice")
# 📧 Sending welcome email to Alice
# 📊 Logging login for Alice
# 🔔 Sending push notification to Alice
```

### 🗺️ Strategy Pattern

```python
from typing import Protocol

class SortStrategy(Protocol):
    def sort(self, data: list) -> list: ...

class BubbleSort:
    def sort(self, data):
        d = data.copy()
        for i in range(len(d)):
            for j in range(len(d)-i-1):
                if d[j] > d[j+1]:
                    d[j], d[j+1] = d[j+1], d[j]
        return d

class QuickSort:
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[0]
        left  = [x for x in data[1:] if x <= pivot]
        right = [x for x in data[1:] if x > pivot]
        return self.sort(left) + [pivot] + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

data = [5, 2, 8, 1, 9, 3]

sorter = Sorter(BubbleSort())
print(sorter.sort(data))  # [1, 2, 3, 5, 8, 9]

sorter.strategy = QuickSort()  # Swap strategy at runtime!
print(sorter.sort(data))  # [1, 2, 3, 5, 8, 9]
```

---

## 14. 🚀 Advanced OOP Concepts

### Metaclasses

```python
# Metaclasses are the "class of a class"
# type is the default metaclass of every class

print(type(int))    # <class 'type'>
print(type(str))    # <class 'type'>
print(type(list))   # <class 'type'>

class MyMeta(type):
    """Custom metaclass that adds auto-logging."""

    def __new__(mcs, name, bases, namespace):
        # Auto-wrap all methods with logging
        for key, value in namespace.items():
            if callable(value) and not key.startswith("_"):
                namespace[key] = mcs._add_logging(value)
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def _add_logging(func):
        def wrapper(*args, **kwargs):
            print(f"📝 Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"✅ {func.__name__} completed")
            return result
        return wrapper


class MyService(metaclass=MyMeta):
    def process(self):
        return "Processing..."

    def save(self):
        return "Saved!"


svc = MyService()
svc.process()
# 📝 Calling process
# ✅ process completed
```

### Descriptors

```python
class PositiveNumber:
    """Descriptor — reusable attribute validation!"""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"❌ {self.name} must be a positive number!")
        obj.__dict__[self.name] = value


class Product:
    price    = PositiveNumber()  # Descriptor instance
    quantity = PositiveNumber()  # Descriptor instance

    def __init__(self, name, price, quantity):
        self.name     = name
        self.price    = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity


p = Product("Laptop", 999.99, 5)
print(p.total)    # 4999.95

# p.price = -100  # ❌ ValueError: price must be a positive number!
```

### `__slots__` — Memory Optimization

```python
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ['x', 'y']  # No __dict__ — saves memory!

    def __init__(self, x, y):
        self.x = x
        self.y = y


import sys
rp = RegularPoint(1, 2)
sp = SlottedPoint(1, 2)

print(f"Regular: {sys.getsizeof(rp.__dict__)} bytes for dict")
print(f"Slotted: No __dict__ — much lighter! 🪶")

# __slots__ prevents adding new attributes:
rp.z = 3   # ✅ Works
# sp.z = 3 # ❌ AttributeError — slots are fixed!
```

### Dataclasses — Modern OOP 🌟

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name:   str
    age:    int
    grades: List[float] = field(default_factory=list)
    gpa:    float = field(init=False)  # Computed, not passed in

    def __post_init__(self):
        """Called after __init__ — perfect for computed fields!"""
        self.gpa = sum(self.grades) / len(self.grades) if self.grades else 0.0

    def add_grade(self, grade: float):
        self.grades.append(grade)
        self.gpa = sum(self.grades) / len(self.grades)


s1 = Student("Alice", 20, [85, 92, 78, 96])
print(s1)       # Student(name='Alice', age=20, grades=[85,92,78,96], gpa=87.75)
print(s1.gpa)   # 87.75

s2 = Student("Bob", 21, [70, 88])
print(s1 == s2)   # False (auto __eq__ based on fields!)
```

### Mixins — The Power Technique 💪

```python
class JsonMixin:
    """Add JSON serialization to any class."""
    import json

    def to_json(self):
        import json
        return json.dumps(self.__dict__, indent=2)

    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class LogMixin:
    """Add logging to any class."""
    def log(self, msg):
        print(f"[{type(self).__name__}] {msg}")


class TimestampMixin:
    """Add creation timestamp to any class."""
    from datetime import datetime
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now().isoformat()


class User(TimestampMixin, JsonMixin, LogMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name  = name
        self.email = email

    def save(self):
        self.log(f"Saving user {self.name}...")
        return self.to_json()


u = User("Alice", "alice@example.com")
u.log("User created!")
print(u.to_json())
```

---

## 15. 🎯 Sample Projects to Build

> 🎓 *"Reading about OOP is 10%. Actually BUILDING projects is 90%. Here are 10 carefully chosen projects — ordered from beginner to advanced — that will cement every OOP concept you've learned!"*

---

### 🟢 BEGINNER LEVEL

---

#### 🏦 Project 1: Bank Management System
**Concepts:** Classes, encapsulation, inheritance, properties

**What to build:**
- `Account` base class with `__balance` (private), deposit, withdraw
- `SavingsAccount(Account)` — adds interest rate, compounds monthly
- `CheckingAccount(Account)` — adds overdraft limit
- `Bank` class that holds multiple accounts, transfers between them

**Key challenges:**
- Validate all transactions (negative amounts, overdraft)
- Implement `@property` for balance (read-only from outside)
- Use `__str__` and `__repr__` for nice printing
- Add transaction history as a list

```python
# Starter scaffold — you fill in the rest!
class Account:
    def __init__(self, owner, account_id, initial_balance=0):
        self.owner      = owner
        self.account_id = account_id
        self.__balance  = initial_balance
        self.__history  = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount): ...
    def withdraw(self, amount): ...
    def get_history(self): ...

class SavingsAccount(Account):
    def __init__(self, owner, account_id, balance, interest_rate):
        super().__init__(owner, account_id, balance)
        self.interest_rate = interest_rate

    def apply_interest(self): ...

class Bank:
    def __init__(self, name):
        self.name     = name
        self.accounts = {}

    def add_account(self, account): ...
    def transfer(self, from_id, to_id, amount): ...
    def total_assets(self): ...
```

---

#### 📚 Project 2: Library Management System
**Concepts:** Classes, composition, lists, searching, sorting

**What to build:**
- `Book` class with title, author, ISBN, available copies
- `Member` class with borrow/return history
- `Library` class that manages books and members
- Borrowing system with due dates

**Key challenges:**
- Search books by title, author, or ISBN
- Track who has which book
- Late fee calculation
- Use `__len__`, `__contains__` on Library class

---

#### 🎮 Project 3: Text-Based RPG Game
**Concepts:** Inheritance, polymorphism, composition, abstract classes

**What to build:**
- Abstract `Character` class with hp, attack, defend
- `Warrior`, `Mage`, `Archer` subclasses with unique abilities
- `Monster` base class with `Dragon`, `Goblin`, `Troll` subclasses
- `Battle` system using polymorphism
- `Inventory` system using composition
- `Item`, `Weapon`, `Potion` classes

**Key challenges:**
- Each character class has unique `special_attack()` (polymorphism)
- Items affect character stats (composition)
- Battle loop using abstract methods

---

### 🟡 INTERMEDIATE LEVEL

---

#### 🛒 Project 4: E-Commerce Cart System
**Concepts:** Design patterns (Factory, Observer), dataclasses, properties

**What to build:**
- `Product` (physical) and `DigitalProduct` classes
- `Cart` with add/remove/apply_discount
- `Order` with status transitions (pending → paid → shipped → delivered)
- Discount system: `PercentDiscount`, `FixedDiscount`, `BuyXGetY`
- Observer pattern: notify user on order status change

**Key challenges:**
- Apply multiple discount strategies (Strategy pattern)
- Observer for email/SMS notifications
- `__iter__` on Cart to loop over items
- Serialize cart to JSON using `__dict__`

---

#### 🐍 Project 5: Custom Data Structures Library
**Concepts:** Magic methods, generics, iterators, `__slots__`

**What to build:**
- `Stack` class with `push`, `pop`, `peek`, `__len__`, `__iter__`, `__contains__`
- `Queue` class with `enqueue`, `dequeue`
- `LinkedList` with `__getitem__`, `__setitem__`, `__delitem__`
- `BinaryTree` with in-order iteration (`__iter__`)
- `PriorityQueue` using `__lt__` for comparison

**Key challenges:**
- Implement `__iter__` and `__next__` for custom iteration
- Use `__slots__` for Node classes (memory efficiency)
- Make structures work with Python's `len()`, `in`, `for` naturally

---

#### 🌡️ Project 6: Smart Home Automation System
**Concepts:** Abstract classes, composition, Observer, Singleton, Strategy

**What to build:**
- Abstract `Device` class: `SmartLight`, `SmartThermostat`, `SmartLock`, `SmartTV`
- `Room` class that holds multiple devices (composition)
- `Home` class (Singleton — only one home!) holding rooms
- `AutomationRule` system: "If time is 10pm, turn off all lights"
- `EnergyMonitor` that observes all devices (Observer)

**Key challenges:**
- Singleton for the Home
- Observer for energy monitoring
- Devices have state machine: ON/OFF/STANDBY/ERROR
- Schedule-based automation using Strategy pattern

---

### 🔴 ADVANCED LEVEL

---

#### 🗄️ Project 7: Mini ORM (Object-Relational Mapper)
**Concepts:** Metaclasses, descriptors, `__init_subclass__`, advanced dunders

**What to build:**
- `Field` descriptor classes: `IntField`, `StringField`, `FloatField`
- `ModelMeta` metaclass that auto-registers fields
- `Model` base class: `save()`, `delete()`, `find()` (using SQLite)
- Query builder: `User.filter(age__gt=18).order_by('name').limit(10)`

```python
# Target API — what your ORM should support:
class User(Model):
    name  = StringField(max_length=100)
    age   = IntField(min_val=0)
    email = StringField(unique=True)

# Usage
User(name="Alice", age=30, email="alice@ex.com").save()
users = User.filter(age__gte=18).order_by("name").all()
```

**Key challenges:**
- Descriptors for field validation on assignment
- Metaclass to auto-detect fields and generate SQL
- `__init_subclass__` for auto table registration
- Fluent query builder (method chaining with `__getattr__`)

---

#### 🔌 Project 8: Plugin System / Extension Framework
**Concepts:** Abstract classes, metaclasses, dynamic imports, decorators

**What to build:**
- Plugin registry using metaclass (auto-registers subclasses)
- `@plugin` decorator to mark plugin entry points
- Plugin loader that discovers and loads plugins dynamically
- Hook system: plugins can hook into events

```python
# Target API
@plugin(name="csv_exporter", version="1.0")
class CSVExporter(ExporterPlugin):
    def export(self, data, filename): ...

@plugin(name="json_exporter", version="2.0")
class JSONExporter(ExporterPlugin):
    def export(self, data, filename): ...

# Auto-discovery
PluginManager.load_all()
exporter = PluginManager.get("csv_exporter")
exporter.export(data, "output.csv")
```

---

#### 🎲 Project 9: Game Engine (2D)
**Concepts:** Full OOP architecture, all patterns, mixins, ECS pattern

**What to build:**
- `Entity` base class for all game objects
- `Component` system: `Transform`, `Renderer`, `Physics`, `Collider`
- `System` classes that process components: `PhysicsSystem`, `RenderSystem`
- `Scene` manager: load/unload scenes
- `EventBus` for game events (Observer)
- `AssetManager` (Singleton) for images/sounds

**Architecture:**
```
GameEngine
├── SceneManager (scenes)
│   └── Scene
│       └── Entity[]
│           ├── TransformComponent
│           ├── RendererComponent
│           └── PhysicsComponent
├── EventBus (Observer)
├── AssetManager (Singleton)
└── Systems[]
    ├── PhysicsSystem
    ├── RenderSystem
    └── CollisionSystem
```

---

#### 🤖 Project 10: AI Chatbot Framework
**Concepts:** Everything! Full enterprise OOP architecture

**What to build:**
- Abstract `LLMProvider`: `OpenAIProvider`, `AnthropicProvider`, `LocalProvider`
- `Conversation` class with message history management
- `Memory` system: `ShortTermMemory`, `LongTermMemory` (file/DB backed)
- `Tool` abstract class: `WebSearchTool`, `CalculatorTool`, `WeatherTool`
- `Agent` class that orchestrates provider + memory + tools
- `Middleware` pipeline: logging, rate limiting, caching (Chain of Responsibility)

```python
# Target API — build toward this!
agent = Agent(
    provider=AnthropicProvider(model="claude-3"),
    memory=LongTermMemory(db="conversations.db"),
    tools=[WebSearchTool(), CalculatorTool()],
    middlewares=[LoggingMiddleware(), RateLimitMiddleware(60)]
)

response = agent.chat("What's the weather in Mumbai today?")
```

---

## 📋 Professor's Final Wisdom

> *"After 30 years of teaching, here's what separates great OOP programmers from mediocre ones:"*

### The 10 Commandments of OOP 📜

1. **🎯 Single Responsibility** — One class, one job. If you can't describe it in one sentence, split it.
2. **🔒 Encapsulate Everything** — Default to private. Expose only what's necessary.
3. **🔗 Favor Composition** — Before inheriting, ask: "Does this IS-A relationship truly make sense?"
4. **🪄 Program to Interfaces** — Depend on abstract classes, not concrete ones.
5. **📏 Keep Classes Small** — If a class has > 200 lines, it's doing too much.
6. **✨ Use Dunder Methods** — Make your objects feel native to Python.
7. **🏠 Use Properties** — Never expose raw attributes if validation is needed.
8. **📐 Follow SOLID** — These aren't optional — they're professional standards.
9. **🧪 Write Testable Code** — Good OOP design naturally leads to testable code.
10. **📖 Read Others' Code** — Study Django, SQLAlchemy source code. Real-world OOP mastery.

### Quick Reference Cheatsheet 📋

```python
# Class Definition
class MyClass(ParentClass):
    class_var = "shared"                    # Class variable

    def __init__(self, x):                  # Constructor
        self.x = x                          # Instance variable
        self._protected = "semi-private"    # Convention: protected
        self.__private  = "truly private"   # Name mangled

    def instance_method(self): ...          # Has access to self
    @classmethod
    def class_method(cls): ...              # Has access to cls
    @staticmethod
    def static_method(): ...               # No self or cls

    @property
    def value(self): return self.__private  # Getter
    @value.setter
    def value(self, v): self.__private = v  # Setter

    def __str__(self):  return "user string"  # print()
    def __repr__(self): return "dev string"   # repr()
    def __len__(self):  return 0              # len()
    def __eq__(self, o):return True           # ==
    def __lt__(self, o):return True           # <
    def __add__(self, o):return self          # +
    def __contains__(self, item): return True # in
    def __iter__(self): return iter([])       # for x in obj
    def __call__(self, *args): ...            # obj()
    def __enter__(self): return self          # with obj:
    def __exit__(self, *args): return False   #   end of with

# Inheritance
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)  # Call parent init
        self.y = y

# Abstract
from abc import ABC, abstractmethod
class Interface(ABC):
    @abstractmethod
    def must_implement(self): pass

# Dataclass
from dataclasses import dataclass
@dataclass
class Point:
    x: float
    y: float

# Check relationships
isinstance(obj, MyClass)      # Is obj an instance of MyClass?
issubclass(Child, Parent)     # Is Child a subclass of Parent?
type(obj)                     # Exact type
obj.__class__.__name__        # Class name as string
MyClass.__mro__               # Method Resolution Order
```

---

> *"OOP isn't about classes and objects. It's about thinking in systems, responsibilities, and relationships. Code like an architect — not just a programmer!"* 