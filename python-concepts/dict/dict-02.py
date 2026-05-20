company = {
    "Alice": {"dept": "Engineering", "salary": 80000, "age": 28},
    "Bob":   {"dept": "Marketing",   "salary": 60000, "age": 32},
    "Carol": {"dept": "Engineering", "salary": 90000, "age": 35},
}
ages = []
salarys = []
for key, values in company.items():
    # print(f"key {key} _----> {values}")
    for i, j in values.items():
        print(f"{i} --------------> {j}")
        if i == "age":
            ages.append(j)
        if i == 'salary':
            salarys.append(j)
print(max(ages))
print(f"{[i for i  in salarys if i > 60000 ]}")