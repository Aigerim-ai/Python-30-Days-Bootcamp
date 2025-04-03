### **Solution 1: Basic Input and Output**

```python
# Asking for user's first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Displaying the greeting message
print(f"Hello, {first_name} {last_name}! Welcome to Python.")
```

✅ **Example Output:**

```
Enter your first name: Alice
Enter your last name: Johnson
Hello, Alice Johnson! Welcome to Python.
```

---

### **Solution 2: Converting String Input to Integer**

```python
# Asking for user's birth year
birth_year = int(input("Enter your birth year: "))

# Calculating age
current_year = 2025
age = current_year - birth_year

# Displaying the result
print(f"You are {age} years old.")
```

✅ **Example Output:**

```
Enter your birth year: 1997
You are 28 years old.
```

---

### **Solution 3: Handling Decimal Numbers**

```python
# Asking for radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the area
pi = 3.14159
area = pi * (radius ** 2)

# Displaying the result
print(f"The area of the circle with radius {radius} is {area:.2f}.")
```

✅ **Example Output:**

```
Enter the radius of the circle: 5
The area of the circle with radius 5.0 is 78.54.
```

---

### **Solution 4: Performing Arithmetic Operations**

```python
# Asking for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Performing calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Displaying the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient:.2f}")
```

✅ **Example Output:**

```
Enter first number: 10
Enter second number: 5
Sum: 15
Difference: 5
Product: 50
Quotient: 2.00
```

---

### **Solution 5: Boolean Check with Membership Operator**

```python
# Asking for user input
user_input = input("Enter a word or phrase: ")

# Checking if "Python" is present
if "Python" in user_input:
    print("Yes, your input contains 'Python'!")
else:
    print("No, 'Python' is not found.")
```

✅ **Example Output:**

```
Enter a word or phrase: I love Python programming!
Yes, your input contains 'Python'!
```

---

### **Solution 6: Identity and Comparison Operators**

```python
# Asking for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Comparing values
if num1 == num2:
    print("The numbers are equal.")
elif num1 != num2:
    print("The numbers are not equal.")

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is smaller than {num2}.")
```

✅ **Example Output:**

```
Enter first number: 8
Enter second number: 5
The numbers are not equal.
8 is greater than 5.
```

---

### **Solution 7: Using f-strings for Output**

```python
# Asking for user's favorite color
color = input("Enter your favorite color: ")

# Displaying the response
print(f"Your favorite color is {color}. That's a great choice!")
```

✅ **Example Output:**

```
Enter your favorite color: Blue
Your favorite color is Blue. That's a great choice!
```

---

### **Solution 8: Full Interaction Program**

```python
# Asking for user's name
name = input("What is your name? ")

# Asking for user's age
age = int(input("How old are you? "))

# Asking for user's favorite number
fav_number = float(input("What is your favorite number? "))

# Displaying the collected information
print(f"Hello, {name}! You are {age} years old.")
print(f"Your favorite number is {fav_number}, which is interesting!")
```

✅ **Example Output:**

```
What is your name? John
How old are you? 30
What is your favorite number? 7.5
Hello, John! You are 30 years old.
Your favorite number is 7.5, which is interesting!
```

---
