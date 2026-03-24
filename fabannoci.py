a=0
b=1
n=int(input("enter number"))
print(a,b)
for i in range (0,n,1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c






def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(0,9):
    print (fib(i))




    
        
