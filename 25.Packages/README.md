# Comprehensive Beginner's Tutorial on Python Packages

## Introduction

In Python, as projects grow in complexity and size, organizing code into manageable, reusable, and logically structured parts becomes essential. This is where **modules** and **packages** come in. While a _module_ is a single file containing Python definitions and statements, a _package_ is a way of organizing related modules together using a directory structure.

This tutorial will walk you through everything you need to know as a beginner about Python packages, from basic concepts to best practices.

---

## Table of Contents

1. What Is a Module?
2. What Is a Package?
3. Creating a Basic Package
4. Importing from Packages
5. The Role of `__init__.py`
6. Absolute vs Relative Imports
7. Controlling Imports with `__all__`
8. Sub-packages and Nested Packages
9. Namespace Packages
10. Best Practices
11. Practice Project: Build Your Own Calculator Package

---

## 1. What Is a Module?

A **module** is a Python file (`.py`) that contains code (functions, classes, variables) you can reuse in other files by importing it.

### Example

```python
# greetings.py

def say_hello(name):
    return f"Hello, {name}!"
```

You can use it in another file like this:

```python
import greetings
print(greetings.say_hello("Alice"))
```

---

## 2. What Is a Package?

A **package** is a directory that contains a special file named `__init__.py` (can be empty) and one or more Python modules or sub-packages. It tells Python that the directory should be treated as a package.

Packages allow for hierarchical organization of the module namespace using dot notation.

---

## 3. Creating a Basic Package

Let’s say we want to create a package called `mypkg`.

### Directory Structure

```
mypkg/
├── __init__.py
├── mod1.py
└── mod2.py
```

### `mod1.py`

```python
def greet():
    return "Hello from mod1"
```

### `mod2.py`

```python
def farewell():
    return "Goodbye from mod2"
```

### `__init__.py`

```python
# This file makes 'mypkg' a package. It can also contain package-level initialization.
print("mypkg package initialized")
```

### Usage

```python
import mypkg.mod1
print(mypkg.mod1.greet())
```

---

## 4. Importing from Packages

### Option 1: Full path

```python
import mypkg.mod1
mypkg.mod1.greet()
```

### Option 2: Specific function

```python
from mypkg.mod1 import greet
print(greet())
```

### Option 3: Alias

```python
from mypkg.mod1 import greet as hello
hello()
```

---

## 5. The Role of `__init__.py`

The `__init__.py` file is executed when the package is imported. It can:

- Initialize package-level data
- Control what is exposed when the package is imported
- Aggregate imports from submodules

### Example

```python
# mypkg/__init__.py
from .mod1 import greet
from .mod2 import farewell
```

Then you can use:

```python
from mypkg import greet, farewell
```

---

## 6. Absolute vs Relative Imports

### Absolute Import

```python
from mypkg.mod1 import greet
```

### Relative Import (used inside packages)

```python
from .mod1 import greet  # current package
from ..subpackage import something  # parent package
```

Avoid relative imports in scripts executed directly; they are more suitable inside modules.

---

## 7. Controlling Imports with `__all__`

To specify which names to import when using `from mypkg import *`, define `__all__`.

### `mypkg/__init__.py`

```python
__all__ = ['mod1', 'mod2']
```

Now only `mod1` and `mod2` are accessible via wildcard imports.

---

## 8. Sub-packages and Nested Packages

You can nest packages inside packages.

### Structure

```
mypkg/
├── __init__.py
├── mod1.py
└── subpkg/
    ├── __init__.py
    └── mod3.py
```

### Usage

```python
from mypkg.subpkg import mod3
```

---

## 9. Namespace Packages

In Python 3.3+, a directory without `__init__.py` can still be treated as a package. This allows splitting a package across multiple directories.

### Structure (no `__init__.py`)

```
mypkg/
├── mod1.py
└── mod2.py
```

Still importable with:

```python
import mypkg.mod1
```

---

## 10. Best Practices

- ✅ Use `__init__.py` even though it's optional (for clarity).
- ✅ Structure related functionality into logical modules.
- ✅ Keep function and class names descriptive.
- ✅ Use relative imports only inside packages, not scripts.
- ✅ Avoid `from module import *` in production code.
- ✅ Document your modules and packages.

---

## 11. Practice Project: Build Your Own Calculator Package

### Goal

Create a package `calculator` with modules for basic operations.

### Structure

```
calculator/
├── __init__.py
├── add.py
├── subtract.py
├── multiply.py
└── divide.py
```

### Example: `add.py`

```python
def add(a, b):
    return a + b
```

### Example: `__init__.py`

```python
from .add import add
from .subtract import subtract
from .multiply import multiply
from .divide import divide
```

### Usage

```python
from calculator import add, subtract
print(add(5, 3))         # 8
print(subtract(10, 4))   # 6
```

---

## Conclusion

Python packages allow you to organize and reuse code across multiple modules and projects. Understanding how to create, structure, and import from packages will help you build scalable and maintainable applications. Practice by building your own packages and gradually using more advanced patterns like sub-packages and namespace packages.
