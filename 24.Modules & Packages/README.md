**Note on Python Modules and Packages for Modular Programming**

Modular programming in Python involves dividing a large programming task into smaller, manageable modules. This approach makes development simpler, more maintainable, and promotes code reuse. Python supports modularization through **functions**, **modules**, and **packages**.

- **Simplicity**: Each module handles a small part of the problem, reducing complexity and potential for errors.
- **Maintainability**: Modules minimize interdependency, allowing easier updates and teamwork.
- **Reusability**: Well-defined modules can be reused across different parts of the application.
- **Scoping**: Each module has its own namespace, preventing name conflicts.

Python modules and packages are key tools for organizing and structuring code efficiently.

---

---

**Note on Python Modules: Overview**

Python modules are a fundamental part of modular programming. They allow developers to separate code into independent, reusable units. In Python, a module is simply a file containing Python definitions and statements, saved with a `.py` extension.

### Three Types of Modules in Python:

1. **Written in Python** – The most common and easiest to create. Just write valid Python code in a file with a `.py` extension.
2. **Written in C and dynamically loaded** – These are compiled modules loaded at runtime, like the `re` (regular expression) module.
3. **Built-in modules** – These are embedded in the Python interpreter itself, such as `itertools`.

Despite the differences, all modules are used in the same way via the `import` statement.

### Creating a Python Module

To create a basic Python module:

- Write code in a file, e.g., `mod.py`
- Example content:
  ```python
  s = "If Comrade Napoleon says it, it must be right."
  a = [100, 200, 300]

  def foo(arg):
      print(f'arg = {arg}')

  class Foo:
      pass
  ```

This module defines:

- `s`: a string object
- `a`: a list
- `foo()`: a function
- `Foo`: a class

### Accessing Module Contents

Once the module is saved and located in a directory that Python can find, it can be imported and used like this:

```python
>>> import mod
>>> print(mod.s)
If Comrade Napoleon says it, it must be right.

>>> mod.a
[100, 200, 300]

>>> mod.foo(['quux', 'corge', 'grault'])
arg = ['quux', 'corge', 'grault']

>>> x = mod.Foo()
>>> x
<mod.Foo object at 0x03C181F0>
```

### Summary

- Python modules simplify code organization.
- They are easy to create and use.
- All module types—Python, C extension, and built-in—are accessed the same way.
- A module can define variables, functions, and classes that can be imported and reused.

---

---

### 🧭 Python Module Search Path – Notes

When you use `import mod` in your script, Python looks for the `mod.py` file by searching through a list of directories, in this order:

#### 1. Current Script Directory

- Python first checks the folder where the script you're running is located.
- If you're in the Python interactive shell, it checks the current working directory.

#### 2. `PYTHONPATH` Environment Variable

- If set, this variable lists additional directories to search for modules.
- It mimics your system's `PATH` variable (platform-dependent syntax).

#### 3. Default Installation Directories

- These are set when Python is installed and include:
  - The standard library directory
  - The `site-packages` directory for third-party packages

#### 🛠️ View the Search Path

You can inspect the full search path using:

```python
import sys
print(sys.path)
```

Example output:

```python
['',
 'C:\\Users\\john\\Documents\\Python\\doc',
 'C:\\Python36\\Lib\\idlelib',
 'C:\\Python36\\python36.zip',
 'C:\\Python36\\DLLs',
 'C:\\Python36\\lib',
 'C:\\Python36',
 'C:\\Python36\\lib\\site-packages']
```

> ⚠️ This list is installation-specific. Yours may look different.

---

### ✅ How to Ensure Python Finds Your Module

You can make sure your `mod.py` is found by doing **one** of the following:

- Place `mod.py` in the same directory as your script
- Add its path to the `PYTHONPATH` environment variable
- Move `mod.py` into a directory already in `sys.path`
- Add the module’s folder dynamically at runtime:

```python
import sys
sys.path.append(r'C:\Users\john')  # or any valid path
import mod
```

---

### 📁 Finding the Imported Module’s Location

Once imported, you can find where Python loaded the module from:

```python
print(mod.__file__)
```

