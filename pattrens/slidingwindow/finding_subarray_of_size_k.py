#finidng all the sub arrays of some fixed size 

def sub_array(arr,k):

    n = len(arr)

    window = arr[0:k] #intial window of size k
    result = []
    result.append(window[:]) #first window append to result

    for i in range(k,n):  # taking every window hear the trick is poping the first elemnt and adding new element in the last
        window.pop(0)
        window.append(arr[i])
        result.append(window[:])

    return result

print(sub_array([1,2,3,4,5,6,7,8,9],2))



