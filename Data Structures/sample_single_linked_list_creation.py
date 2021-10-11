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
n1 = node(10)
L.head = n1
n2 = node(20)
n1.next = n2
n3 = node(30)
n2.next = n3
L.display()
