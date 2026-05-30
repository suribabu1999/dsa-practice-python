num = [n for n in range(1,8)]
print(num)
k = 3
initial_window = num[:k]
result = []
result.append(initial_window[:])

for i in range(len(num)):
    initial_window.pop(0)
    initial_window.append(num[i])
    result.append(initial_window[:])

print(result)