list1 = [1,2,[1,2,3],[4,5,6,7,[8,9,10]]]

list2 = [
    y if not isinstance(y,list) else z
    for x in list1
    for y in (x if isinstance(x,list) else [x])
    for z in ([y] if not isinstance(y,list) else y)
]

print(list2)