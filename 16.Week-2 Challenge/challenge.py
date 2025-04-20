students_data = [
    ("Alice", [85, 90, 78]),
    ("Bob", [65, 70, 58]),
    ("Charlie", [95, 100, 98]),
    ("David", [45, 55, 50]),
    ("Eva", [100, 100, 100])
]

def calculate_average(scores):
    avg=sum(scores)/len(scores)
    return avg
average_scores={}
for name,scores in students_data:
    avg =calculate_average(scores)
    average_scores[name]=round(avg,2)
print(average_scores)    

students_name=list(average_scores.keys())
i=0

while i<len(students_name):
    name=students_name[i]
    avg=average_scores[name]
    if avg < 60:
        print(f"\nStopped processing at: {name}")
        break
    print(f"{name}:{avg}")
    i +=1

for name,scores in students_data:
    if all(score==100 for score in scores):
        print(f"\nSkipping perfect scorer: {name}")
        continue

passed_students = set()
failed_students = set()

for name, avg in average_scores.items():
    if avg>=60:
        passed_students.add(name)
    else:
        failed_students.add(name)    


print(f"\nPassed Students: {passed_students}")
print(f"Failed Students: {failed_students}")        


# Step 6: Find students who improved
improved_students = set()

for name, scores in students_data:
    if scores[-1] > scores[0]:  # last score > first score
        improved_students.add(name)

print(f"\nImproved Students: {improved_students}")
