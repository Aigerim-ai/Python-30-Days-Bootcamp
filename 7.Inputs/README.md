### Tutorial: Getting Input from the User in Python

In Python, getting input from a user is simple and is commonly done using the `input()` function. This function allows us to display a prompt message to the user and capture what they type. Let’s break it down in a way that’s easy to understand.

#### 1. **Using the `input()` Function**

The basic syntax for the `input()` function is:

```python
input(prompt)
```

- `prompt` is an optional string that gets displayed to the user, telling them what kind of input you’re expecting. If you don’t specify a prompt, Python will still wait for the user to type something, but it won’t display any message.

#### 2. **Getting User Input**

Let’s start with a basic example where we ask the user for their name:

```python
name = input("What is your name? ")
print("Hello, " + name)
```

**Explanation:**

- The `input()` function shows the prompt `"What is your name?"`.
- The user types in their name (let’s say, "Vern").
- The `input()` function then returns the typed name as a **string**.
- The `print()` function prints a greeting using the name provided by the user.

Here’s what happens when you run it:

```
What is your name? Vern
Hello, Vern
```

#### 3. **Converting Input to Numbers**

A common scenario is when we need to get numeric input from the user. However, the `input()` function always returns input as a **string**. If we want to perform mathematical operations with that input, we must convert it into a number using `int()` (for integers) or `float()` (for decimal numbers).

For example, if we ask the user for their age and want to store it as a number:

```python
age = int(input("How old are you? "))
print("You are " + str(age) + " years old.")
```

**Explanation:**

- The `input()` function takes the user's input as a string.
- We use the `int()` function to **convert** that string to an integer (in this case, the user is expected to enter a whole number).
- Finally, we print the age. Since `age` is now an integer, we use `str()` to convert it back into a string for concatenation in the print statement.

Example input/output:

```
How old are you? 28
You are 28 years old.
```

#### 4. **Handling Decimal Numbers (Floats)**

If you expect the user to input a decimal (like a weight or temperature), you can use the `float()` function to convert the input into a floating-point number:

```python
weight = float(input("What is your weight in kilograms? "))
print("Your weight is " + str(weight) + " kg.")
```

**Explanation:**

- `float()` converts the string input into a decimal number.
- The `print()` statement converts `weight` back to a string to display it.

Example input/output:

```
What is your weight in kilograms? 75.5
Your weight is 75.5 kg.
```

#### 5. **Input with Default Prompt**

If you don’t want to give a specific prompt, you can simply use `input()` without any arguments:

```python
response = input()  # No prompt
print("You said: " + response)
```

This will work, but the user won’t know what you expect from them unless you tell them separately.

#### 6. **Summary of Key Points:**

- **input()**: Captures user input as a string.
- **int() and float()**: Used to convert input into numeric types.
- **String Concatenation**: When combining input with other text, remember to convert numbers back to strings using `str()`.

### Example: Full Program

Here’s a more complete example of using `input()` to interact with the user:

```python
# Asking for user's name
name = input("What is your name? ")

# Asking for user's age and converting it to an integer
age = int(input("How old are you? "))

# Asking for user's weight and converting it to a float
weight = float(input("What is your weight in kilograms? "))

# Displaying the collected information
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your weight is {weight} kg.")
```

**Expected output:**

```
What is your name? Alice
How old are you? 25
What is your weight in kilograms? 65.4
Hello, Alice!
You are 25 years old.
Your weight is 65.4 kg.
```

### Conclusion:

- The `input()` function is a simple way to get input from the user.
- You can convert the input to numbers (like integers or floats) using `int()` and `float()`.
- Always be aware that `input()` returns a string, so you must convert it when necessary.
