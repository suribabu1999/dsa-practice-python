def amstrong(x):
    lis = []
    sum = 0
    temp = 0
    
    while x > 0:
        num = x % 10
        lis.append(num)
        x = x//10

    length = len(lis)

    while temp < length:
        sum += lis[temp] **length
        temp +=1
    print(sum)
    

amstrong(153)

