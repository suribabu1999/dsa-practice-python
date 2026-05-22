list1 = [1,2,3,4,5,6,7,8,9]
k = 3

initial_window_sum = sum(list1[0:k])
print(initial_window_sum)
max_sum = 0

for i in range(k, len(list1)):
    initial_window_sum = initial_window_sum-list1[i-k] + list1[i]
    max_sum = max(max_sum,initial_window_sum)

print(max_sum)