Example:

```python
'C:\\Users\\john\\mod.py'
```

Built-in modules will also show their file paths, e.g.:

```python
import re
print(re.__file__)
# 'C:\\Python36\\lib\\re.py'
```

---

---

# 📚 Understanding the `import` Statement in Python – Step-by-Step Guide

The `import` statement in Python is used to bring code from another module (a `.py` file) into your program. It allows you to reuse functions, variables, and classes defined elsewhere.

---

## 🔹 1. Basic Import

### Syntax:

```python
import <module_name>
```

This is the simplest and most common way to import a module.

### Example:

```python
import mod
```

Now, the name `mod` is available in your program. But, the contents like functions or variables inside `mod` are **not directly accessible**. You must access them using the module name as a prefix:

```python
mod.s
mod.foo("quux")
```

Trying to access them without the `mod.` prefix will cause an error:

```python
s              # ❌ NameError
foo("quux")    # ❌ NameError
```

---

## 🔹 2. Importing Multiple Modules

You can import more than one module at once by separating them with commas:

```python
import os, sys, mod
```

This imports all three modules.

---

## 🔹 3. Importing Specific Objects

### Syntax:

```python
from <module_name> import <name1>, <name2>, ...
```

This allows you to bring specific items (like variables or functions) into your program **without needing the module prefix**.

### Example:

```python
from mod import s, foo
```

Now, you can use `s` and `foo` directly:

```python
print(s)           # ✅ Works
foo("quux")        # ✅ Works
```

If you do:

```python
from mod import Foo
x = Foo()
print(x)
```

You’ll get:

```plaintext
<mod.Foo object at 0x02E3AD50>
```

---

## 🔹 4. Overwriting Local Names

If you already have a variable named `a`, and then import `a` from the module, it will be replaced:

```python
a = ['foo', 'bar', 'baz']
print(a)   # ['foo', 'bar', 'baz']

from mod import a
print(a)   # [100, 200, 300]  # Overwritten!
```

---

## 🔹 5. Importing Everything

### Syntax:

```python
from <module_name> import *
```

This imports **all objects** from the module into the local scope (except names that start with `_`).

### Example:

```python
from mod import *
```

Now you can access everything directly:

```python
print(s)
print(a)
foo("test")
Foo()
```

⚠️ **Caution**: This is not recommended for big projects, as it can accidentally overwrite variables and make code harder to understand. It’s okay for quick testing in an interactive shell.

---

## 🔹 6. Using Aliases for Imported Names

### A. Rename specific objects

```python
from mod import s as string, a as alist
```

Now:

```python
print(string)   # 'If Comrade Napoleon says it, it must be right.'
print(alist)    # [100, 200, 300]
```

You avoid name conflicts this way:

```python
s = "foo"
a = ["foo", "bar", "baz"]
# After import:
# s and a are still intact
# string and alist are used for imported values
```

### B. Rename the whole module

```python
import mod as my_module
```

Now access contents using `my_module`:

```python
my_module.a
my_module.foo("qux")
```

---

## 🔹 7. Importing Inside a Function

You can import specific parts of a module inside a function:

```python
def bar():
    from mod import foo
    foo("corge")

bar()
# Output: arg = corge
```

🚫 But you **cannot** use `from mod import *` inside a function:

```python
def bar():
    from mod import *  # ❌ SyntaxError

# Python 3 does not allow this
```

---

## 🔹 8. Handling Import Errors Gracefully

### A. Importing a non-existent module:

```python
try:
    import baz  # Module does not exist
except ImportError:
    print("Module not found")
```

### B. Importing a missing object from a valid module:

```python
try:
    from mod import baz  # Object not in mod
except ImportError:
    print("Object not found in module")
```

This helps prevent crashes if something is missing.

---

## ✅ Summary Table

| Syntax                        | What It Does                                        |
| ----------------------------- | --------------------------------------------------- |
| `import mod`                  | Imports the module. Use as `mod.s`, `mod.foo()`     |
| `import mod1, mod2`           | Imports multiple modules                            |
| `from mod import s, foo`      | Brings specific items directly into local namespace |
| `from mod import *`           | Brings all names (except those starting with `_`)   |
| `from mod import s as string` | Imports `s` as `string`                             |
| `import mod as mymod`         | Imports whole module under new name                 |
| `try ... except ImportError`  | Prevents crashes if import fails                    |

