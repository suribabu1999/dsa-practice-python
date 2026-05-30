class Linkedlist:
    def __init__(self,val):
        self.val = val
        self.next = None


a = Linkedlist(1)
b = Linkedlist(2)
c = Linkedlist(3)
d = Linkedlist(4)

a.next = b
b.next = c
c.next = d

head = a


def find_middle(a):
    fast = a
    slow = a
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

result = find_middle(head)
print(result.val)