# Python Data Types: A Comprehensive Tutorial

In Python, data types define the kind of value a variable holds. Python has a rich set of built-in data types that cater to various kinds of data, from simple numbers to complex data structures. Understanding these data types and how they work is crucial for writing efficient and effective Python code.

This tutorial will cover the following data types in Python, including their characteristics, uses, and examples.

---

## 1. **Numeric Types**

Python provides several numeric types for handling numbers.

### a. **Integers (`int`)**

Integers are whole numbers, positive or negative, without a decimal point. They are of arbitrary size, limited only by the available memory.

**Example**:

```python
a = 5
b = -123
large_number = 12345678901234567890
```

- **Key points**:
  - Integers can be used in arithmetic operations.
  - Python’s `int` type can handle numbers of virtually any size.

### b. **Floating-Point Numbers (`float`)**

Floating-point numbers represent real numbers and include a decimal point. Python uses IEEE 754 double-precision for representing floating-point numbers.

**Example**:

```python
pi = 3.14159
negative_float = -0.000123
scientific_notation = 1.23e4  # Equivalent to 12300.0
```

- **Key points**:
  - Floating-point numbers can lose precision due to the limitations of representing real numbers in binary.
  - Floats are useful for more precise calculations, such as scientific measurements.

### c. **Complex Numbers (`complex`)**

A complex number consists of a real part and an imaginary part. In Python, complex numbers are denoted with a `j` for the imaginary part.

**Example**:

```python
z = 3 + 4j  # Real part 3, Imaginary part 4
```

- **Key points**:
  - Complex numbers are often used in mathematical computations involving electrical engineering or signal processing.
  - You can access the real and imaginary parts of complex numbers using `.real` and `.imag`.

---

## 2. **Boolean Type (`bool`)**

The Boolean data type represents two possible values: `True` and `False`.

**Example**:

```python
a = True
b = False
```

- **Key points**:
  - `True` is treated as `1`, and `False` is treated as `0`.
  - Booleans are essential in conditional statements and logical operations.

---

## 3. **Text Type (`str`)**

The `str` type is used for representing text (strings). Strings in Python can be created using either single or double quotes.

**Example**:

```python
message = "Hello, World!"
name = 'Alice'
multiline_str = """This is
a multi-line
string"""
```

- **Key points**:
  - Strings are immutable, meaning you cannot modify a string in place.
  - Python provides various string methods like `.upper()`, `.replace()`, and `.split()` to manipulate strings.

---

## 4. **Sequence Types**

Python has multiple sequence types that represent ordered collections of items. These types include lists, tuples, and ranges.

### a. **List (`list`)**

Lists are mutable sequences that can store elements of different types.

**Example**:

```python
numbers = [1, 2, 3, 4]
mixed = [1, "apple", 3.14, True]
```

- **Key points**:
  - Lists are mutable, meaning you can modify them after creation.
  - Lists support operations like slicing, appending, and removing elements.

### b. **Tuple (`tuple`)**

Tuples are immutable sequences, meaning they cannot be changed after they are created.

**Example**:

```python
point = (3, 4)
colors = ("red", "green", "blue")
```

- **Key points**:
  - Since tuples are immutable, they are often used for fixed data.
  - They can be used as dictionary keys, unlike lists.

### c. **Range (`range`)**

A range represents an immutable sequence of numbers, often used in loops.

**Example**:

```python
r = range(5)  # Output: 0, 1, 2, 3, 4
```

- **Key points**:
  - The `range()` function is frequently used in `for` loops to iterate over a sequence of numbers.

---

## 5. **Set Types**

Sets are unordered collections of unique elements, used when you want to eliminate duplicates from a collection.

### a. **Set (`set`)**

A set is a mutable collection that cannot contain duplicate items.

**Example**:

```python
fruits = {"apple", "banana", "cherry"}
```

- **Key points**:
  - Sets automatically remove duplicates.
  - They are unordered, so elements are not indexed.

### b. **Frozen Set (`frozenset`)**

A `frozenset` is an immutable version of a set.

**Example**:

```python
frozen_fruits = frozenset({"apple", "banana", "cherry"})
```

