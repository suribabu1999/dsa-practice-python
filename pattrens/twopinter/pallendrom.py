def pallendrome(string):
    left, right = 0 , len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left+=1
        right-=1
    return True


print(pallendrome("kjsdf"))

list1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]