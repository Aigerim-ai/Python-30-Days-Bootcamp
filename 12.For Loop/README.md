### 🌟 What is a Loop?

A **loop** is a way to make the computer **repeat something** — a task or a block of code — again and again **without writing it multiple times**.

Think of it like this:

> Imagine you want to clap 5 times. You could say:
>
> - Clap
> - Clap
> - Clap
> - Clap
> - Clap

But with a loop, you’d say:

> - **Repeat "Clap" 5 times**

Much shorter, and more flexible if you want to change the number!

---

### 🧠 Why Use Loops?

- To **repeat tasks** automatically
- To go through items in a list (like all names in your contact list).
- To do something until a certain **condition is met** (like “keep asking until they say yes”).

---

### 🔄 Two Common Types of Loops:

#### 1. **For Loop** — Think: "Do this _for_ each thing"

You use it when you **know how many times** you want to repeat something.

> Example idea (not code):  
> Say "Hi" to each friend in a list of 5 friends.

#### 2. **While Loop** — Think: "Do this _while_ a condition is true"

You use it when you **don’t know how many times**, but you know the condition.

> Example idea (not code):  
> Keep asking "Are we there yet?" **while** the answer is "No".

---

### 💡 The Big Idea

Loops save time and make your code **cleaner, smarter, and less repetitive**.

---

---

### 🔁 What is a `for` loop?

A **`for` loop** lets you **repeat** a block of code **for each item in a group** (like a list, a string, or a range of numbers).

---

### 🧠 Think of it like this:

> Imagine you have a basket with 3 fruits: 🍎, 🍌, 🍇  
> You want to pick up each one and say its name.

You can say:

- This is an apple
- This is a banana
- This is a grape

But with a `for` loop, Python can do:

> “**For each fruit in the basket, say its name**”

---

### 📚 In Python, the format looks like this:

```python
for item in group:
    do something with item
```

Let’s break that down:

- **`item`** – a temporary name for each thing in the group (like a fruit)
- **`group`** – the collection of things you’re looping over (like a list)
- **Indented block** – the code that runs each time

---

### 🍓 Example in words:

If you have:

- A list of fruits: `["apple", "banana", "cherry"]`

You can loop through them and say:

- “This is an apple”
- “This is a banana”
- “This is a cherry”

---

---

### 🍓 Example: Loop through a list of fruits

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("This is a", fruit)
```

---

### 🔍 What’s happening here?

1. We created a list called `fruits` with 3 items.
2. The `for` loop says:

   > "For each **fruit** in the list **fruits**, do the next step."

3. On each loop, the `fruit` variable takes one value from the list.
4. The `print()` function runs, showing the current fruit.

---

### 🖨️ Output:

```
This is a apple
This is a banana
This is a cherry
```

Pretty cool, right? Python automatically goes through the list for you — one item at a time!

---

## Examples

---

## 🧠 1. Looping Over a List

We already did this one, but here’s another example with a twist:

```python
colors = ["red", "green", "blue"]
for color in colors:
    print(f"I like the color {color}")
```

### Output:

```
I like the color red
I like the color green
I like the color blue
```

---

## 🔢 2. Looping Over Numbers with `range()`

```python
for num in range(5):
    print("Number is:", num)
```

### Output:

```
Number is: 0
Number is: 1
Number is: 2
Number is: 3
Number is: 4
```

> `range(5)` gives you numbers from 0 to 4 (not including 5).

You can also customize the start, stop, and step:

```python
for i in range(1, 10, 2):
    print(i)
```

### Output:

```
1
3
5
7
9
```

---

## 📝 3. Looping Over a String (character by character)

```python
word = "hello"
for letter in word:
    print(letter)
```

### Output:

```
h
e
l
l
o
```

---

## 📈 4. Summing Numbers in a List

```python
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num

print("Total is:", total)
```

### Output:

```
Total is: 100
```

---

## 📦 5. Looping with `enumerate()` (Get index + value)

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

### Output:

```
0: Alice
1: Bob
2: Charlie
```

---

## ✅ 6. Filtering with `if` inside a loop

```python
numbers = [1, 4, 7, 10, 13]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
```

### Output:

```
4 is even
10 is even
```

---

---
