# # Problem 3: Move Zeroes
arr = [0, 1, 0, 3, 12, 0, 5, 0, 7, 8]

# # Move all zeroes to the end.
# # Maintain the original order of non-zero elements.
# # Don't use sort().
# #
# # Expected:
# # [1, 3, 12, 5, 7, 8, 0, 0, 0, 0]

left = 0
right = 1

while left < len(arr):
    if arr[left] == 0:
        arr[left] = arr[right]
        left +=1
        right +=1
    else:
        left +=1
        right +=1
print(arr)