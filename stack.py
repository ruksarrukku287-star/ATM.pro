stack=[]
def push():
    x=int(input("enter element to push:"))
    stack.append(x)
    print(x,"pushed into stack")
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        re_ele=stack.pop()
        print(re_ele,"popped from stack")
def peek():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Top element is:",stack[-1])
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("stack elements (top to bottom):")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
def length():
    print("Number of elements in stack:",len(stack))
while True:
    print("\n---stack operations---")
    print("1.push")
    print("2.pop")
    print("3.peek")
    print("4.display")
    print("5.length")
    print("6.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        peek()
    elif choice==4:
        display()
    elif choice==5:
        length()
    elif choice==6:
        print("program ended")
        break
    else:
        print("Invalid choice")
