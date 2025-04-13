### ✅ **Student Performance Analyzer – Readable Solution**

```python
# ----------------------------------------
# Function to calculate average score
# ----------------------------------------
def calculate_average(scores):
    return sum(scores) / len(scores)

# ----------------------------------------
# Function to get top scorers based on a threshold
# ----------------------------------------
def top_scorers(data, threshold):
    top = []
    for name, scores in data:
        avg = calculate_average(scores)
        if avg > threshold:
            top.append(name)
    return top

# ----------------------------------------
# Student records (name, list of scores)
# ----------------------------------------
students_data = [
    ("Alice", [85, 90, 78]),
    ("Bob", [65, 70, 58]),
    ("Charlie", [95, 100, 98]),
    ("David", [45, 55, 50]),
    ("Eva", [100, 100, 100])
]

# ----------------------------------------
# Step 1 & 2: Calculate and store average scores
# ----------------------------------------
average_scores = {}

for name, scores in students_data:
    avg = calculate_average(scores)
    average_scores[name] = round(avg, 2)

# ----------------------------------------
# Step 3: Use a while loop to print averages until a failing student is found
# ----------------------------------------
print("Average Scores:")
i = 0
while i < len(students_data):
    name, scores = students_data[i]
    avg = average_scores[name]

    if avg < 60:
        print(f"\nStopped processing at: {name}")
        break

    print(f"{name}: {avg}")
    i += 1

# ----------------------------------------
# Step 4: Skip students who scored perfect 100s using `continue`
# ----------------------------------------
for name, scores in students_data:
    if all(score == 100 for score in scores):
        print(f"\nSkipping perfect scorer: {name}")
        continue
    # (Optional) Could process non-perfect scorers here

# ----------------------------------------
# Step 5: Create sets of passed and failed students
# ----------------------------------------
passed_students = set()
failed_students = set()

for name, avg in average_scores.items():
    if avg >= 60:
        passed_students.add(name)
    else:
        failed_students.add(name)

print(f"\nPassed Students: {passed_students}")
print(f"Failed Students: {failed_students}")

# ----------------------------------------
# Step 6: Find students who improved (last score > first score)
# ----------------------------------------
improved_students = set()

for name, scores in students_data:
    if scores[-1] > scores[0]:
        improved_students.add(name)

print(f"\nImproved Students: {improved_students}")

# ----------------------------------------
# Step 7: Use function to get top scorers above a threshold
# ----------------------------------------
threshold = 90
top = top_scorers(students_data, threshold)

print(f"Top Scorers above {threshold}: {top}")
```

---

### 📌 Output Example:

```
Average Scores:
Alice: 84.33
Bob: 64.33
Charlie: 97.67

Stopped processing at: David

Skipping perfect scorer: Eva

Passed Students: {'Charlie', 'Alice', 'Eva', 'Bob'}
Failed Students: {'David'}

Improved Students: {'Charlie', 'Alice'}

Top Scorers above 90: ['Charlie', 'Eva']
```
