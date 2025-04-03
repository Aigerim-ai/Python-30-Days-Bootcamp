## **Exercises: Understanding Python Numbers**

### **1. Identifying Number Types**

Identify the type of each number in Python. Use the `type()` function to check.

#### **Exercise:**

```python
# Predict the output before running
print(type(42))
print(type(3.14159))
print(type(2 + 3j))
print(type(True))
```

#### **Questions:**

- What type does Python assign to each number?
- How do Booleans behave in arithmetic operations?

---

### **2. Performing Arithmetic Operations**

Write a program that performs basic arithmetic operations on two numbers.

#### **Exercise:**

```python
# Define two numbers
a = 15
b = 4

# Perform calculations
sum_result = a + b
difference = a - b
product = a * b
quotient = a / b
floor_division = a // b
modulus = a % b
power = a ** b

# Print results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Power:", power)
```

#### **Questions:**

- What is the difference between `/` and `//`?
- What happens if `b = 0` when using `/` or `%`?

---

### **3. Type Conversions**

Convert different number types and observe the results.

#### **Exercise:**

```python
# Convert float to integer
print(int(9.99))

# Convert integer to float
print(float(100))

# Convert boolean to integer
print(int(True), int(False))

# Convert scientific notation to integer
print(int(2e2))
```

#### **Questions:**

- Why does `int(9.99)` return `9` instead of `10`?
- What happens when converting `True` and `False` to integers?

---

### **4. Using Built-in Numeric Functions**

Use Python’s built-in functions to perform operations.

#### **Exercise:**

```python
# Absolute value
print(abs(-15))

# Round a floating point number
print(round(3.675, 2))

# Power function
print(pow(3, 4))

# Find the max and min in a list
numbers = [4, 7, 2, 9, 1]
print(max(numbers))
print(min(numbers))
```

#### **Questions:**

- What happens when rounding `3.675`?
- What is the difference between `pow(x, y)` and `x ** y`?

---

### **5. Working with the Math Module**

Use Python’s `math` module for advanced calculations.

#### **Exercise:**

```python
import math

# Find square root
print(math.sqrt(25))

# Find logarithm (base 10)
print(math.log10(1000))

# Find sine of 90 degrees
print(math.sin(math.radians(90)))
```

#### **Questions:**

- What happens if you try `math.sqrt(-1)`?
- Why use `math.radians(90)` instead of `math.sin(90)`?

---

### **6. Complex Number Operations**

Perform arithmetic with complex numbers.

#### **Exercise:**

```python
z1 = 3 + 4j
z2 = 1 - 2j

# Addition
print(z1 + z2)

# Multiplication
print(z1 * z2)

# Find magnitude (absolute value)
print(abs(z1))

# Extract real and imaginary parts
print(z1.real, z1.imag)
```

#### **Questions:**

- What happens when you multiply two complex numbers?
- What does `abs(z1)` return?

---

### **7. Advanced Complex Number Functions**

Use the `cmath` module for complex calculations.

#### **Exercise:**

```python
import cmath

# Square root of a negative number
print(cmath.sqrt(-16))

# Exponential function
print(cmath.exp(1j * cmath.pi))
```

#### **Questions:**

- What is the result of `cmath.exp(1j * cmath.pi)`?
- How does `cmath.sqrt(-16)` differ from `math.sqrt(-16)`?

---

### **8. Exploring `None` in Python**

Experiment with `None` in functions.

#### **Exercise:**

```python
def my_function():
    return None

result = my_function()
print(result)
```

#### **Questions:**

- What happens if you try `print(result + 1)`?
- How is `None` different from `0` or `False`?

---

### **Bonus Challenge: User Input and Math Operations**

Write a program that takes two numbers from the user and performs various operations.

#### **Exercise:**

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")
print(f"Power: {num1 ** num2}")
```

#### **Questions:**

- What happens if you enter `0` for `num2`?
- Can you modify the program to handle division by zero?

---

### **Final Thoughts**

These exercises cover different aspects of working with numbers in Python. Completing them will give you a strong foundation in numeric operations, type conversions, built-in functions, and handling special cases like complex numbers and `None`.