---

---

---

# 🔍 Understanding the `dir()` Function in Python

The built-in `dir()` function helps you **explore the current namespace** (or the contents of a module). It returns a **sorted list of names** (variables, functions, classes, etc.) that are currently defined.

---

## 🔹 1. Using `dir()` Without Arguments

When you call `dir()` with **no arguments**, it shows the names in the **current local scope** (the local symbol table).

### Example:

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__']
```

These are automatically defined when Python starts — they are built-in or internal names.

---

### Defining a Variable Adds It to the Namespace

```python
>>> qux = [1, 2, 3, 4, 5]
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'qux']
```

The name `qux` now appears in the list.

---

### Defining a Class and Creating an Object

```python
>>> class Bar():
...     pass

>>> x = Bar()
>>> dir()
['Bar', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'qux', 'x']
```

Both the class `Bar` and the instance `x` appear in the list.

---

## 🔹 2. `dir()` Helps Track What Was Added by Imports

This is handy for checking what changes when you import something.

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__']
```

Now, import a module:

```python
>>> import mod
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'mod']
```

✅ The name `mod` is added to the namespace.

---

### Accessing Contents of the Imported Module

```python
>>> mod.s
'If Comrade Napoleon says it, it must be right.'
>>> mod.foo([1, 2, 3])
arg = [1, 2, 3]
```

---

## 🔹 3. Importing Specific Items Adds Them Directly

```python
>>> from mod import a, Foo
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'a', 'mod']
```

Now `a` and `Foo` are directly in the local namespace — no need for `mod.` prefix.

```python
>>> a
[100, 200, 300]
>>> x = Foo()
>>> x
<mod.Foo object at 0x002EAD50>
```

---

### Using Aliases for Imports

```python
>>> from mod import s as string
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'a', 'mod', 'string', 'x']
>>> string
'If Comrade Napoleon says it, it must be right.'
```

Now the string `s` is available as `string`.

---

## 🔹 4. Using `dir()` with a Module as Argument

You can inspect the **contents of a module** directly by passing it to `dir()`.

```python
>>> import mod
>>> dir(mod)
['Foo', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__', 'a', 'foo', 's']
```

This lists all the names that are defined inside `mod`.

---

## 🔹 5. After `from mod import *`

This imports **all non-private names** from the module into the current namespace.

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__']

>>> from mod import *
>>> dir()
['Foo', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
 '__package__', '__spec__', 'a', 'foo', 's']
```

Now `Foo`, `a`, `foo`, and `s` are directly available.

---

## ✅ Summary

| Usage                     | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `dir()`                   | Lists names in the current local scope         |
| `dir(mod)`                | Lists names defined inside the module `mod`    |
| After `import mod`        | Adds `mod` to your namespace                   |
| After `from mod import x` | Adds `x` directly to your namespace            |
| After `from mod import *` | Adds all public names from `mod` to your scope |

---

---

---

---

---

````markdown
# 🐍 Executing a Module as a Script

In Python, any `.py` file that contains a module can also be executed as a standalone script. This flexibility allows Python modules to be tested directly, or used as reusable components.

---

## 🔹 1. Basic Python Module

Consider the following module `mod.py`:

```python
# mod.py

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
```
````

You can execute this module like a regular script by running the following command:

```bash
C:\Users\john\Documents>python mod.py
C:\Users\john\Documents>
```

### Output:

There is no visible output because the module only defines variables, a function, and a class. It doesn't perform any operations.

---

## 🔹 2. Modifying the Module to Generate Output

Now, let's add some code to generate output when the module is executed as a script:

```python
# mod.py

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print(s)
print(a)
foo('quux')
x = Foo()
print(x)
```

### Running the Script:

```bash
C:\Users\john\Documents>python mod.py
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x02F101D0>
```

The script now produces output, but when the module is imported, it also generates unwanted output:

### Importing the Module:

```python
>>> import mod
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<mod.Foo object at 0x0169AD50>
```

This is not typical behavior for a module, as it should not produce output upon import.

---

## 🔹 3. Distinguishing Between Module Import and Script Execution

You can prevent unwanted output by using the `__name__` special variable.

- When a module is **imported**, `__name__` is set to the module’s name.
- When a module is **run as a script**, `__name__` is set to `'__main__'`.

You can check this with an `if` statement to alter the behavior depending on how the file is executed.

### Modified `mod.py`:

```python
# mod.py

