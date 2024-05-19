class Node:
    def __init__(self, data=None):
          
        self.data = data
        
        self.next = None  
       
        self.prev = None
 

class DoublyLInkedList:
 
    def __init__(self):
        self.head = None
 
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
     
   
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
 
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        curr = Node()
        curr = self.head
 
        while(curr != None):
            print(curr.data)
            curr = curr.next
 
        print()
 
 
head = DoublyLInkedList()
head.insert_at_begin(10)
head.insert_at_begin(20)
head.insert_at_begin(30)
 
print("List after inserting node at begining:")
head.print_list()
 
head.delete_at_begin()
print("List after deleting node from begining:")
head.print_list()
head.delete_at_begin()
head.delete_at_begin()
head.delete_at_begin()