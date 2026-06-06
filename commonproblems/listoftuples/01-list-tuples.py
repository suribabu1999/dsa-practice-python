students = [
    ("Ravi", 85),
    ("Priya", 92),
    ("Arjun", 78),
    ("Sita", 92),
    ("Rahul", 67),
    ("Meena", 85)
]

# first take out all the marks to find the highist marks 

marks = [mark for name, mark in students ]
h_marks = max(marks)
print("highest marks ===>>>" ,h_marks)

names = [name for name, mark in students]
print("names present in the tuple---->",names)

print(marks)

highest_mark = [mark for name, mark in students]
top_students = []

top_student = [name for name, mark in students if mark == h_marks]
print("top student ------->",top_student)

for name, mark in students:
    if mark == highest_mark:
        top_students.append(name)

print("Top Students:", top_students)


total = 0

for name, mark in students:
    total += mark

average = total / len(students)

print("Average Marks:", average)


above_80 = []

for name, mark in students:
    if mark > 80:
        above_80.append((name, mark))

print("Students Above 80:", above_80)


sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("\nStudents Sorted By Marks:")

for student in sorted_students:
    print(student)


freq = {}

for name, mark in students:
    if mark in freq:
        freq[mark] += 1
    else:
        freq[mark] = 1

print("\nMarks Frequency:")
print(freq)