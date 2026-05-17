nums = [1,2,3,3,4,2,8,8,8,8,9,6,6,6,6]

found = set()

for num in nums:
    if num in found:
        print("First found num", num)
        break
    found.add(num)