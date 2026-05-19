for i in range(10):
    for j in range(10):
        if i==j or j == 0 or i == 9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()