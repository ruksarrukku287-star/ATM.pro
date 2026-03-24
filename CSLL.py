class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CSLL:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
                       if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
          new_node=Node(data)                                                                                                                                                
          if self.head is None:
              self.head=new_node
              new_node.next=self.head
              return

          temp=self.head
          while temp.next!=self.head:
            temp=temp.next
          temp.next=new_node
          new_node.next=self.head
    def display(self):
        temp=self.head
        if temp is None:
            print("list is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp==self.head:
                break
        print("back to Head")
    def delete(self,key):
        if self.head is None:
            print("List empty")
            return
        temp=self.head
        if temp.data==key:
            while temp.next!=self.head:
                temp=temp.next
            if temp==self.head:
                self.head=None
                return
            temp.next=self.head.next
            self.head=self.head.next
            return
        prev=self.head
        temp=self.head.next
        while temp!=self.head:
            if temp.data==key:
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next
        print("value not found")
csll=CSLL()
while True:
    print("\n1.Insert Beginning")
    print("2.Insert End")
    print("3.Display")
    print("4.Delete")
    print("5.Exit")
    choice=int(input("Enetr choice:"))
    if choice==1:
        val=int(input("Enter value:"))
        csll.insert_begin(val)
    elif choice==2:
        val=int(input("Enter value:"))
        csll.insert_end(val)
    elif choice==3:
        csll.display()
    elif choice==4:
        val=int(input("Enter value to delete:"))
        csll.delete(val)
    elif choice==5:
        print("program ended:")
    else:
        print("invalid option:")
        
            
        
