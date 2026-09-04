list1 = [11,1,2,2,2,2,2,3,3,3,4,5,6,7,7,7,7,8,8,8,6]
freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for index, value in freq.items():
    # print("i",index," ---> val",value)
    # if value>1:
    #     print("values more than 1::",value)
    temp = 0
    if value > temp:
        temp = value
print(temp)
    