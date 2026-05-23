class ListCretion:
    def __init__(self,val):
        self.val = val
        self.next = None

l1 = [1,2,3]
head = ListCretion(l1[0])  #deciding the first node here
current = head #creating current next node 
# print(head.val)
# print(head.next)
# current.next = 10
# print(current.next)
for i in range(1,len(l1)):
     current.next = ListCretion(l1[i])
     current = current.next
    
temp =  head
while temp:
    print('---->>',temp.val)
    temp = temp.next

    

