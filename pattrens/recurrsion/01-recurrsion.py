list1 = [1,2,3,[4,5,6,7,[8,9,10,[11,12,13,14]]]]
print(list1)

def recurrsion(arr):
    falt = []
    for element in arr:
        if type(element) == list:
            # print(element)
            falt.extend(recurrsion(element))
        else:
            falt.append(element)
    return falt

result = recurrsion(list1)
print(result)


list2 = [1,2,3,4,5]
list3 = [10,6,7,8,9]
list2.extend(list3)
print(list2)