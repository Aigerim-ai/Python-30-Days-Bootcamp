### **Solution: Python Script**

```python
# Arithmetic Operations
x = 15
y = 4
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

print("\n")

# Assignment Operators
a = 10
a += 5
print("After a += 5:", a)
a *= 3
print("After a *= 3:", a)
a -= 8
print("After a -= 8:", a)
a //= 2
print("After a //= 2:", a)

print("\n")

# Comparison Operators
m = 25
n = 30
print("m == n:", m == n)
print("m != n:", m != n)
print("m > n:", m > n)
print("m <= n:", m <= n)

print("\n")

# Logical Operators
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

print("\n")

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)  # False (Different objects)
print("list1 is list3:", list1 is list3)  # True (Same object)
print("list1 == list2:", list1 == list2)  # True (Same values)

print("\n")

# Membership Operators
text = "Hello, Python!"
print('"Python" in text:', "Python" in text)
print('"Java" not in text:', "Java" not in text)

print("\n")

# Bitwise Operators
a = 5  # 101 in binary
b = 3  # 011 in binary

print("a & b:", a & b)  # 1 (001)
print("a | b:", a | b)  # 7 (111)
print("a ^ b:", a ^ b)  # 6 (110)
print("~a:", ~a)        # -6 (2's complement)
print("a << 1:", a << 1)  # 10 (1010)
print("b >> 1:", b >> 1)  # 1 (001)
```

---

### **Expected Output:**

```
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Floor Division: 3
Modulus: 3
Exponentiation: 50625


After a += 5: 15
After a *= 3: 45
After a -= 8: 37
After a //= 2: 18


m == n: False
m != n: True
m > n: False
m <= n: True


p and q: False
p or q: True
not p: False


list1 is list2: False
list1 is list3: True
list1 == list2: True


"Python" in text: True
"Java" not in text: True


a & b: 1
a | b: 7
a ^ b: 6
~a: -6
a << 1: 10
b >> 1: 1
```
