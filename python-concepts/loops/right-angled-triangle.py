for i in range(10):
    for j in range(10):
        if j == 9 or i==9 or i+j==9:
            print(f"{i}",end=' ')
        else:
            print(" ", end=' ')
    print()