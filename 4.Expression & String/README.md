# **Python Expressions and Strings: A Detailed Guide**

## **4.4 Expressions in Python**

An **expression** in Python is a combination of **values, variables, and operators** that can be evaluated to produce a result.

---

### **Basic Arithmetic Expressions**

Python supports common arithmetic operations, such as:  
✔️ **Addition (+)**  
✔️ **Subtraction (-)**  
✔️ **Multiplication (\*)**  
✔️ **Division (/)**  
✔️ **Floor Division (//)**  
✔️ **Modulo (%)**  
✔️ **Exponentiation (**)\*\*

#### **Example: Calculating an Average**

```python
x = 3
y = 5
z = (x + y) / 2  # Result is 4.0
print(z)
```

📌 **Note:**

- In **Python 3**, division (`/`) always returns a floating-point number, even when both operands are integers.
- To perform **integer division** (truncating decimals), use `//` instead.

#### **Example: Integer Division and Modulo**

```python
a = 10
b = 3

print(a // b)  # Output: 3 (integer division)
print(a % b)   # Output: 1 (remainder)
```

---

### **Operator Precedence in Expressions**

Python follows the **standard mathematical precedence rules** (PEMDAS):  
1️⃣ **Parentheses** `( )`  
2️⃣ **Exponentiation** `**`  
3️⃣ **Multiplication, Division, Floor Division, Modulo** `*, /, //, %`  
4️⃣ **Addition, Subtraction** `+, -`

#### **Example: Precedence in Action**

```python
result = 10 + 5 * 2  # Multiplication happens first
print(result)  # Output: 20

result = (10 + 5) * 2  # Parentheses change precedence
print(result)  # Output: 30
```

---

### **Expressions with Different Data Types**

Expressions can work with **strings, Booleans, and more**:

#### **String Concatenation**

```python
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!
```

#### **Boolean Expressions**

```python
x = 10
y = 5
print(x > y)  # Output: True
```

Python allows expressions beyond simple math—expressions involving strings, logical operations, and more.

---

## **4.5 Strings in Python**

A **string** is a sequence of characters enclosed in **single (' '), double (" "), or triple quotes (''' ''' or """ """)**. Strings are widely used in programming for handling text data.

---

### **Creating Strings**

```python
text1 = "Hello, World!"  # Double quotes
text2 = 'Hello, World!'  # Single quotes
print(text1 == text2)  # Output: True
```

✔️ You can use **single or double quotes** interchangeably.  
✔️ Single quotes **don’t require escaping** double quotes, and vice versa.

#### **Example: Avoiding Escape Characters**

```python
message1 = "Don't need a backslash"  # Correct
message2 = 'Can\'t get by without a backslash'  # Correct, but needs escape (\)
```

---

### **Escape Characters in Strings**

Python uses the **backslash (`\`)** to give special meaning to certain characters.

| Escape Sequence | Meaning             |
| --------------- | ------------------- |
| `\n`            | Newline (next line) |
| `\t`            | Tab space           |
| `\\`            | Backslash (`\`)     |
| `\'`            | Single quote (`'`)  |
| `\"`            | Double quote (`"`)  |

#### **Example: Using Escape Characters**

```python
x = "This is a new\nline"
print(x)
```

**Output:**

```
This is a new
line
```

---

### **Multi-line Strings**

You **cannot** split a normal string across multiple lines without using escape characters:

```python
# ❌ ERROR: This is not allowed
x = "This is a misguided attempt to
put a newline into a string without using backslash-n"
```

Instead, you should use **triple-quoted strings**:

#### **Example: Multi-line Strings**

```python
x = """This is a multi-line
string that spans
multiple lines."""
print(x)
```

✔️ **Triple quotes allow line breaks inside strings.**  
✔️ You can use **single (`'''`) or double (`"""`)** triple quotes.

---

### **Combining and Repeating Strings**

Strings can be **concatenated (joined)** using `+` and **repeated** using `*`:

#### **Example: Concatenation**

```python
greeting = "Hello" + ", " + "Python!"
print(greeting)  # Output: Hello, Python!
```

#### **Example: Repeating a String**

```python
laugh = "Ha" * 3
print(laugh)  # Output: HaHaHa
```

---

### **Conclusion**

- **Expressions** involve variables, values, and operators to produce a result.
- **Python follows standard precedence rules (PEMDAS).**
- **Strings** can be created using **single, double, or triple quotes**.
- **Escape sequences** allow special characters inside strings.
- **Triple-quoted strings** enable multi-line text.
- **Strings can be concatenated (`+`) and repeated (`*`).**
