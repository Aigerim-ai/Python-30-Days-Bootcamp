---
# 🐍 Python Exception Handling: A Complete Tutorial
---

## 📌 What Are Exceptions?

An **exception** is an error that occurs **during the execution** of a program. Instead of crashing your program immediately, Python provides a way to handle the error gracefully.

### ❗ Common Causes of Exceptions:

- Trying to divide by zero
- Accessing a list index that doesn't exist
- Opening a file that doesn't exist
- Incorrect input type

---

## 🧠 Why Handle Exceptions?

Without exception handling:

```python
x = 10 / 0  # ZeroDivisionError
```

With exception handling:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

Your program **continues** instead of crashing.

---

## 🔤 Basic Syntax of try-except

```python
try:
    # Code that might throw an error
except SomeException:
    # Code that runs if the error occurs
```

### ✅ Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Oops! That was not a valid number.")
```

---

## 💡 Common Built-in Exceptions

| Exception           | What It Means                                |
| ------------------- | -------------------------------------------- |
| `ZeroDivisionError` | Dividing by zero                             |
| `ValueError`        | Invalid value (e.g. converting "abc" to int) |
| `IndexError`        | Accessing a list index that doesn’t exist    |
| `KeyError`          | Accessing a dict key that doesn't exist      |
| `TypeError`         | Operation on incompatible types              |
| `FileNotFoundError` | File not found when trying to open           |

---

## 🔄 Handling Multiple Exceptions

```python
try:
    num = int(input("Number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Enter numbers only.")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

---

## 🔀 Using `else` with `try`

The `else` block runs **only if the `try` block doesn't raise an exception**.

```python
try:
    print("Trying...")
    num = int(input("Enter number: "))
except ValueError:
    print("That's not a number.")
else:
    print("Success! You entered:", num)
```

---

## 🔚 Using `finally`

The `finally` block **always runs**, whether or not there was an exception.

```python
try:
    f = open("data.txt", "r")
    # do something with the file
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing the file (if it was opened).")
```

---

## 🧱 Nested try-except Blocks

You can **nest** one try-except inside another.

```python
try:
    num = int(input("Enter a number: "))
    try:
        result = 10 / num
    except ZeroDivisionError:
        print("Division by zero inside nested block.")
except ValueError:
    print("Invalid number entered.")
```

---

## 🎯 Raising Exceptions Manually

You can raise exceptions using the `raise` keyword.

```python
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age can't be negative")
```

---

## 🧰 Creating Custom Exceptions

Define your own exceptions by subclassing `Exception`.

```python
class NegativeAgeError(Exception):
    pass

age = int(input("Enter age: "))
if age < 0:
    raise NegativeAgeError("Age cannot be negative!")
```

---

## 🛠️ Practical Example: File Reader

```python
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Sorry, the file does not exist.")
    except IOError:
        print("An I/O error occurred.")
    finally:
        print("Finished attempting to read the file.")
```

---

## 🧪 Catching Multiple Exceptions at Once

```python
try:
    # some code
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
```

---

## 🧵 Best Practices for Exception Handling

✅ **Be specific** — catch only the exceptions you expect  
✅ **Use `finally` for cleanup** like closing files or DB connections  
✅ **Avoid bare except:**

```python
# Bad:
try:
    ...
except:
    print("Something went wrong")  # Hides real error
```

✅ **Log exceptions** for debugging  
✅ **Don't suppress exceptions silently**  
✅ **Use custom exceptions for application-specific errors**

---

## 🧩 Summary

| Block     | Purpose                   |
| --------- | ------------------------- |
| `try`     | Code that may throw error |
| `except`  | Handle specific error     |
| `else`    | Code to run if no error   |
| `finally` | Code that always runs     |

---

## 📘 Exercises

1. Write a function that reads a number from the user and divides 100 by that number. Handle all possible exceptions.
2. Create a program that reads a file and counts the number of lines. Handle the case where the file doesn't exist.
3. Create a custom exception called `EmptyInputError` and raise it if the user inputs an empty string.

---
