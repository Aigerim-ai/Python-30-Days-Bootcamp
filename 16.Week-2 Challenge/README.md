### 🧠 Python Challenge: **Student Performance Analyzer**

#### 📝 Background:

A school has asked you to develop a simple program that analyzes student performance. You'll be working with data in **tuples**, using **loops** and **functions** to process it, storing results in **dictionaries**, and applying **set operations** to find special cases.

---

### 📌 Problem Statement:

You are given a list of student records where each record is a **tuple** of the form:

```python
(name, [list_of_scores])
```

Example:

```python
students_data = [
    ("Alice", [85, 90, 78]),
    ("Bob", [65, 70, 58]),
    ("Charlie", [95, 100, 98]),
    ("David", [45, 55, 50]),
    ("Eva", [100, 100, 100])
]
```

Your task is to:

1. **Create a function** called `calculate_average(scores)` that returns the average score of a list of integers.
2. **Use a for loop** to process each student’s data and store the result in a dictionary where:
   - key: student name
   - value: average score
3. **Use a while loop** to print each student's name and average score **until you encounter a student with an average below 60** (and then stop the loop using `break`).
4. **Use a loop and `continue`** to skip students who scored a perfect 100 in all subjects.
5. **Create a set** of students who passed (average ≥ 60) and another for those who failed.
6. **Print students who improved**: those whose **last score is higher than the first**.
7. Make sure your code uses **correct Python indentation**, and test it with the provided data.

---

### ✅ Bonus:

Write a function `top_scorers(data, threshold)` that returns the names of students whose average score is greater than the given `threshold`.

---

### 🎯 Sample Output:

```
Average Scores:
Alice: 84.33
Bob: 64.33
Charlie: 97.67

Stopped processing at: David

Skipping perfect scorer: Eva

Passed Students: {'Alice', 'Charlie', 'Bob', 'Eva'}
Failed Students: {'David'}

Improved Students: {'Alice', 'Charlie'}
Top Scorers above 90: ['Charlie', 'Eva']
```

---
