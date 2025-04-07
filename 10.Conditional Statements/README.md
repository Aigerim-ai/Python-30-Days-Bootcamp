# Conditional Statements in Python: A Beginner's Guide

Conditional statements are one of the most important concepts in programming. They allow your program to make decisions and take different actions based on certain conditions. In Python, we use `if`, `elif`, and `else` to create these conditional statements. This tutorial will explain how each of them works with easy-to-understand examples.

## What are Conditional Statements?

In simple terms, conditional statements allow your program to check whether something is true or false, and then decide what to do next based on that.

For example:

- If a number is greater than 10, print "High".
- If a number is less than or equal to 10, print "Low".

The condition we check can either be **True** or **False**. Depending on that, the program takes one action or another.

Let's break down the three main types of conditional statements in Python: `if`, `elif`, and `else`.

---

## The `if` Statement

The `if` statement is the most basic form of a conditional statement. It checks whether a condition is **True**. If the condition is True, the program runs the code inside the `if` block. If the condition is False, it skips the code inside the `if` block.

### Syntax:

```python
if condition:
    # Code to run if the condition is True
```

### Example:

Let’s look at an example where we check if a number is greater than 5:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

In this case, since `x = 10` and `10 > 5` is **True**, the program will print:

```
x is greater than 5
```

---

## The `elif` Statement

Sometimes, you may want to check multiple conditions. This is where `elif` comes in. `elif` stands for "else if". It checks another condition if the previous `if` or `elif` condition was **False**.

### Syntax:

```python
if condition1:
    # Code to run if condition1 is True
elif condition2:
    # Code to run if condition2 is True
elif condition3:
    # Code to run if condition3 is True
else:
    # Code to run if none of the above conditions are True
```

### Example:

Let’s say we want to check if a number is greater than 15, greater than 5, or less than or equal to 5:

```python
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")
```

In this case:

- The first condition (`x > 15`) is False because `10` is not greater than `15`.
- The second condition (`x > 5`) is True because `10` is greater than `5`.

So, the program will print:

```
x is greater than 5 but not greater than 15
```

---

## The `else` Statement

The `else` statement comes after an `if` or `elif`. It is used to define a block of code that should be executed **if none of the previous conditions are True**. You can think of it as the "catch-all" block of code.

### Syntax:

```python
if condition:
    # Code to run if the condition is True
else:
    # Code to run if the condition is False
```

### Example:

Let’s check if a number is greater than 5 or not:

```python
x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

Since `x = 3` and `3 > 5` is **False**, the program will execute the `else` block and print:

```
x is not greater than 5
```

---

## Combining `if`, `elif`, and `else`

You can combine all three — `if`, `elif`, and `else` — to check multiple conditions in your program. This allows your program to make complex decisions based on many different possibilities.

### Example:

Let’s write a program that checks whether a number is positive, negative, or zero:

```python
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

Here’s how it works:

- `x > 0` is False because `x = 0`.
- `x < 0` is also False.
- Since neither condition was True, the program reaches the `else` block and prints:

```
x is zero
```

---

## More Complex Examples

### Example 1: Checking for Multiple Conditions

Let’s say we want to check if a number is even or odd. We can use the modulo operator (`%`) to check if a number is divisible by 2.

```python
x = 7

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

Since `7 % 2` is `1`, which is not equal to `0`, the program will print:

```
x is odd
```

### Example 2: Using Multiple `elif` Statements

You can check for multiple conditions with `elif` to get more detailed results. For example, checking the grade of a student:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

In this case, `score = 85` fits the second condition (`score >= 80`), so the program will print:

```
Grade: B
```

---

## Conclusion

Conditional statements are a powerful tool that allows you to control the flow of your program based on conditions. The `if` statement checks if a condition is True, `elif` allows you to check additional conditions, and `else` provides a default action when none of the conditions are met.

As you write more complex programs, you'll often find yourself using conditional statements to make decisions and create interactive, dynamic programs. Practice using `if`, `elif`, and `else` in your own projects, and soon you'll be able to use them confidently!