- **Key points**:
  - Unlike regular sets, you cannot modify a `frozenset` once created.
  - `frozenset` can be used as dictionary keys.

---

## 6. **Mapping Type (`dict`)**

Dictionaries are unordered collections of key-value pairs. Keys must be immutable, and values can be any data type.

**Example**:

```python
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

- **Key points**:
  - Dictionaries are fast for lookups by key.
  - They are mutable, allowing you to add, update, and remove key-value pairs.

---

## 7. **Binary Types**

Python provides types for handling binary data, such as bytes, bytearrays, and memory views.

### a. **Bytes (`bytes`)**

Bytes are immutable sequences of bytes, useful for handling raw binary data.

**Example**:

```python
b = b"Hello"
```

- **Key points**:
  - Used when working with binary data, such as files or network communication.

### b. **Byte Array (`bytearray`)**

A `bytearray` is a mutable version of `bytes`.

**Example**:

```python
ba = bytearray([65, 66, 67])
```

- **Key points**:
  - You can modify a `bytearray` in place.

### c. **Memory View (`memoryview`)**

Memory views allow access to binary data without copying it.

**Example**:

```python
mv = memoryview(b"Hello")
```

- **Key points**:
  - Useful for efficient handling of large data structures without duplicating data.

---

## 8. **None Type**

`None` represents the absence of a value. It is often used as a default value or to indicate the lack of a return value from a function.

**Example**:

```python
result = None
```

- **Key points**:
  - `None` is frequently used as a placeholder for missing or undefined values.

---

## Summary Table

| Data Type    | Description                                      | Mutable? | Example                   |
| ------------ | ------------------------------------------------ | -------- | ------------------------- |
| `int`        | Integer, whole number                            | No       | `x = 5`                   |
| `float`      | Floating-point number                            | No       | `x = 3.14`                |
| `complex`    | Complex number (real + imaginary part)           | No       | `x = 1 + 2j`              |
| `bool`       | Boolean (True or False)                          | No       | `x = True`                |
| `str`        | String (sequence of characters)                  | No       | `x = "Hello"`             |
| `list`       | Mutable sequence of items                        | Yes      | `x = [1, 2, 3]`           |
| `tuple`      | Immutable sequence of items                      | No       | `x = (1, 2, 3)`           |
| `set`        | Unordered collection of unique items             | Yes      | `x = {1, 2, 3}`           |
| `frozenset`  | Immutable set                                    | No       | `x = frozenset({1, 2})`   |
| `dict`       | Collection of key-value pairs                    | Yes      | `x = {"key": "value"}`    |
| `bytes`      | Immutable sequence of bytes                      | No       | `x = b"Hello"`            |
| `bytearray`  | Mutable sequence of bytes                        | Yes      | `x = bytearray([65, 66])  |
| `memoryview` | Memory view object that exposes buffer interface | Yes      | `x = memoryview(b"Hello") |
| `None`       | Represents no value                              | No       | `x = None`                |

---

## Conclusion

Understanding Python’s data types is essential for writing efficient and effective code. Python's rich set of data types provides flexibility for handling various kinds of data, from numbers to complex data structures. Whether you're working with simple data or handling more complex collections, Python's data types offer clear and concise ways to represent and manipulate data in your programs.

---

---

---

# **Comprehensive Guide to Keywords in Python**

## **What are Keywords in Python?**

Keywords are reserved words in Python that have a **special meaning** and cannot be used as variable names, function names, or identifiers. These keywords are an essential part of Python's syntax, and they define the structure and flow of a Python program.

Python has a fixed number of keywords, which may change with different versions of Python.

---

## **List of Python Keywords (Python 3.10)**

Here is a list of Python keywords:

| Keyword    | Description                                                |
| ---------- | ---------------------------------------------------------- |
| `False`    | Boolean false value                                        |
| `None`     | Represents a null value or no value                        |
| `True`     | Boolean true value                                         |
| `and`      | Logical AND operator                                       |
| `as`       | Used in aliasing (e.g., `import numpy as np`)              |
| `assert`   | Used for debugging                                         |
| `async`    | Used for asynchronous programming                          |
| `await`    | Used with async functions                                  |
| `break`    | Exits a loop immediately                                   |
| `class`    | Defines a class                                            |
| `continue` | Skips the rest of the loop and moves to the next iteration |
| `def`      | Defines a function                                         |
| `del`      | Deletes objects                                            |
| `elif`     | Else-if statement for conditional execution                |
| `else`     | Specifies an alternative block in an if-else statement     |
| `except`   | Handles exceptions                                         |
| `finally`  | Executes code after a try-except block                     |
| `for`      | Used for loops                                             |
| `from`     | Used in import statements                                  |
| `global`   | Declares a global variable                                 |
| `if`       | Used for conditional statements                            |
| `import`   | Imports a module                                           |
| `in`       | Checks membership in a sequence                            |
| `is`       | Checks identity of two objects                             |
| `lambda`   | Defines an anonymous function                              |
| `nonlocal` | Modifies a variable from an enclosing scope                |
| `not`      | Logical NOT operator                                       |
| `or`       | Logical OR operator                                        |
| `pass`     | Placeholder for future code                                |
| `raise`    | Raises an exception                                        |
| `return`   | Returns a value from a function                            |
| `try`      | Defines a block of code to test for exceptions             |
| `while`    | Creates a while loop                                       |
| `with`     | Simplifies resource management (e.g., file handling)       |
| `yield`    | Used in generator functions                                |

You can check Python keywords dynamically using the `keyword` module:

```python
import keyword
print(keyword.kwlist)
```

---

## **1. Boolean Keywords: `True`, `False`, `None`**

Python uses `True` and `False` as Boolean values.

```python
x = True
y = False
print(x and y)  # Output: False
```

The `None` keyword represents **null** or no value.

```python
a = None
print(a)  # Output: None
```

---

## **2. Control Flow Keywords: `if`, `elif`, `else`**

These keywords are used for decision-making.

```python
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

