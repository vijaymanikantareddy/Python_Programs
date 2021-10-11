class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        if self.head is None:
            print('List is empty')
        else:
            while temp:
                print(temp.data, end=' ')
                temp = temp.next

L = SLL()
val = int(input('enter data or -1 to stop: '))
while val != -1:
    n = node(val)
    if L.head == None:
        L.head = n
        n.next = None
    else:
        temp = L.head
        while temp.next != None:
            temp = temp.next
        temp.next = n
        n.next = None
    val = int(input('enter data or -1 to stop: '))
print('The list is : ', end = '')
L.display()
