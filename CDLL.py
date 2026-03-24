class Node:
    def __init_(self,data):
        self.data=data
        self.prev=None
        self.next=None
class CDLL:
    def __init_(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=new_node
            new_node.prev=new_node
            self.haed=new_node
            return
        last=self.head.prev
        new_node.next=self.head
        new_node.prev=last
        last.next=new_node
        self.head.prev=new_node
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
            return
        last=self.head.prev
        last.next=new_node
        new_node.prev=last
        new_node.next=self.head
        self.head.prev=new_node
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next==self.head:
            self.head=None
            return
        last=self.head.prev
        self.head=self.head.next
        self.head.prev=last
        last.next=self.head
    def delete_end(Self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next==self.head:
            self.head=None
            return
        last=self.head.prev
        second_last=last.prev
        second_last.next=self.head
        self.head.prev=second_last
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="<->")
            temp=temp.next
            if temp==self.head:
                break
            print()
    def search(self,key):
        if self.head is None:
           print("List is empty")
           return
        temp=self.head                                                          
        pos=1
        while True:
            if temp.data==key:
                print("Element found at position:",pos)
                return
            temp=temp.next
            pos+=1
            if temp==self.head:
                break
            print("Element not found")
    def count_of_nodes(self):
         count=0
         temp=self.head
         while(temp.next is not self.head):
             count+=1
             temp=temp.next
         print("the count of nodes in list",count)    
        
        
        
