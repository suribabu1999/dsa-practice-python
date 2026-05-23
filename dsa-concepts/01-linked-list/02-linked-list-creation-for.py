class LinkedNode:
    def __init__(self,val):
        self.val= val
        self.next= None

def linked_list(arr):
    first_node = LinkedNode(arr[0])

    head = first_node
    current = head

    for i in range(1,len(arr)):
        current.next = LinkedNode(arr[i])
        current = current.next
    return head

res = linked_list([1,2,3,4,5])
temp = res

while temp:
    print(temp.val, end= '-->')
    temp = temp.next