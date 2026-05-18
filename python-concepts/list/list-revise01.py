# Student Score Analyzer

# scores = [78, 45, 90, 66, 45, 88, 92, 67, 78, 59]

# Tasks:
# 1. Print the highest and lowest score
# 2. Count how many students passed (pass mark >= 60)
# 3. Remove duplicate scores and store in a new list
# 4. Add 5 bonus marks to every score
# 5. Print scores in ascending and descending order
# 6. Print top 3 scores
# 7. Find the average score


scores = [78, 45, 90, 66, 45, 88, 92, 67, 78, 59]

# highest and lowest
print("Highest:", max(scores))
print("Lowest:", min(scores))


# passed students
passed = 0
for s in scores:
    if s >= 60:
        passed += 1

print("Passed students:", passed)


# remove duplicates
unique_scores = []
for s in scores:
    if s not in unique_scores:
        unique_scores.append(s)

print("Unique scores:", unique_scores)


# add bonus marks
bonus_scores = []
for s in scores:
    bonus_scores.append(s + 5)

print("Bonus scores:", bonus_scores)


# sorting
print("Ascending:", sorted(scores))
print("Descending:", sorted(scores, reverse=True))


# top 3 scores
top3 = sorted(scores, reverse=True)[:3]
print("Top 3 scores:", top3)


# average score
average = sum(scores) / len(scores)
print("Average score:", average)