class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next   #moment of nodes
        fast = fast.next.next
    return slow 

a = Node(1)
print(a.next)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

Head = a
print(a.val)
print(a.next.val)
middle = find_middle(Head)
# print(middle.val)
