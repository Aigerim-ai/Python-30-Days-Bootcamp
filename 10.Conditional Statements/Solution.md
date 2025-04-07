### Problem 1: Check if a number is positive, negative, or zero

```python
# Problem 1: Check if a number is positive, negative, or zero
x = int(input("Enter a number: "))

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

---

### Problem 2: Grade Determination

```python
# Problem 2: Grade Determination
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

### Problem 3: Even or Odd

```python
# Problem 3: Even or Odd
x = int(input("Enter a number: "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### Problem 4: Leap Year Check

```python
# Problem 4: Leap Year Check
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

### Problem 5: Grading System with Edge Cases

```python
# Problem 5: Grading System with Edge Cases
score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

### Bonus Challenge: Nested Conditions

```python
# Bonus Challenge: Nested Conditions
x = int(input("Enter a number: "))

if x % 2 == 0 and x % 3 == 0:
    print("Divisible by 2 and 3")
elif x % 2 == 0:
    print("Divisible by 2 but not 3")
elif x % 3 == 0:
    print("Divisible by 3 but not 2")
else:
    print("Not divisible by 2 or 3")
```
