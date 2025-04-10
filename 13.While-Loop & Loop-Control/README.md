## 🎮 What Are Loop Control Statements?

They let you:

- **Skip** parts of a loop (`continue`)
- **Stop** a loop completely (`break`)
- Do something **after the loop finishes normally** (`else` with loops)

Let’s break them down 👇

---

## 🚪 1. `break`: Exit the loop early

### 🧠 Use it when:

You want to **stop** the loop before it finishes all iterations.

```python
for num in range(1, 10):
    if num == 5:
        break
    print(num)
```

### Output:

```
1
2
3
4
```

> It **breaks** out of the loop when `num == 5`.

---

## ⏭️ 2. `continue`: Skip the current loop iteration

### 🧠 Use it when:

You want to **skip over** one specific case and continue looping.

```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```

### Output:

```
1
2
4
5
```

> It **skips** 3 and continues with the rest.

---

## 🧁 3. `else` with loops — A hidden gem!

### 🧠 Use it when:

You want to do something **after the loop finishes**, but **only if it wasn’t stopped by a `break`.**

```python
for num in range(5):
    print(num)
else:
    print("Loop finished normally!")
```

### Output:

```
0
1
2
3
4
Loop finished normally!
```

But now look at this:

```python
for num in range(5):
    if num == 3:
        break
    print(num)
else:
    print("Loop finished normally!")
```

### Output:

```
0
1
2
```

> Notice: The `else` block **does not run** because we used `break`.

---

## 🔄 Same applies to `while` loops

```python
i = 0
while i < 4:
    print(i)
    i += 1
else:
    print("While loop finished without a break!")
```

---

## 🧠 Summary Table:

| Statement  | What it does                        |
| ---------- | ----------------------------------- |
| `break`    | Stops the loop completely           |
| `continue` | Skips the rest of current iteration |
| `else`     | Runs only if loop wasn't broken     |

---

---

---

---

---

## 🔁 What is a `while` loop?

A `while` loop keeps running **as long as a condition is true**.

### 🧠 Think of it like:

> “Keep doing this **while** the condition is true.”

---

### 📌 Syntax:

```python
while condition:
    # do something
```

If the condition becomes `False`, the loop **stops**.

---

## 🧃 1. Basic Example

```python
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
```

### Output:

```
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```

> Here, it loops while `count` is less than 5.

---

## ⚠️ 2. Infinite Loop (Be Careful!)

If you forget to update the variable inside the loop, it might run forever:

```python
while True:
    print("This will run forever!")
```

Use `Ctrl + C` to stop it in the terminal.

---

## 👀 3. Using `while` for Input Validation

```python
user_input = ""

while user_input != "yes":
    user_input = input("Do you want to continue? (type 'yes' to continue): ")

print("Great! Let's move on.")
```

### 💬 Output (example):

```
Do you want to continue? (type 'yes' to continue): no
Do you want to continue? (type 'yes' to continue): maybe
Do you want to continue? (type 'yes' to continue): yes
Great! Let's move on.
```

---

## 🎯 4. While + Break

```python
x = 0
while True:
    print(x)
    x += 1
    if x == 3:
        break
```

### Output:

```
0
1
2
```

> `break` is used to **exit** the loop even if the condition is still `True`.

---

## ⏭️ 5. While + Continue

```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
```

### Output:

```
1
2
4
5
```

> Skips the `print()` when `num` is 3.

---

## 💡 Real Example: Countdown Timer

```python
import time

countdown = 5
while countdown > 0:
    print("Countdown:", countdown)
    time.sleep(1)  # wait 1 second
    countdown -= 1

print("Time's up!")
```

---

## ⚡ Use Cases for `while` Loops:

- Waiting for correct user input
- Repeating something until a condition is met
- Games (e.g., "keep playing until you lose")
- Polling for a status (like waiting for a server)

---
