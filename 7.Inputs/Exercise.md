### **Exercises: Getting Input from the User in Python**

#### **Exercise 1: Basic Input and Output**

Write a Python script that:

1. Asks the user for their **first name**.
2. Asks the user for their **last name**.
3. Prints a greeting message in the format:
   ```
   Hello, [First Name] [Last Name]! Welcome to Python.
   ```

---

#### **Exercise 2: Converting String Input to Integer**

Write a Python script that:

1. Asks the user for their **birth year**.
2. Calculates their **age** (assuming the current year is 2025).
3. Prints the result in this format:
   ```
   You are [age] years old.
   ```
   📌 _Hint:_ Convert the birth year input into an integer before subtracting.

---

#### **Exercise 3: Handling Decimal Numbers**

Write a Python script that:

1. Asks the user to enter the **radius** of a circle.
2. Calculates the **area** of the circle using the formula:  
   \[
   \text{Area} = \pi \times \text{radius}^2
   \]
   (Use `3.14159` as an approximation for π).
3. Prints the result in the format:
   ```
   The area of the circle with radius [radius] is [area].
   ```
   📌 _Hint:_ Convert the radius to a float before performing calculations.

---

#### **Exercise 4: Performing Arithmetic Operations**

Write a Python script that:

1. Asks the user for two numbers.
2. Converts them into integers.
3. Computes and prints the **sum, difference, product, and quotient** of these numbers in this format:
   ```
   Sum: [sum]
   Difference: [difference]
   Product: [product]
   Quotient: [quotient]
   ```
   📌 _Hint:_ Use `int()` to convert the inputs.

---

#### **Exercise 5: Boolean Check with Membership Operator**

Write a Python script that:

1. Asks the user to enter a **word or phrase**.
2. Checks whether the word `"Python"` is present in the user’s input.
3. Prints `"Yes, your input contains 'Python'!"` if it does, otherwise print `"No, 'Python' is not found."`

---

#### **Exercise 6: Identity and Comparison Operators**

Write a Python script that:

1. Asks the user to enter **two numbers**.
2. Compares them using `==`, `!=`, `<`, and `>`.
3. Prints whether they are equal, not equal, which one is greater, or which one is smaller.

---

#### **Exercise 7: Using f-strings for Output**

Write a Python script that:

1. Asks the user for their **favorite color**.
2. Prints the response in a formatted string like this:
   ```
   Your favorite color is [color]. That's a great choice!
   ```
   📌 _Hint:_ Use an f-string (`f"Your text {variable}"`).

---

#### **Exercise 8: Full Interaction Program**

Write a Python script that interacts with the user as follows:

1. Ask for their **name**.
2. Ask for their **age** and convert it to an integer.
3. Ask for their **favorite number** and convert it to a float.
4. Print the following response:
   ```
   Hello, [name]! You are [age] years old.
   Your favorite number is [favorite number], which is interesting!
   ```
