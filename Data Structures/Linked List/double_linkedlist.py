class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def insert_beg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self,index,data):
        new_node = Node(data)
        if index==0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        else:         
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length+=1

    def remove(self,index):
        if index==0:
            self.head=self.head.next
            self.length-=1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        leader = self.traversetoindex(index-1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1


    def traversetoindex(self,index):
        curr_node = self.head
        i = 0
        while i!= index:
            curr_node = curr_node.next
            i+=1
        return curr_node

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data , end = ' ')
            temp = temp.next
        print()
        print('Length ' + str(self.length))        
            
        
d = DoublyLinkedList()
val = int(input('enter data or -1 to stop: '))
while val != -1:
    d.append(val)
    val = int(input('enter data or -1 to stop: '))
d.insert_beg(int(input('enter data to insert at beginning: ')))
d.insert(2,22)
d.remove(3)
d.display()
