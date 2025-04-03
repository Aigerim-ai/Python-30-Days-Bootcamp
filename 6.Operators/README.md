# **Comprehensive Guide to Operators in Python**

Operators in Python are symbols or keywords that allow you to perform operations on variables and values. Python provides different types of operators for performing mathematical computations, comparisons, logical operations, and bitwise operations.

---

## **1. Types of Operators in Python**

Python supports the following types of operators:

1. **Arithmetic Operators**
2. **Assignment Operators**
3. **Relational (Comparison) Operators**
4. **Logical Operators**
5. **Identity Operators**
6. **Membership Operators**
7. **Bitwise Operators**
8. **Operator Precedence**

---

## **2. Arithmetic Operators**

Arithmetic operators perform mathematical operations such as addition, subtraction, multiplication, and division.

| Operator       | Symbol | Example   | Result |
| -------------- | ------ | --------- | ------ |
| Addition       | `+`    | `5 + 3`   | `8`    |
| Subtraction    | `-`    | `10 - 4`  | `6`    |
| Multiplication | `*`    | `6 * 3`   | `18`   |
| Division       | `/`    | `10 / 2`  | `5.0`  |
| Floor Division | `//`   | `10 // 3` | `3`    |
| Modulus        | `%`    | `10 % 3`  | `1`    |
| Exponentiation | `**`   | `2 ** 3`  | `8`    |

### **Example:**

```python
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
```

✅ **Output:**

```
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Floor Division: 3
Modulus: 1
Exponentiation: 1000
```

---

## **3. Assignment Operators**

Assignment operators are used to assign values to variables. Python also provides compound assignment operators that combine arithmetic and assignment.

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `a = 5`   | `a = 5`       |
| `+=`     | `a += 3`  | `a = a + 3`   |
| `-=`     | `a -= 2`  | `a = a - 2`   |
| `*=`     | `a *= 4`  | `a = a * 4`   |
| `/=`     | `a /= 3`  | `a = a / 3`   |
| `//=`    | `a //= 2` | `a = a // 2`  |
| `%=`     | `a %= 2`  | `a = a % 2`   |
| `**=`    | `a **= 2` | `a = a ** 2`  |

### **Example:**

```python
x = 10
x += 5   # x = x + 5
print(x) # Output: 15
```

---

## **4. Relational (Comparison) Operators**

These operators compare two values and return `True` or `False`.

| Operator | Meaning                  | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 5` | `True`  |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `2 < 4`  | `True`  |
| `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | Less than or equal to    | `3 <= 2` | `False` |

### **Example:**

```python
a = 10
b = 5
print(a > b)   # True
print(a == b)  # False
```

---

## **5. Logical Operators**

Logical operators are used for boolean logic operations.

| Operator | Meaning                      | Example          | Result  |
| -------- | ---------------------------- | ---------------- | ------- |
| `and`    | True if both are True        | `True and False` | `False` |
| `or`     | True if at least one is True | `True or False`  | `True`  |
| `not`    | Reverses the condition       | `not True`       | `False` |

### **Example:**

```python
x = 10
y = 20
print(x > 5 and y < 30)  # True
print(x > 15 or y > 25)  # False
print(not (x > 5))       # False
```

---

## **6. Identity Operators**

Identity operators check if two variables point to the **same object in memory**.

| Operator | Meaning                                                   | Example      | Result       |
| -------- | --------------------------------------------------------- | ------------ | ------------ |
| `is`     | Returns `True` if both variables point to the same object | `a is b`     | `True/False` |
| `is not` | Returns `True` if variables are different objects         | `a is not b` | `True/False` |

