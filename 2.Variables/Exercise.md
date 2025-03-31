### **Python Variables Exercise: "My Profile"**

#### **Objective:**

Practice declaring and assigning variables in Python.

#### **Instructions:**

Create a simple Python program that stores information about yourself using variables.

1. **Declare the following variables:**

   - `name` → Your name (string)
   - `age` → Your age (integer)
   - `height` → Your height in meters (float)
   - `is_student` → Whether you are a student (boolean, `True` or `False`)

2. **Print out each variable in a sentence.**  
   Example output:

   ```
   My name is Alex.
   I am 25 years old.
   My height is 1.75 meters.
   Am I a student? True
   ```

3. **Bonus Challenge:**
   - Change the value of `age` to one year older and print the updated value.
   - Change `is_student` to `False` (if it was `True`) or `True` (if it was `False`), then print the new value.

---

### **Sample Code (Solution)**

```python
# Step 1: Declare variables
name = "Alex"
age = 25
height = 1.75
is_student = True

# Step 2: Print variables
print("My name is", name)
print("I am", age, "years old")
print("My height is", height, "meters")
print("Am I a student?", is_student)

# Bonus Challenge
age += 1  # One year older
is_student = not is_student  # Toggle student status

print("Next year, I will be", age, "years old.")
print("Updated student status:", is_student)
```

This exercise will help beginners understand:  
✅ Variable declaration and assignment  
✅ Different data types (`str`, `int`, `float`, `bool`)  
✅ Printing variables