s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)
```

### Running the Script:

```bash
C:\Users\john\Documents>python mod.py
Executing as standalone script
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = quux
<__main__.Foo object at 0x03450690>
```

Now, when run as a script, the program outputs the expected information.

### Importing the Module:

```python
>>> import mod
>>> mod.foo('grault')
arg = grault
```

The module now **does not** generate output upon import, but you can still use its contents like the `foo()` function.

---

## 🔹 4. Unit Testing with `__name__ == '__main__'`

This pattern is often used for **unit testing** modules, where you can run the module as a standalone script to test its functionality.

Consider the following example where we create a simple factorial function in `fact.py`:

```python
# fact.py

def fact(n):
    return 1 if n == 1 else n * fact(n-1)

if (__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))
```

### Importing the Function:

You can import and use the `fact()` function in other scripts or Python interactive sessions:

```python
>>> from fact import fact
>>> fact(6)
720
```

### Running as a Standalone Script:

Alternatively, you can execute it directly from the command line, passing an argument to test the functionality:

```bash
C:\Users\john\Documents>python fact.py 6
720
```

---

## ✅ Summary

| Behavior                     | Description                                               |
| ---------------------------- | --------------------------------------------------------- |
| `if __name__ == '__main__':` | Distinguishes between module import and script execution  |
| Running as a script          | Executes the code block under `if __name__ == '__main__'` |
| Importing as a module        | Does not execute code inside `if __name__ == '__main__'`  |

```


