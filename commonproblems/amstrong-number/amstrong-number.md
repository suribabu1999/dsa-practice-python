# 🔢 Armstrong Number Problem

## 📌 Problem Statement

Write a program to determine whether a given number is an **Armstrong Number**.

An **Armstrong Number** (also called a **Narcissistic Number**) is a number that is equal to the **sum of its digits each raised to the power of the number of digits in the number**.

If the calculated sum is equal to the original number, then the number is called an **Armstrong Number**.

Otherwise, it is **not an Armstrong Number**.

---

# 🧠 Understanding the Concept

To check whether a number is an Armstrong number, follow these logical steps:

1. Take the input number.
2. Count how many digits the number has.
3. Separate each digit of the number.
4. Raise each digit to the power of the **total number of digits**.
5. Add all those values together.
6. Compare the result with the original number.

If both are equal → **Armstrong Number**  
If they are different → **Not an Armstrong Number**

---

# 🔍 Example 1

### Number
```
153
```

### Step 1: Count digits

```
Digits in 153 = 3
```

### Step 2: Break the digits

```
1, 5, 3
```

### Step 3: Raise each digit to the power of 3

```
1³ = 1
5³ = 125
3³ = 27
```

### Step 4: Add them

```
1 + 125 + 27 = 153
```

### Step 5: Compare

```
153 == 153
```

✅ **Result:** 153 is an **Armstrong Number**

---

# 🔍 Example 2

### Number
```
370
```

### Step 1: Count digits

```
Digits = 3
```

### Step 2: Break digits

```
3, 7, 0
```

### Step 3: Raise to power 3

```
3³ = 27
7³ = 343
0³ = 0
```

### Step 4: Add them

```
27 + 343 + 0 = 370
```

### Step 5: Compare

```
370 == 370
```

✅ **Result:** 370 is an **Armstrong Number**

---

# 🔍 Example 3

### Number
```
9474
```

### Step 1: Count digits

```
Digits = 4
```

### Step 2: Break digits

```
9, 4, 7, 4
```

### Step 3: Raise to power 4

```
9⁴ = 6561
4⁴ = 256
7⁴ = 2401
4⁴ = 256
```

### Step 4: Add them

```
6561 + 256 + 2401 + 256 = 9474
```

### Step 5: Compare

```
9474 == 9474
```

✅ **Result:** 9474 is an **Armstrong Number**

---

# ❌ Example of a Non-Armstrong Number

### Number
```
123
```

### Step 1: Count digits

```
Digits = 3
```

### Step 2: Break digits

```
1, 2, 3
```

### Step 3: Raise to power 3

```
1³ = 1
2³ = 8
3³ = 27
```

### Step 4: Add them

```
1 + 8 + 27 = 36
```

### Step 5: Compare

```
36 ≠ 123
```

❌ **Result:** 123 is **NOT an Armstrong Number**

---

# 📚 Common Armstrong Numbers

Some well-known Armstrong numbers are:

```
0
1
153
370
371
407
1634
8208
9474
```

---

# 🎯 Key Points to Remember

✔ Armstrong numbers depend on the **number of digits**  
✔ Each digit is raised to the **power of total digits**  
✔ If the sum equals the original number → Armstrong number  
✔ Works for **any number of digits**

---

# 🧩 Practice Questions

Try solving these manually:

1. Is **371** an Armstrong number?
2. Check whether **407** is an Armstrong number.
3. Verify if **1634** is an Armstrong number.
4. Is **200** an Armstrong number?
5. Find Armstrong numbers between **100 and 999**.

---
