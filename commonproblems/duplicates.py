arr = [1,2,3,4,5,6,4,3,2,1]

def duplicates(arr):
    count = {}
    for item in arr:
        if item in count:
            count[item] +=1
        else:
            count[item] = 1
    print(count)
    dup = []
    for k,v in count.items():
        if v > 1:
            dup.append(k)
        if v == 1:
            print("First unique non repeting number", k)
            break
    print("Duplicate elements ",dup)

    


duplicates(arr)