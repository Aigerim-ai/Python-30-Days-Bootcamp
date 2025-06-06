**Object-Oriented Programming (OOP)** in Python is a programming paradigm based on the concept of **objects**, which are instances of **classes**. It allows you to structure your code by bundling data (attributes) and behavior (methods) together.

---

### 🔑 **Key Concepts of OOP in Python**

#### 1. **Class**

A class is a blueprint for creating objects. It defines attributes and methods.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")
```

#### 2. **Object (Instance)**

An object is an instantiation of a class. It has real values in its attributes and can use its methods.

```python
my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
```

#### 3. **Encapsulation**

It means hiding the internal state of an object and requiring all interaction through methods.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

#### 4. **Inheritance**

A class can inherit from another class to reuse its code.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow")
```

#### 5. **Polymorphism**

Different classes can define methods with the same name but different behavior.

```python
animals = [Dog("Max"), Cat()]
for animal in animals:
    animal.speak()  # Dog: woof, Cat: meow
```

---

### ✅ **Why Use OOP in Python?**

- **Modularity**: Code is organized into classes and objects.
- **Reusability**: Inheritance allows code reuse.
- **Scalability**: Easy to manage and scale.
- **Maintainability**: Encapsulation improves code readability and security.

---

Defining a class in Python is straightforward. You use the `class` keyword followed by the class name and a colon. Inside the class, you define methods (functions) and attributes (variables) that belong to the class.

---

### Basic Syntax to Define a Class:

```python
class ClassName:
    # class body: attributes and methods
    pass
```

The `pass` statement is just a placeholder if you don't want to define anything yet.

---

### Example: Defining a Simple Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def bark(self):
        print(f"{self.name} says woof!")
```

---

### Explanation:

- `class Dog:` — defines a new class named `Dog`.
- `def __init__(self, name, age):` — special method called a **constructor** that initializes the object when created.
  - `self` refers to the current instance of the class.
  - `self.name` and `self.age` are attributes assigned when you create an object.
- `def bark(self):` — a method that belongs to the class and can be called on instances.

---

### Creating an Object (Instance) of the Class:

```python
my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!
```

---

Great! Let's clarify the difference between **Classes** and **Instances**, and then review **Class Definition**.

---

## Classes vs Instances

| **Class**                                         | **Instance (Object)**                                                                    |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| A blueprint or template for creating objects.     | A specific object created from a class.                                                  |
| Defines attributes (data) and methods (behavior). | Has actual values for attributes defined by the class.                                   |
| Exists only once in your code.                    | Multiple instances can be created from one class.                                        |
| Example: `Dog` class defines what a dog is.       | Example: `my_dog = Dog("Buddy")` is an instance representing a specific dog named Buddy. |

---

### Example:

```python
# Class definition (blueprint)
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

# Creating instances (objects) from the class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # Buddy says woof!
dog2.bark()  # Max says woof!
```

- `Dog` is the **class**.
- `dog1` and `dog2` are two **instances** of that class, each with their own `name`.

---

## Class Definition Recap

```python
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = parameter

    def method_name(self):
        # Behavior of the class
        pass
```

- Use `class` keyword followed by the class name (capitalized by convention).
- `__init__` is the constructor method to initialize new instances.
- `self` represents the instance being created or used.

---

Instantiating a class in Python means **creating an object (instance)** from that class.

---

### How to Instantiate a Class

1. Write the class name followed by parentheses `()`.
2. If the class constructor (`__init__`) requires arguments, provide them inside the parentheses.

---

### Example

Given this class:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")
```

You instantiate (create) an object like this:

```python
my_dog = Dog("Buddy", 3)
```

Here:

- `Dog` is the class.
- `"Buddy"` and `3` are arguments passed to `__init__`.
- `my_dog` is an instance of the class `Dog`.

---

### Using the Instance

```python
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!
```

---

**Summary:**

```python
instance_name = ClassName(arguments_if_any)
```

Let's break down **Class Attributes**, **Instance Attributes**, and **Instance Methods** clearly:

---

## 1. Class Attributes

- Attributes that belong to the **class itself**, shared by **all instances**.
- Defined directly inside the class, outside any methods.
- Useful for properties common to all instances.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name):
        self.name = name          # Instance attribute
```

All `Dog` instances share the same `species` value.

```python
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
```

---

## 2. Instance Attributes

- Attributes unique to each instance.
- Usually set inside the `__init__` method using `self`.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # Instance attribute
        self.age = age     # Instance attribute
```

Each dog has its own `name` and `age`.

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Buddy
print(dog2.name)  # Max
```

---

## 3. Instance Methods

- Functions defined inside the class that operate on instances.
- The first parameter is always `self`, which refers to the specific instance.
- Can access and modify instance attributes.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):  # Instance method
        print(f"{self.name} says woof!")
```

Calling the method on an instance:

```python
dog = Dog("Buddy")
dog.bark()  # Buddy says woof!
```

---

### Summary:

| Concept                | Defined Where                  | Shared or Unique?         | Access via                                    |
| ---------------------- | ------------------------------ | ------------------------- | --------------------------------------------- |
| **Class Attribute**    | Inside class, outside methods  | Shared by all instances   | `ClassName.attribute` or `instance.attribute` |
| **Instance Attribute** | Inside `__init__` via `self`   | Unique to each instance   | `instance.attribute`                          |
| **Instance Method**    | Inside class with `self` param | Operates on instance data | `instance.method()`                           |

---

Inheriting from another class in Python means creating a **new class** (called a **child** or **subclass**) that **reuses, extends, or modifies** the behavior of an existing class (called the **parent** or **base class**).

---

### How to Inherit from a Class in Python

You specify the parent class inside parentheses after the child class name.

```python
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
```

---

### Example

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog says woof!")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print("Cat says meow!")
```

---

### Using the Classes

```python
dog = Dog()
dog.speak()  # Output: Dog says woof!

cat = Cat()
cat.speak()  # Output: Cat says meow!
```

---

### Key Points:

- The child class automatically has access to **all methods and attributes** of the parent class (unless overridden).
- You can **override** parent methods by defining a method with the same name in the child class.
- You can still call the parent’s method explicitly using `super()`.

---

### Calling Parent Method with `super()`

```python
class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Animal's speak()
        print("Dog says woof!")
```

```python
dog = Dog()
dog.speak()
# Output:
# Animal makes a sound
# Dog says woof!
```

---

Inheriting from another class in Python means creating a **new class** (called a **child** or **subclass**) that **reuses, extends, or modifies** the behavior of an existing class (called the **parent** or **base class**).

---

### How to Inherit from a Class in Python

You specify the parent class inside parentheses after the child class name.

```python
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
```

---

### Example

```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog says woof!")

class Cat(Animal):  # Cat inherits from Animal
    def speak(self):
        print("Cat says meow!")
```

---

### Using the Classes

```python
dog = Dog()
dog.speak()  # Output: Dog says woof!

cat = Cat()
cat.speak()  # Output: Cat says meow!
```

---

### Key Points:

- The child class automatically has access to **all methods and attributes** of the parent class (unless overridden).
- You can **override** parent methods by defining a method with the same name in the child class.
- You can still call the parent’s method explicitly using `super()`.

---

### Calling Parent Method with `super()`

```python
class Dog(Animal):
    def speak(self):
        super().speak()  # Calls Animal's speak()
        print("Dog says woof!")
```

```python
dog = Dog()
dog.speak()
# Output:
# Animal makes a sound
# Dog says woof!
```

---
