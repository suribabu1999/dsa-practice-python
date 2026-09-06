arr = [-4, -1, -1, 0, 1, 2, 3, 5]
target = 0
arr.sort()

left = 0
right = len(arr) - 1

for i in range(len(arr)-2):
    sum = arr[i] + arr[left+1] + arr[right]

    if sum == target:
        print(f"This triplet with index {i}, {left+1} and {right} with elemnts {arr[i]}, {arr[left+1]} and {arr[right]} targets sum == >> {target}")
        left += 1
        right -= 1
    elif sum > target:
        right -= 1
    else:
        left += 1
    