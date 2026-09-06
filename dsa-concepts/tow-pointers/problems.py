# ==============================
# TWO POINTERS - 5 PRACTICE PROBLEMS
# ==============================

# Problem 1: Pair Sum
arr = [1, 3, 4, 6, 8, 10, 13, 15]
arr.sort()
target = 14

# Find ALL pairs whose sum equals target.
# Use two pointers.


left = 0
right = len(arr) - 1

while left < right:
    sum = arr[left]+arr[right]
    if sum == target:
        print(f"This pair with index {left} and {right} with elemnts {arr[left]} and {arr[right]} targets sum == >> {target}")
        left += 1
        right -= 1
    elif sum > target:
        right -= 1
    else:
        left += 1





# # --------------------------------------------------




# # --------------------------------------------------

# # Problem 4: Three Sum
# arr = [-4, -1, -1, 0, 1, 2, 3, 5]
# target = 0

# # Find ALL UNIQUE triplets whose sum equals target.
# # Use sorting + two pointers.
# #
# # Expected triplets include:
# # [-1, -1, 2]
# # [-1, 0, 1]


# # --------------------------------------------------

# # Problem 5: Container With Most Water
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# # Find the maximum amount of water that can be contained.
# # Use ONLY the two-pointer approach.
# #
# # Expected answer:
# # 49