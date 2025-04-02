### **Solution: Python Keywords & Data Types**

1️⃣ **Identify Keywords**  
 **Answers (True/False):**

```python
1. while   → True  ✅ (Python keyword)
2. integer → False ❌ (Not a Python keyword)
3. import  → True  ✅ (Python keyword)
4. function → False ❌ (Not a Python keyword)
5. return  → True  ✅ (Python keyword)
6. string  → False ❌ (Not a Python keyword)
7. lambda  → True  ✅ (Python keyword)
8. def     → True  ✅ (Python keyword)
```

2️⃣ **Data Type Identification**  
 **Answers:**

```python
x = 10                # int
y = 3.14              # float
z = "Hello, World!"   # str
a = True              # bool
b = [1, 2, 3]         # list
c = (4, 5, 6)         # tuple
d = { "name": "Alice", "age": 25 }  # dict
e = {7, 8, 9}         # set
```

3️⃣ **Fix the Errors**  
 **Corrected Code:**

```python
# Corrected code
course = "Python Course"  # 'class' is a reserved keyword, so we rename it.
number10 = 5  # Variable names cannot start with a number.
is_true = True  # TRUE should be written as True (Python is case-sensitive).

def sum_numbers(a, b):  # 'sum' is a built-in function; renaming it is better.
    return a + b  # 'plus' is incorrect; use '+' instead.
```

---

### **Bonus Challenge Solution 🎯**

To print all **reserved keywords** in Python:

```python
import keyword

print(keyword.kwlist)  # Prints a list of all Python keywords
```

---
