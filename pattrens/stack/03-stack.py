list1 = [n for n in range(1,11)]

stack = []
result = [-1]*(len(list1))
print(list1)
# print(len(result))

for i in range(len(list1)-1,-1,-1):
    while stack and stack[-1] <= list1[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(list1[i])
print(result)