```

## Reloading

The concept of **reloading a module** in Python refers to re-importing a module after it has already been imported in the current interpreter session. This can be useful when you've made changes to a module's code and you want to see those changes reflected without restarting the entire interpreter.

### Key Points to Understand:

1. **Modules are loaded only once per session**:  
   When you import a module in Python, it is loaded only once during that session. Any subsequent imports of the same module do not cause the module to be re-executed. Instead, Python simply reuses the already-loaded module.

   **Example:**

   ```python
   # mod.py
   a = [100, 200, 300]
   print('a =', a)

   >>> import mod
   a = [100, 200, 300]
   >>> import mod  # No print statement here
   >>> import mod  # No print statement here
   >>> mod.a  # [100, 200, 300]
   ```

   In the example above, when `mod.py` is imported the first time, the print statement `print('a =', a)` is executed. But on subsequent imports, the print statement doesn't run because Python doesn't reload the module. It just references the already-loaded module.

2. **How to reload a module**:  
   If you make changes to a module (like adding new functions or modifying the code), and you want to see those changes without restarting the interpreter, you need to **reload** the module.

   Python's standard library provides the `importlib` module to allow for reloading a module.

   **Example:**

   ```python
   >>> import mod
   >>> import importlib
   >>> importlib.reload(mod)
   ```

   - First, `import mod` loads the module.
   - Then, by calling `importlib.reload(mod)`, the module `mod` is reloaded, meaning any changes made to the `mod.py` file (like modifying variables or adding functions) will take effect.

   **What happens during reloading**:

   - The module is re-executed, so any changes (like new assignments or print statements) will be run again.
   - The contents (functions, classes, variables) of the module are updated in memory.
   - The print statement or other side effects of module execution will happen again, but this is usually something you want only for reloading purposes.

   **Example in action**:

   ```python
   # mod.py
   a = [100, 200, 300]
   print('a =', a)

   >>> import mod
   a = [100, 200, 300]
   >>> import mod  # No print here
   >>> import importlib
   >>> importlib.reload(mod)  # This will print 'a = [100, 200, 300]' again
   a = [100, 200, 300]
   ```

3. **Why Reloading Might Be Needed**:

   - **Testing changes**: During development, you may need to test changes you make to a module while keeping the current interpreter session active.
   - **Avoiding interpreter restart**: Instead of restarting the Python interpreter every time you modify a module, reloading allows you to refresh the module’s content dynamically.
   - **Interactive development**: In environments like interactive shells or notebooks, where you are making small iterative changes, reloading saves time by applying changes without restarting.

### Important Considerations:

- **Reloading does not clear state**: If your module defines classes, functions, or variables that are used elsewhere, reloading does not reset those objects to their initial state. It only updates the module’s code and rebinds variables in the module's namespace.
- **Limitations**: Some changes (like changes to the module’s import statements) may not take effect properly with a reload. In such cases, restarting the interpreter may be necessary.

### Summary:

- **Normal imports**: Python loads the module only once.
- **Reloading**: If you make changes to a module and need to see them immediately, use `importlib.reload(module_name)` to reload it.
- **Use case**: Ideal for interactive sessions, debugging, or testing where you want to dynamically update the module’s behavior without restarting Python.

---

---

---

## 🧠 What Happens When You Run `import mod`?

You are telling Python:

> "Hey, find a file named `mod.py` and load it as a module."

But Python needs to **look somewhere** to find that file.

---

## 🔍 Where Does Python Look?

Python checks a **list of folders** called the **module search path**. That list is stored in a special variable: `sys.path`.

You can see it by typing this in the Python shell:

```python
import sys
print(sys.path)
```

You'll see something like:

```python
['', 'C:\\Users\\john\\Documents\\Python\\doc', 'C:\\Python36\\Lib\\idlelib',
'C:\\Python36\\python36.zip', 'C:\\Python36\\DLLs', 'C:\\Python36\\lib',
'C:\\Python36', 'C:\\Python36\\lib\\site-packages']
```

Each item in this list is a **folder** where Python will **look for your module**.

---

## ✅ How Python Builds This List

Python builds the search path (`sys.path`) using these sources:

1. **Current directory** (where your script is or where you're running Python).
2. **PYTHONPATH** environment variable (if you set it).
3. **Standard library directories** (built into your Python installation).
4. **Site-packages directory** (where installed packages like `numpy` live).

---

## 👨‍🏫 Example

Let's say you have this file:

```
C:\Users\john\mod.py
```

But you're running your script from:

```
C:\Users\john\Documents\Python\doc\main.py
```

If you do:

```python
import mod
```

❌ Python **won’t find `mod.py`**, because it’s not in any of the folders listed in `sys.path`.

---

## 🛠 How to Fix This?

You have 5 options:

### ✅ Option 1: Move `mod.py` into the same folder as your script

```text
C:\Users\john\Documents\Python\doc\
├── main.py
├── mod.py
```

### ✅ Option 2: Add the path to `mod.py` to `PYTHONPATH`

On Windows Command Prompt:

```bash
set PYTHONPATH=C:\Users\john
python main.py
```

### ✅ Option 3: Put `mod.py` in a directory already in `sys.path`

(e.g., `C:\Python36\Lib\site-packages`)

### ✅ Option 4: Modify `sys.path` at runtime in your script

```python
import sys
sys.path.append(r'C:\Users\john')

import mod
```

### ✅ Option 5: Install it as a package (advanced, for later)

---

## 🔎 How to Check Where a Module Came From?

After importing, you can ask Python:

```python
import mod
print(mod.__file__)
```

This shows the **exact file path** where Python found the module.

---

## 🧪 Bonus Example:

```python
import sys
print(sys.path)

# Add a custom directory
sys.path.append(r"C:\Users\john")

import mod
print(mod.__file__)
```

---

## 🧠 Summary

| Concept        | Meaning                                                 |
| -------------- | ------------------------------------------------------- |
| `sys.path`     | List of places Python looks for modules                 |
| `PYTHONPATH`   | Lets you add folders to `sys.path` before Python starts |
| `mod.__file__` | Tells you exactly where the module was loaded from      |

---
