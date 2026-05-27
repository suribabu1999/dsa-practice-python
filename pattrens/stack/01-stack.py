s = "({[]})"

#this is for checking brackets are balenced on each side 

stack = []

mapping = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

valid = True

for char in s:

    # opening brackets
    if char in "({[":
        stack.append(char)

    # closing brackets
    else:

        if not stack:
            valid = False
            break

        top = stack.pop()

        if mapping[char] != top:
            valid = False
            break

print(valid)