### **Example:**

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)   # True (same memory location)
print(x is z)   # False (different objects)
print(x == z)   # True (same values)
```

---

## **7. Membership Operators**

These operators check if a value exists in a sequence (list, tuple, string, etc.).

| Operator | Meaning                              | Example              | Result |
| -------- | ------------------------------------ | -------------------- | ------ |
| `in`     | Returns `True` if value is found     | `"a" in "apple"`     | `True` |
| `not in` | Returns `True` if value is not found | `"b" not in "apple"` | `True` |

### **Example:**

```python
numbers = [1, 2, 3, 4]
print(3 in numbers)   # True
print(5 not in numbers)  # True
```

---

## **8. Bitwise Operators**

Bitwise operators perform operations at the **binary level**.

| Operator | Meaning     | Example (5 = 101, 3 = 011) | Result    |
| -------- | ----------- | -------------------------- | --------- |
| `&`      | Bitwise AND | `5 & 3`                    | `1` (001) |
| `        | `           | Bitwise OR                 | `5        |
| `^`      | Bitwise XOR | `5 ^ 3`                    | `6` (110) |
| `~`      | Bitwise NOT | `~5`                       | `-6`      |
| `<<`     | Left shift  | `5 << 1`                   | `10`      |
| `>>`     | Right shift | `5 >> 1`                   | `2`       |

### **Example:**

```python
a = 5  # 101
b = 3  # 011
print(a & b)  # 1 (001)
print(a | b)  # 7 (111)
print(a ^ b)  # 6 (110)
```

---

### **Understanding Operator Precedence in Python**

Operator precedence tells Python **which operation to perform first** in a complex expression.

Think of it like **math rules**—multiplication happens before addition unless you use parentheses.

---

### **Operator Precedence Order**

Here’s how Python decides which operation to execute first:

| Operator    | Description                                       | Precedence (Priority) |
| ----------- | ------------------------------------------------- | --------------------- |
| `()`        | Parentheses (grouping operations)                 | **Highest**           |
| `**`        | Exponentiation (power)                            | High                  |
| `* / // %`  | Multiplication, Division, Floor Division, Modulus | Medium                |
| `+ -`       | Addition, Subtraction                             | Medium-Low            |
| `== != > <` | Comparison Operators                              | Low                   |
| `not`       | Logical NOT                                       | Lower                 |
| `and`       | Logical AND                                       | Very Low              |
| `or`        | Logical OR                                        | **Lowest**            |

---

### **How It Works in Python**

#### **1. Parentheses (`()`) Have the Highest Priority**

Operations inside `()` **always** happen first.

```python
print((3 + 5) * 2)  # 16 (Addition first because of parentheses)
```

Without parentheses:

```python
print(3 + 5 * 2)  # 13 (Multiplication first, then addition)
```

---

#### **2. Exponentiation (`**`) Happens Before Multiplication & Division\*\*

```python
print(2 ** 3 * 4)  # 32 (Exponentiation first: 2³ = 8, then 8 * 4 = 32)
```

To change order:

```python
print(2 ** (3 * 4))  # 4096 (Multiplication first inside parentheses, then exponentiation)
```

---

#### **3. Multiplication & Division Happen Before Addition & Subtraction**

```python
print(10 + 5 * 2)  # 20 (Multiplication first: 5 * 2 = 10, then 10 + 10 = 20)
```

To add first:

```python
print((10 + 5) * 2)  # 30 (Parentheses force addition first)
```

---

#### **4. Comparison Operators (`== != > <`) Come After Math Operations**

```python
print(10 + 5 > 12)  # True (Addition first: 10 + 5 = 15, then 15 > 12)
```

---

#### **5. Logical Operators (`not`, `and`, `or`) Have the Lowest Priority**

- `not` is applied **first**.
- `and` is **stronger** than `or`.
- `or` happens **last**.

```python
print(True or False and False)  # True (AND happens first, then OR)
```

- `False and False` → `False`
- `True or False` → `True`

To change order:

```python
print((True or False) and False)  # False (Parentheses force OR first)
```

---

### **Summary**

1. **Use parentheses `()`** when you want to control the order.
2. **Exponentiation `**`\*\* happens before multiplication/division.
3. **Multiplication & division** happen before addition/subtraction.
4. **Logical operators (`not`, `and`, `or`) happen last.**

---

## **Conclusion**

Python provides a wide range of operators for arithmetic, assignment, comparisons, logical operations, identity checks, membership checks, and bitwise operations. Understanding these operators helps in writing efficient Python code.
