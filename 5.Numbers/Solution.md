## **Exercises: Understanding Python Numbers**

### **1. Identify the Type of Numbers**

Determine the type of each number in Python.

```python
# Exercise
num1 = 42
num2 = 3.14
num3 = 2 + 3j
num4 = False

print(type(num1))  # What will this output?
print(type(num2))  # What about this?
print(type(num3))  # And this?
print(type(num4))  # Finally, this?
```

**Solution:**

```python
print(type(num1))  # <class 'int'>
print(type(num2))  # <class 'float'>
print(type(num3))  # <class 'complex'>
print(type(num4))  # <class 'bool'>
```

---

### **2. Perform Basic Arithmetic**

Perform the given arithmetic operations.

```python
# Exercise
a = 10
b = 4

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
```

**Solution:**

```python
print(a + b)  # 14
print(a - b)  # 6
print(a * b)  # 40
print(a / b)  # 2.5
print(a // b) # 2
print(a % b)  # 2
print(a ** b) # 10000
```

---

### **3. Type Conversions**

Convert between different types.

```python
# Exercise
x = 5.75
y = 100
z = "123"

print(int(x))     # Convert float to int
print(float(y))   # Convert int to float
print(int(z))     # Convert string to int
```

**Solution:**

```python
print(int(x))     # 5
print(float(y))   # 100.0
print(int(z))     # 123
```

---

### **4. Using Built-in Numeric Functions**

Use Python's built-in numeric functions.

```python
# Exercise
n1 = -8
n2 = 3.5678
n3 = 2

print(abs(n1))       # Absolute value
print(round(n2, 2))  # Round to 2 decimal places
print(pow(n3, 3))    # Power function
print(max(5, 10, 15, 2))  # Maximum value
print(min(5, 10, 15, 2))  # Minimum value
```

**Solution:**

```python
print(abs(n1))       # 8
print(round(n2, 2))  # 3.57
print(pow(n3, 3))    # 8
print(max(5, 10, 15, 2))  # 15
print(min(5, 10, 15, 2))  # 2
```

---

### **5. Using the Math Module**

Use Python's `math` module to perform advanced calculations.

```python
import math

# Exercise
print(math.sqrt(25))   # Square root
print(math.factorial(5))  # Factorial
print(math.sin(math.pi / 2))  # Sine function
print(math.log2(16))   # Log base 2
print(math.ceil(4.3))  # Ceiling function
print(math.floor(4.7)) # Floor function
```

**Solution:**

```python
print(math.sqrt(25))   # 5.0
print(math.factorial(5))  # 120
print(math.sin(math.pi / 2))  # 1.0
print(math.log2(16))   # 4.0
print(math.ceil(4.3))  # 5
print(math.floor(4.7)) # 4
```

---

### **6. Working with Complex Numbers**

Perform calculations using complex numbers.

```python
# Exercise
z1 = 4 + 3j
z2 = 2 + 5j

print(z1 + z2)  # Add
print(z1 - z2)  # Subtract
print(z1 * z2)  # Multiply
print(z1 / z2)  # Divide
print(z1.real)  # Real part of z1
print(z1.imag)  # Imaginary part of z1
```

**Solution:**

```python
print(z1 + z2)  # (6+8j)
print(z1 - z2)  # (2-2j)
print(z1 * z2)  # (2+23j)
print(z1 / z2)  # (0.8275862068965518-0.41379310344827586j)
print(z1.real)  # 4.0
print(z1.imag)  # 3.0
```

---

### **7. Using the `cmath` Module**

Use the `cmath` module for complex number calculations.

```python
import cmath

# Exercise
c1 = 1 + 2j

print(cmath.sqrt(-1))  # Square root of -1
print(cmath.exp(c1))   # Exponential of a complex number
print(cmath.phase(c1)) # Phase of the complex number
```

**Solution:**

```python
print(cmath.sqrt(-1))  # 1j
print(cmath.exp(c1))   # (-1.1312043837568135+2.4717266720048188j)
print(cmath.phase(c1)) # 1.1071487177940904
```

---

### **8. None Type**

Understand the `None` type in Python.

```python
# Exercise
def test_function():
    return None

result = test_function()
print(result)      # What will this print?
print(type(result))  # What is the type of result?
```

**Solution:**

```python
print(result)      # None
print(type(result))  # <class 'NoneType'>
```

---

## **Summary**

These exercises covered:

- Identifying number types
- Performing arithmetic operations
- Type conversions
- Using built-in functions
- Working with complex numbers
- Utilizing Python’s math and cmath modules
