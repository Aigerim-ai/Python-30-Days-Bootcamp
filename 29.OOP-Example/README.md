# 🧾 Building a Payroll System With Python Inheritance

When building complex software systems like HR or payroll platforms, you often encounter scenarios where different entities share common features but also have unique behaviors. In such cases, **object-oriented programming (OOP)** and **class inheritance** can help you structure your code in a clean, reusable, and extensible way.

In this blog post, we’ll walk through creating a simple **payroll system** in Python. Along the way, you’ll learn how to:

- Define a class hierarchy
- Use inheritance to avoid code duplication
- Implement polymorphism through a shared interface
- Convert a base class into an abstract class to enforce implementation consistency

---

## 🎯 The Goal

We're going to design a payroll system that supports multiple types of employees:

- **Salaried employees**: Get a fixed weekly salary.
- **Hourly employees**: Get paid based on the number of hours worked.
- **Commissioned employees**: Earn a base salary plus commission.

Each employee must implement a `calculate_payroll()` method so the system can determine their pay.

---

## 🧱 Step 1: Create the Payroll System

First, we define a `PayrollSystem` class responsible for processing payroll for all employees:

```python
class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")
```

This method iterates over a list of employees and calls each one’s `calculate_payroll()` method. But how do we make sure each employee type has this method?

---

## 👪 Step 2: Define the Employee Base Class

We’ll start with a base class `Employee` that holds the common attributes:

```python
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

This defines a blueprint every employee must follow. But there’s no `calculate_payroll()` method here—yet.

---

## 💼 Step 3: Implement Employee Types

Now let’s add the specialized employee classes that inherit from `Employee` and implement their own `calculate_payroll()` logic.

### 🧍‍♂️ Salaried Employees

```python
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
```

### 🛠 Hourly Employees

```python
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
```

### 💰 Commission Employees

```python
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
```

Note: `CommissionEmployee` inherits from `SalaryEmployee` instead of `Employee` because both types share the `weekly_salary` attribute.

---

## 🚀 Step 4: Run the Program

Let’s tie everything together in `program.py`:

```python
import hr

salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr.HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = hr.CommissionEmployee(3, "Kevin Bacon", 1000, 250)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee]
)
```

### 🖥 Output:

```
Calculating Payroll
===================
Payroll for: 1 - John Smith
- Check amount: 1500

Payroll for: 2 - Jane Doe
- Check amount: 600

Payroll for: 3 - Kevin Bacon
- Check amount: 1250
```

Boom! Payroll processed.

---

## 💥 What If You Forget to Implement `calculate_payroll()`?

If you accidentally pass a plain `Employee` object to the system, you’ll get an error:

```python
employee = Employee(1, "Invalid")
payroll_system.calculate_payroll([employee])
```

```text
AttributeError: 'Employee' object has no attribute 'calculate_payroll'
```

This happens because the base class doesn’t implement `calculate_payroll()`.

---

## 🧩 Step 5: Make the Base Class Abstract

To prevent such mistakes, you can make `Employee` an **abstract base class** using the `abc` module:

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass
```

Now Python will enforce that any subclass of `Employee` **must** implement `calculate_payroll()`, and you won’t be able to instantiate `Employee` directly.

---

## 📊 UML Class Diagram Overview

Here’s a simple visual representation of the hierarchy:

```
        [ Employee ] (abstract)
              ↑
    ┌─────────┼─────────┐
    │         │         │
[Salary] [Hourly] [Commission]
                    ↑
                (inherits Salary)
```

---

## 🧠 Key Takeaways

- Use inheritance to represent a hierarchy of related classes.
- Abstract base classes help enforce consistent behavior.
- Polymorphism lets you treat different employee types the same way in your payroll system.
- `super()` lets you reuse and extend base class functionality cleanly.

---

By using inheritance, you’ve built a flexible, extensible payroll system with minimal duplication and maximum clarity. As your HR system grows, adding new types of employees (like freelancers or interns) will be as easy as creating a new class and implementing `calculate_payroll()`.

Happy coding! 🐍💼

---

# Implementing Class Hierarchies in Python: An HR System Example

This example demonstrates how to use inheritance to create a hierarchy of employee classes for a payroll system. Let's break down the key concepts:

## Base Class: Employee

```python
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

The `Employee` class serves as the base class with:

- Common attributes: `id` and `name` for all employees
- No implementation of `calculate_payroll()` (making it incomplete)

## Derived Employee Classes

### 1. SalaryEmployee (Fixed Weekly Salary)

```python
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
```

### 2. HourlyEmployee (Paid by Hour)

```python
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
```

### 3. CommissionEmployee (Salary + Commission)

```python
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
```

## Payroll System

```python
class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")
```

## Key Design Principles Illustrated:

1. **Inheritance Hierarchy**:

   ```
   Employee
   ├── SalaryEmployee
   │   └── CommissionEmployee
   └── HourlyEmployee
   ```

2. **Method Overriding**: Each derived class implements its own version of `calculate_payroll()`

3. **Code Reuse**: Using `super()` to access base class functionality

4. **Polymorphism**: The payroll system can process any employee type uniformly

5. **Liskov Substitution Principle**: Derived classes can substitute the base class

## Current Limitations:

1. The base `Employee` class is concrete but incomplete (missing `calculate_payroll()`)
2. Nothing prevents creating direct `Employee` instances that will fail at runtime
3. No formal interface enforcement (Python uses duck typing)

## UML Representation:

```
┌──────────────────┐       ┌──────────────────┐
│   PayrollSystem  │       │    Employee      │
└────────┬─────────┘       └────────┬─────────┘
         │ uses                     △
         │                   _______│_______
         │                  │               │
┌────────▼─────────┐  ┌─────▼─────┐  ┌─────▼─────┐
│IPayrollCalculator│  │SalaryEmpl.│  │HourlyEmpl.│
└──────────────────┘  └─────┬─────┘  └───────────┘
                            △
                            │
                     ┌──────▼──────┐
                     │CommissionEmp│
                     └─────────────┘
```

This design shows how inheritance allows creating specialized employee types while maintaining a common interface for payroll processing. The next step would be to make `Employee` an abstract base class to prevent direct instantiation and enforce implementation of `calculate_payroll()` in derived classes.