✅ **Output:**

```
Positive
```

---

## **3. Loop Keywords: `for`, `while`, `break`, `continue`, `pass`**

- `for`: Used for iteration over sequences
- `while`: Runs a loop as long as a condition is `True`
- `break`: Exits the loop immediately
- `continue`: Skips the current iteration
- `pass`: Placeholder for future code

```python
for i in range(5):
    if i == 3:
        break  # Stops the loop at 3
    print(i)
```

✅ **Output:**

```
0
1
2
```

---

## **4. Function and Class Keywords: `def`, `return`, `lambda`, `class`**

- `def`: Defines a function
- `return`: Returns a value from a function
- `lambda`: Creates an anonymous function
- `class`: Defines a class

```python
def square(n):
    return n * n

print(square(4))  # Output: 16

# Lambda function
double = lambda x: x * 2
print(double(5))  # Output: 10
```

---

## **5. Exception Handling Keywords: `try`, `except`, `finally`, `raise`**

Used for handling errors.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always executes.")
```

✅ **Output:**

```
Cannot divide by zero!
This block always executes.
```

---

## **6. Import Keywords: `import`, `from`, `as`**

Used for importing modules.

```python
import math
print(math.sqrt(16))  # Output: 4.0

from math import pi
print(pi)  # Output: 3.141592653589793

import numpy as np  # Aliasing
```

---

## **7. Identity and Membership Keywords: `is`, `in`**

- `is`: Checks if two variables refer to the same object
- `in`: Checks if a value exists in a sequence

```python
a = [1, 2, 3]
b = a
print(a is b)  # Output: True (same memory reference)

print(2 in a)  # Output: True (2 is in list a)
```

---

## **8. Asynchronous Programming: `async`, `await`**

Used in asynchronous programming.

```python
import asyncio

async def hello():
    print("Hello, Async!")

asyncio.run(hello())
```

✅ **Output:**

```
Hello, Async!
```

---

## **9. Variable Scope Keywords: `global`, `nonlocal`**

- `global`: Used to modify global variables inside a function
- `nonlocal`: Modifies variables from an enclosing scope

```python
x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)  # Output: 20
```

```python
def outer():
    y = 5
    def inner():
        nonlocal y
        y = 10
    inner()
    print(y)

outer()  # Output: 10
```

---

## **Conclusion**

- Python keywords are reserved words that have specific meanings.
- They **cannot be used as variable names**.
- They control the flow of a Python program.
