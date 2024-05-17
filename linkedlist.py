class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class list:
    def __init__(self):
        self.head=None
    def printll(self):
        if self.head is None:
            print("the list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def addbegin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def addend(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def addmiddle(self,data,x):
        n=self.head
        while n.data is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("x not present")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node    
    def addbef(self,data,x):
        if self.head is None:
            print("the list is empty")
            return
        if self.head.data==x:
            new_node=node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("the elemet is notr found")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
                    
ll1=list()
ll1.addbegin(10)
ll1.addbegin(20)
ll1.addbef(11,20)
ll1.addmiddle(12,20)
ll1.addend(100)
ll1.printll()