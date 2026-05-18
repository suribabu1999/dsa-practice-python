# Dictionary Practice Problem

# data = {
#     "Alice": 78,
#     "Bob": 45,
#     "Charlie": 90,
#     "David": 66,
#     "Eva": 88,
#     "Frank": 92,
#     "Grace": 59
# }

# Tasks:
# 1. Print all student names
# 2. Print all scores
# 3. Find the student with the highest score
# 4. Count how many students passed (pass mark >= 60)
# 5. Add 5 bonus marks to each student
# 6. Remove students who scored below 50
# 7. Find the average score


data = {
    "Alice": 78,
    "Bob": 45,
    "Charlie": 90,
    "David": 66,
    "Eva": 88,
    "Frank": 92,
    "Grace": 59
}


# 1. print student names
print("Students:", list(data.keys()))


# 2. print scores
print("Scores:", list(data.values()))


# 3. highest score
top_student = max(data, key=data.get)
print("Top student:", top_student, data[top_student])


# 4. count passed students
passed = 0
for name, score in data.items():
    if score >= 60:
        passed += 1

print("Passed students:", passed)


# 5. add bonus marks
bonus_data = {}
for name, score in data.items():
    bonus_data[name] = score + 5

print("Bonus scores:", bonus_data)


# 6. remove students below 50
filtered = {}
for name, score in data.items():
    if score >= 50:
        filtered[name] = score

print("After removing below 50:", filtered)


# 7. average score
average = sum(data.values()) / len(data)
print("Average score:", average)