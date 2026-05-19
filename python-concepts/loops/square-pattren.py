for i in range(10):
    pass
    # print("*", end=" ") # prints in straight because it has i index from 0 to range(10)

for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print()