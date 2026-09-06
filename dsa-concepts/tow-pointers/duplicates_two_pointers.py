# # Problem 2: Remove Duplicates
arr= [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 6]

# Remove duplicates IN-PLACE using two pointers.
# Expected:
# [1, 2, 3, 4, 5, 6]
arr.sort()
left = 0
right = 1

while right < len(arr):
    if arr[left] == arr[right]:
        right+=1
    else:
        left +=1
        arr[left] = arr[right]
        right += 1
print(f" {left} and {right}")
print(arr[:left+1])
        

