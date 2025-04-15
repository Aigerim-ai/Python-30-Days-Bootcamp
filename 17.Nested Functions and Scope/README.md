# Nested Functions and Scope in Python – A Deep Dive

Understanding **nested functions** and **variable scope** is essential to mastering Python. They form the foundation of many advanced features like **closures**, **decorators**, and **functional programming** patterns.

---

## 🧠 What Are Nested Functions?

A **nested function** is simply a function defined **inside another function**.

You can imagine it like this:

> 🍳 “A recipe within a recipe.” The outer recipe (function) contains all the steps, and the inner recipe (function) performs a specific step of the bigger task.

---

## ✅ Step 1: Basic Syntax

Let’s look at the structure:

```python
def outer_function():
    def inner_function():
        # code inside the inner function
    # code inside the outer function
```

Here:

- `inner_function()` is only accessible from inside `outer_function()`.
- It's not visible or usable outside.

---

## 🧪 Step 2: Simple Nested Function Example

Let’s start with a basic print example.

```python
def outer():
    def inner():
        print("Inside inner function!")
    inner()  # Inner is called inside outer
    print("Inside outer function!")

outer()
```

### 🔍 Output:

```
Inside inner function!
Inside outer function!
```

### 💡 Key Points:

- `inner()` is defined and called **within** `outer()`.
- You **cannot** call `inner()` from outside `outer()`.

---

## 🧪 Step 3: Using Outer Function Variables

Nested functions can **access variables** from their enclosing function. This is called **enclosing (nonlocal) scope**.

```python
def outer(x):
    def inner():
        return x * 2
    return inner()

print(outer(5))
```

### 🔍 Output:

```
10
```

### 💡 Key Points:

- `inner()` can **see and use** `x` from `outer()`.

---

---

# 🐍 Understanding Python Variable Scope: Local, Global, and Nonlocal

One of the key concepts in Python (and most programming languages) is **variable scope**. Understanding how variable scope works can save you from many bugs and headaches as your code grows in complexity. In this blog, we’ll explore **three main types of variable scope** in Python: **local**, **global**, and **nonlocal**.

---

## 📍 What is Variable Scope?

Variable scope refers to the **region of the program where a variable is accessible**. Depending on where a variable is declared, it can be local to a function, global to the entire program, or nonlocal within nested functions.

Let’s dive into each one.

---

## 🔹 Local Variables in Python

Local variables are declared **inside a function** and can **only be accessed within that function**. They’re temporary and exist only during the function's execution.

### Example:

```python
def greet():
    # local variable
    message = 'Hello'
    print('Local:', message)

greet()

# trying to access the local variable outside its scope
print(message)  # This will cause an error
```

### Output:

```
Local: Hello
NameError: name 'message' is not defined
```

As you can see, `message` is local to the `greet()` function and cannot be accessed outside of it.

---

## 🔸 Global Variables in Python

Global variables are defined **outside of all functions**, making them accessible **from anywhere in your code**, including inside functions.

### Example:

```python
# declare global variable
message = 'Hello'

def greet():
    print('Local:', message)

greet()
print('Global:', message)
```

### Output:

```
Local: Hello
Global: Hello
```

Here, `message` is declared in the global scope and accessed both inside and outside the `greet()` function.

---

## 🔹 Nonlocal Variables in Python

Nonlocal variables come into play when dealing with **nested functions**. If you want to modify a variable from an outer function inside a nested function, use the `nonlocal` keyword.

### Example:

```python
def outer():
    message = 'local'

    def inner():
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
```

### Output:

```
inner: nonlocal
outer: nonlocal
```

In this case, the `nonlocal` keyword lets the inner function modify the `message` variable from its enclosing function `outer()`.

---

## 🧠 Summary

Here’s a quick summary of Python variable scopes:

| Scope    | Defined In              | Accessible From                                 | Keyword Used                           |
| -------- | ----------------------- | ----------------------------------------------- | -------------------------------------- |
| Local    | Inside a function       | Only that function                              | _(None)_                               |
| Global   | Outside all functions   | Anywhere in the file                            | `global` (to modify inside a function) |
| Nonlocal | Inside nested functions | Inner function modifies outer function variable | `nonlocal`                             |

---

## 💡 Final Thoughts

Understanding variable scope is essential for writing clean, bug-free Python code. Whether you’re building a small script or a complex application, knowing when and where your variables are accessible can help you write better, more predictable code.

Have any questions or want to share your thoughts on Python scopes? Drop a comment below! 🚀

---
